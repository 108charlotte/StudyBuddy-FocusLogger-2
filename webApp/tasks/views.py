from django.shortcuts import render

# Create your views here.
def tasks(request): 
    if "task_list" not in request.session: 
        request.session["task_list"] = []
    
    task_list = request.session["task_list"]

    if request.method == "POST": 
        new_task = request.POST["task"]
        task_list.append(new_task)
        request.session['task_list'] = task_list
        request.session.modified = True

    return render(request, "tasks/tasks.html", {
        "tasks": task_list
    })