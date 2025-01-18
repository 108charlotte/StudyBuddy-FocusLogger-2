from django.urls import path
from . import views

app_name = 'tasks'  # Add this line to avoid namespace conflicts

urlpatterns = [
    path('tasks/', views.tasks, name='task_list'),  # Define clear views
]
