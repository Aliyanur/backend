from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden

def todo_list(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    todos = Todo.objects.filter(owner=request.user)
    return render(request, 'todo_list.html', {'todos': todos})


def todo_detail(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    todo = get_object_or_404(Todo, id=id, owner=request.user)
    return render(request, 'todo_detail.html', {'todo': todo})


def todo_create(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.save()
            return redirect('/todos/')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})


def todo_delete(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    todo = get_object_or_404(Todo, id=id, owner=request.user)
    todo.delete()
    return redirect('/todos/')


def todo_update(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    todo = get_object_or_404(Todo, id=id, owner=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_form.html', {'form': form})


def register_view(request):
    print('ok2')
    if request.method == 'POST':
        print('okokoko')
        form = RegisterForm(request.POST)
        print(form.errors, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/todos/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')
