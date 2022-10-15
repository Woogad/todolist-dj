from django.shortcuts import redirect, render
from .models import Todo
from .forms import *


def index(req):
    todos = Todo.objects.all()
    form = TodoForm()
    if req.method == 'POST':
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'todos': todos, 'form': form}
    return render(req, 'todo/index.html', context)


def updateTodo(req, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if req.method == 'POST':
        form = TodoForm(req.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(req, 'todo/updateTodo.html', context)


def deleteTodo(req, pk):
    item = Todo.objects.get(id=pk)
    if req.method == 'POST':
        item.delete()
        return redirect("/")
    context = {'item': item}
    return render(req, 'todo/deleteTodo.html', context)


def getTodo(req, pk):
    todo = Todo.objects.get(id=pk)
    context = {'todo': todo}
    return render(req, 'todo/todo.html', context)
