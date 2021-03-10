from django.contrib import admin
from blog.models import BlogPost, Author, News

# Register your models here.
admin.site.register(Author)
@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'date_created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_field = {'slug':('title',)}
    raw_id_field = ('author')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_date', 'news_status')
    list_filter = ('news_status', 'date_created', 'publish_date', 'author')
    search_fields = ('title', 'body')
    prepopulated_field = {'slug':('title',)}
    raw_id_field = ('author')
    date_hierarchy = 'publish_date'
    ordering = ('news_status', 'publish_date')

