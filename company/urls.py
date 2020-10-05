from django.conf.urls import url
from django.urls import include, path
from api.views import EmployeesViewSet, DeviceViewSet, DeliveryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r"employees", EmployeesViewSet)
router.register(r"devices", DeviceViewSet)
router.register(r"deliveries", DeliveryViewSet)

urlpatterns = router.urls
