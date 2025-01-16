from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def login(request): 
    if request.method == 'GET': 
        return render(request, 'authentication/login.html')

def register(request): 
    # chatgpt code, since I don't know django yet
    if request.method == 'GET': 
        return render(request, 'authentication/register.html')

    username = request.POST['username']
    password = request.POST['password']
    repeat = request.POST['repeat']
    if repeat == password: 
        if User.objects.filter(username=username).exists(): 
            messages.error(request, 'Username already exists')
        else: 
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('sessionLogger/home')
    else: 
        messages.error(request, 'Passwords do not match')
    return render(request, 'authentication/register.html')

def logout(request): 
    return render(request, "authentication/login.html")