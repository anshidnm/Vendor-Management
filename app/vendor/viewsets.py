from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Vendor, PerformanceHistory
from .schema import Documentaion
from .serializers import (
    VendorSerializer,
    VendorPerformanceSerializer,
    VendorPerformanceHistorySerializer,
)


@Documentaion.VENDOR
class VendorViewset(ModelViewSet):
    queryset = Vendor.objects.order_by("-id")
    serializer_class = VendorSerializer

    @action(methods=["GET"], detail=True, serializer_class=VendorPerformanceSerializer)
    def performance(self, request, *args, **kwargs):
        obj = self.get_object()
        ser = self.get_serializer(obj, many=False)
        return Response(ser.data)


@Documentaion.HISTORY
class VendorHistoryViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = PerformanceHistory.objects.order_by("-id")
    serializer_class = VendorPerformanceHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "date": ["exact", "date__gte", "date__lte", "date__range", "gte", "lte"]
    }

    def get_queryset(self):
        vendor = Vendor.objects.get(id=self.kwargs["vendor_id"])
        queryset = self.queryset.filter(vendor=vendor)
        return queryset

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
