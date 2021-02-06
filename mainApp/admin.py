from django.contrib import admin
import mainApp.models as app_model

# Register your models here.
admin.site.register(app_model.Customer)
admin.site.register(app_model.Product)
admin.site.register(app_model.Order)
admin.site.register(app_model.OrderItem)
admin.site.register(app_model.ShippingAddress)
#admin.site.register(app_model.Post)

@admin.register(app_model.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_field = {'slug':('title',)}
    raw_id_field = ('author')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

