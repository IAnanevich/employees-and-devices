from django.test import TestCase

from company.models import Employees, Device,Delivery
from api.serializers import EmployeesSerializer, DeliverySerializer, DeviceSerializer


class EmployeesSerializerTest(TestCase):
    def setUp(self):
        self.employees_attributes = {
            "first_name": "Ivan",
            "last_name": "Ananevich",
            "email": "ivanshahter71@gmail.com",
        }

        self.serializer_data = {
            "first_name": "Alex",
            "last_name": "Varkalov",
            "email": "alexvarkalov@gmail.com",
        }

        self.employees = Employees.objects.create(**self.employees_attributes)
        self.serializer = EmployeesSerializer(instance=self.employees, context={'request': None})

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"first_name", "last_name", "photo", "email", "id", "url", "register_date"})

    def test_firstname_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["first_name"], self.employees_attributes["first_name"])

    def test_lastname_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["last_name"], self.employees_attributes["last_name"])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["email"], self.employees_attributes["email"])


class DeviceSerializerTest(TestCase):
    def setUp(self):
        self.device_attributes = {
            "device_type": "laptop",
            "device_name": "Dell",
            "device_model": "Vostro 15",
            "price": 1000,
        }

        self.serializer_data = {
            "device_type": "laptop",
            "device_name": "Asus",
            "device_model": "Vivobook 15",
            "price": 1200,
        }

        self.device = Device.objects.create(**self.device_attributes)
        self.serializer = DeviceSerializer(instance=self.device, context={'request': None})

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"device_item", "device_type", "device_name", "device_model", "production_date", "price", "device_photo"})

    def test_device_type_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["device_type"], self.device_attributes["device_type"])

    def test_device_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["device_name"], self.device_attributes["device_name"])

    def test_device_model_content(self):
        data = self.serializer.data
        self.assertEqual(data["device_model"], self.device_attributes["device_model"])

    def test_price_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["price"], self.device_attributes["price"])
