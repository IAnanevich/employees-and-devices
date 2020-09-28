from django.contrib import admin
from .models import Employees, Device, Delivery


# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'register_date')


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'device_name', 'device_model', 'device_item', 'production_date', 'price')


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'device', 'delivery_date')


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Delivery, DeliveryAdmin)
