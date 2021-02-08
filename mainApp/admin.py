from django.contrib import admin
import mainApp.models as app_model

# Register your models here.
admin.site.register(app_model.Customer)
admin.site.register(app_model.Product)
admin.site.register(app_model.Order)
admin.site.register(app_model.OrderItem)
admin.site.register(app_model.ShippingAddress)
#admin.site.register(app_model.Post)


