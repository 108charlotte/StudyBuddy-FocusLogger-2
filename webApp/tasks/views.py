from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create your views here.
def tasks(request): 
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })