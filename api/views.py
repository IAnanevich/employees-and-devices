from company.models import Employees, Device, Delivery
from api.serializers import DeviceSerializer, DeliverySerializer, EmployeesSerializer
from rest_framework import viewsets


# Create your views here.
class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()
