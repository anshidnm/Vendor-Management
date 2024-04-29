from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import OrderViewset


router = DefaultRouter()

router.register("", OrderViewset, "order")


urlpatterns = [path("", include(router.urls))]
