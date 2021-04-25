from django.db import models
from django.db.models.fields.files import ImageField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Person(models.Model):
    # Region choices
    CHOICES = (
        ('Arusha', 'Arusha'),
        ('Dar es Salaam', 'Dar es Salaam'),
        ('Geita', 'Geita'),
        ('Kagera', 'Kagera'),
        ('Mwanza', 'Mwanza'),
        ('Morogoro', 'Morogoro'),
        ('Shinyanga', 'Shinyanga'),
        ('Tabora', 'Tabora'),
        ('Singida', 'Singida'),
        ('Simiyu', 'Simiyu'),
        ('Mbeya', 'Mbeya'),
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, )
    phone_number = PhoneNumberField(null=False, blank=False)
    region = models.CharField(max_length=50, choices=CHOICES) 
    district = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=150)
    price = models.FloatField(max_length=100, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add = True)
    thumbnail = ImageField(upload_to='static/img/', null=True, blank=True)

    def __str__(self):
        return self.product_name
