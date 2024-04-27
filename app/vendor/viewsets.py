from rest_framework.viewsets import ModelViewSet

from .models import Vendor
from .serializers import VendorSerializer


class VendorViewset(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
