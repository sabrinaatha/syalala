import json
from django.shortcuts import render
from django.conf import settings
from django.templatetags.static import static
from django.db import connection

from works.models import Works
from projects.models import Project
from skills.models import Skills

# Load CV data from JSON file
def load_cv_data():
    with open(settings.BASE_DIR / 'data' / 'cv_data.json', 'r') as file:
        return json.load(file)

# Resolve photo URLs for static and direct link values
def resolve_photo_url(path: str) -> str:
    if not path:
        return ''
    normalized = path.strip()
    if normalized.startswith(('http://', 'https://', '//', '/')):
        return normalized
    if normalized.startswith('static/'):
        normalized = normalized[len('static/'):]
    if normalized.startswith('/'):
        normalized = normalized[len('/'):] 
    return static(normalized)

def home(request):
    cv_data = load_cv_data()
    cv_data['profile']['photo_url'] = resolve_photo_url(cv_data['profile'].get('photo', ''))

    works_qs = (
        Works.objects
        .prefetch_related('skills')
        .all()
        .order_by('-start_date')
    )

    projects_qs = (
        Project.objects
        .prefetch_related('skills')
        .all()
        .order_by('-start_date')
    )

    skills_qs = (
        Skills.objects
        .all()
        .order_by('type', 'skills_name')
    )

    return render(request, 'main_project/home.html', {
        'cv': cv_data,
        'works': works_qs,
        'projects': projects_qs,
        'skills': skills_qs,
        'active_page': 'home',
        'contact_status': request.GET.get('contact')
    })
