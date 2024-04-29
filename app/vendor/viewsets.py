from rest_framework.viewsets import ModelViewSet

from .models import Vendor
from .serializers import VendorSerializer


class VendorViewset(ModelViewSet):
    queryset = Vendor.objects.filter(is_active=True)
    serializer_class = VendorSerializer
    http_method_names = ["get", "post", "put", "delete"]
