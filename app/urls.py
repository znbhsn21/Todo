from django.urls import path
from .views import home, welcome, signup, login_view, logout, profile

urlpatterns = [
    path('', welcome, name = 'welcome'),
    path("home/", home, name="home"),
    path("home/<int:task_id>/<str:action>/", home, name="task_action"), 
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout, name="logout"), 
    path("profile/", profile, name="profile"),
]