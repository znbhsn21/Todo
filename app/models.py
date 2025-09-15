from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    due_date = models.DateField(null = True, blank = True)

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in-progress", "In-Progress"),
        ("completed", "Completed"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )