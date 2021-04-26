from marketing.views import post_product
from products.views import products
from django.contrib import admin
from marketing.models import PostProduct
# Register your models here.

admin.site.register(PostProduct)
