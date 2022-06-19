from django.db import models
from django.contrib.auth import get_user_model

# Post

class blog(models.Model):
  Title = models.CharField(max_length=30)
  Text = models.TextField()
  Author = get_user_model()
  Created_date = models.DateTimeField()
  Published_date = models.DateTimeField()
