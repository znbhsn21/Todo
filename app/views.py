from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Task
from .forms import TaskForm, CustomLoginForm, CustomSignupForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "home.html", {"tasks": tasks})

@login_required
def task_add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "task_add.html", {"form": form})

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_edit.html", {"form": form, "task": task})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("home")
    return render(request, "task_delete.html", {"task": task})


def welcome(request):
    return render(request, 'welcome.html')

def signup(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomSignupForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomLoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("welcome")