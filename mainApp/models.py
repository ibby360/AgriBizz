from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    