from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import VendorViewset, VendorHistoryViewset


router = DefaultRouter()

router.register("", VendorViewset, "vendor")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "<int:vendor_id>/performance-history/",
        VendorHistoryViewset.as_view({"get": "list"}),
    ),
]
