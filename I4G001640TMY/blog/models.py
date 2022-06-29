from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

# Post


class blog(models.Model):
    Title = models.CharField(max_length=30)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
