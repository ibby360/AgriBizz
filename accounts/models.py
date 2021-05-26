from django.db import models
from django.contrib.auth.models import User

from marketing.models import PostProduct

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
	name = models.CharField(max_length=200, default='', blank=True)
	phone = models.CharField(max_length=200, default='', blank=True)
	email = models.CharField(max_length=200, default='', blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, blank=True)
	product = models.ForeignKey(PostProduct, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	order_status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name
