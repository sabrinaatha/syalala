from django.urls import path
from . import views

app_name = 'connectme'

urlpatterns = [
    path('', views.connect, name='connect'),
]