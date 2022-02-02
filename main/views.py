from asyncio import tasks
from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task


def index(request):
    context = {
        'title': "Main page website",
        'tasks': Task.objects.order_by('-id')
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About page website'
    }
    return render(request, 'main/about.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = "Form empty"
        
    context = {
        'title': 'Create new task',
        "form": TaskForm()
    }
    return render(request, 'main/create.html', context)
