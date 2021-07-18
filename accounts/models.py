from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class Customer(models.Model):
# 	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
# 	name = models.CharField(max_length=200, default='', blank=True)
# 	phone = models.CharField(max_length=200, default='', blank=True)
# 	email = models.CharField(max_length=200, default='', blank=False, null=False)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

# 	def __str__(self):
# 		return self.name
