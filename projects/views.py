from django.shortcuts import render

# Create your views here.

def project_home(request):
    return render(request, 'projects/home.html')
