import json
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from works.models import Works
import datetime
from datetime import date


def load_cv_data():
    with open(settings.BASE_DIR / 'data' / 'cv_data.json', 'r') as file:
        return json.load(file)


def works(request):
    cv_data = load_cv_data()
    works_qs = (
        Works.objects
        .prefetch_related('skills', 'projectsunderworks_set')
        .all()
        .order_by('-start_date')
    )
    
    
    today = date.today()
    earliest_start = None
    latest_end = None

    for work in works_qs:
        if not work.start_date:
            continue
        start = work.start_date
        end = work.end_date or today
        if end < start:
            end = today

        if earliest_start is None or start < earliest_start:
            earliest_start = start
        if latest_end is None or end > latest_end:
            latest_end = end

    total_years = None
    if earliest_start and latest_end:
        total_years = latest_end.year - earliest_start.year
        if (latest_end.month, latest_end.day) < (earliest_start.month, earliest_start.day):
            total_years -= 1
        if total_years < 0:
            total_years = 0
    
    return render(request, 'works/experience_list.html', {
        'works': works_qs,
        'cv': cv_data,
        'total_years': total_years,
        'active_page': 'works',
    })


def work_detail(request, work_id):
    cv_data = load_cv_data()
    work = get_object_or_404(
        Works.objects.prefetch_related('skills', 'projectsunderworks_set'),
        id=work_id
    )
    
    return render(request, 'works/experience_detail.html', {
        'work': work,
        'cv': cv_data,
        'active_page': 'works',
    })
    
    