from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Task
from .forms import TaskForm
from datetime import datetime, timedelta


@login_required
def index(request):
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    q = request.GET.get('q')
    if q:
        tasks = tasks.filter(title__icontains=q)
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title == '':
            raise ValidationError("Title must be filled")
        deadline = datetime.now().date() + timedelta(days=3)
        Task.objects.create(user_id=user_id, title=title, deadline=deadline)
    ctx = {
        'object_list': tasks
    }
    return render(request, 'task/index.html', ctx)


@login_required
def edit(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:index')
    ctx = {
        'form': form,
        'obj': task,
    }
    return render(request, 'task/edit.html', ctx)


@login_required
def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task:index')
    ctx = {
        'obj': task
    }
    return render(request, 'task/delete.html', ctx)
