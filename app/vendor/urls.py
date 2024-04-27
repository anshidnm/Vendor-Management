from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import VendorViewset


router = DefaultRouter()

router.register("", VendorViewset, "vendor")


urlpatterns = [path("", include(router.urls))]
