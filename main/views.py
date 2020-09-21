from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task

# Create your views here.

def home(request):
    content = { 'tasks': Task.objects.all().order_by('-status','-added_time') }
    return render(request, 'main/home.html', content)

def add_task(request):
    new_task_text = request.POST['task_text']
    new_task = Task(text=new_task_text, status='Not Started')
    new_task.save()
    return HttpResponseRedirect('/')

def delete_task(request, task_id):
    print(task_id)
    taskToDel = Task.objects.get(pk=task_id)
    print(taskToDel)
    taskToDel.delete()
    return HttpResponseRedirect('/')

def open_task(requset, task_id):
    print(task_id)
    task = Task.objects.get(pk=task_id)
    task.status = 'In Progress'
    task.save()
    return HttpResponseRedirect('/')

def close_task(request, task_id):
    print(task_id)
    task = Task.objects.get(pk=task_id)
    task.status = 'Finished'
    print(task)
    task.save()
    return HttpResponseRedirect('/')