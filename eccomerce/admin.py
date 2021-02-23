from django.contrib import admin
import eccomerce.models as eccom
# Register your models here.
admin.site.register(eccom.Customer)
admin.site.register(eccom.Product)
admin.site.register(eccom.Order)
admin.site.register(eccom.OrderItem)
admin.site.register(eccom.ShippingAddress)
#admin.site.register(app_model.Post)
