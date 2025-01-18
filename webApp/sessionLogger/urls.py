from django.urls import path
from . import views

app_name = 'sessionLogger'  # Add this line to avoid namespace conflicts

urlpatterns = [
    path('', views.home, name='home'),  # Define clear views
]
