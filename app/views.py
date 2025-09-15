from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Task
from .forms import TaskForm, CustomLoginForm, CustomSignupForm

def welcome(request):
    return render(request, 'welcome.html')

def home(request, task_id=None, action=None):
    # Handle Add / Update
    if request.method == "POST":
        if task_id:  # updating a task
            task = get_object_or_404(Task, id=task_id)
            form = TaskForm(request.POST, instance=task)
        else:  # adding a new task
            form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()

    # If editing
    edit_task = None
    if action == "edit" and task_id:
        edit_task = get_object_or_404(Task, id=task_id)
        form = TaskForm(instance=edit_task)

    # If deleting
    if action == "delete" and task_id:
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect("home")

    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "home.html", {
        "tasks": tasks,
        "form": form,
        "edit_task": edit_task
    })

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

def logout(request):
    logout(request)
    return redirect("welcome")