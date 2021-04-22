from products.views import products
from django.contrib import admin
from marketing.models import Person, Product
# Register your models here.

admin.site.register(Product)
admin.site.register(Person)
