import json

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from projects.models import Project


def load_cv_data():
    with open(settings.BASE_DIR / 'data' / 'cv_data.json', 'r') as file:
        return json.load(file)


def projects(request):
    cv_data = load_cv_data()

    projects = (
        Project.objects
        .prefetch_related('skills')
        .all()
        .order_by('-id')
    )

    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'cv': cv_data,
        'active_page': 'projects',
    })


def project_detail(request, project_id):
    cv_data = load_cv_data()

    project = get_object_or_404(
        Project.objects.prefetch_related('skills'),
        id=project_id
    )

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'cv': cv_data,
        'active_page': 'projects',
    })