from django.db import models


# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(null=True, blank=True)
    email = models.EmailField()
    register_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Device(models.Model):
    device_item = models.AutoField(primary_key=True)
    device_type = models.CharField(max_length=30)
    device_name = models.CharField(max_length=30)
    device_model = models.CharField(max_length=256)
    production_date = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    device_photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.device_name


class Delivery(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.PROTECT)
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
    comment = models.TextField(null=True, blank=True)
    delivery_date = models.DateField(auto_now=True)
