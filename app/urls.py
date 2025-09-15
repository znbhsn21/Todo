from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
    path("task/add/", views.task_add, name="task_add"),
    path("task/<int:task_id>/edit/", views.task_edit, name="task_edit"),
    path("task/<int:task_id>/delete/", views.task_delete, name="task_delete"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
]
