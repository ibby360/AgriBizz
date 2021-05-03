from django.contrib import admin
from products.models import Product
# Register your models here.

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'publish', 'status')
    list_filter = ('status', 'date_created', 'publish',)
    search_fields = ('product_name', '')
    prepopulated_field = {'slug':('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')