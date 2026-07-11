from django.urls import path
from . import views

urlpatterns = [
    path('', views.works, name='works'),
    path('<uuid:work_id>/', views.work_detail, name='work_detail'),
]