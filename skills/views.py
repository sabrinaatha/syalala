import json
from django.conf import settings
from django.shortcuts import render
from projects.models import Skills


def load_cv_data():
    with open(settings.BASE_DIR / 'data' / 'cv_data.json', 'r') as file:
        return json.load(file)


def skills(request):
    cv_data = load_cv_data()
    skills_qs = Skills.objects.all().order_by('type', 'skills_name')
    skills_total = skills_qs.count()
    technologies_count = skills_qs.values_list('skills_name', flat=True).distinct().count()
    beginner_count = skills_qs.filter(ability_level__in=['Beginner']).count()
    intermediate_count = skills_qs.filter(ability_level__in=['Intermediate']).count()
    advanced_plus_count = skills_qs.filter(ability_level__in=['Advanced', 'Expert']).count()
    categories_count = skills_qs.values_list('type', flat=True).distinct().count()

    return render(request, 'skills/skills.html', {
        'skills': skills_qs,
        'cv': cv_data,
        'active_page': 'skills',
        'skills_total': skills_total,
        'technologies_count': technologies_count,
        'beginner_count': beginner_count,
        'intermediate_count': intermediate_count,
        'advanced_plus_count': advanced_plus_count,
        'categories_count': categories_count,
    })