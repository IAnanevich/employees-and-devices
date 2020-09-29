from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from company.models import Employees, Device, Delivery


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ("id", "first_name", "last_name", "email", "register_date", "photo")


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = (
            "device_item",
            "device_type",
            "device_name",
            "device_model",
            "production_date",
            "price",
            "device_photo",
        )


class DeliverySerializer(ModelSerializer):
    employee = serializers.SlugRelatedField(
        slug_field="last_name", queryset=Employees.objects.all()
    )
    device = serializers.SlugRelatedField(
        slug_field="device_name", queryset=Device.objects.all()
    )

    class Meta:
        model = Delivery
        fields = ("id", "employee", "device", "delivery_date", "comment")
