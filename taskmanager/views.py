from django.shortcuts import render
from .models import Task

def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})
