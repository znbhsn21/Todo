from django.db import models

# Create your models here.

class Task(models.Model):
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