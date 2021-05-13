from django.contrib import admin
from crops.models import Crops
# Register your models here.

@admin.register(Crops)
class PostAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'slug', 'publish', 'status')
    list_filter = ('status', 'date_created', 'publish',)
    search_fields = ('crop_name', '')
    prepopulated_field = {'slug':('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')