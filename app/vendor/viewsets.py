from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Vendor
from .serializers import VendorSerializer, VendorPerformanceSerializer


class VendorViewset(ModelViewSet):
    queryset = Vendor.objects.order_by("-id")
    serializer_class = VendorSerializer

    @action(methods=["GET"], detail=True, serializer_class=VendorPerformanceSerializer)
    def performance(self, request, *args, **kwargs):
        obj = self.get_object()
        ser = self.get_serializer(obj, many=False)
        return Response(ser.data)
