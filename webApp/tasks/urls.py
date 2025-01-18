from django.urls import path
from . import views

app_name = 'tasks'  # Add this line to avoid namespace conflicts

urlpatterns = [
    path('', views.tasks, name='tasks'),  # Define clear views
]
