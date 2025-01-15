from django.shortcuts import render
from django.urls import path
from . import views

urlpatters = [
    path('', views.home, name='home')
]

# A simple view function
def home(request):
    return render(request, 'studyBuddy/index.html')  # Adjust the template path as needed
