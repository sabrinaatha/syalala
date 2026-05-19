import json
from django.shortcuts import render
from django.conf import settings

# Load CV data from JSON file
def load_cv_data():
    with open(f"{settings.BASE_DIR}/main_project/data/cv_data.json", "r") as file:
        return json.load(file)

def home(request):
    cv_data = load_cv_data()
    return render(request, 'main_project/home.html', {"cv": cv_data})
