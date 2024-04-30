from datetime import datetime
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .calcualtions import Calculation
from .models import PurchaseOrder
from .schema import Documentaion
from .serializers import OrderSerializer


@Documentaion.ORDER
class OrderViewset(ModelViewSet):
    queryset = PurchaseOrder.objects.select_related("vendor").order_by("-id")
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["vendor_id"]

    def update(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = self.get_object()
                res = super().update(request, *args, **kwargs)
                Calculation(obj, res.data).execute()
                return res
        except Exception as e:
            return Response({"error": str(e)})

    @action(methods=["PATCH"], detail=True)
    def acknowledge(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.acknowledgment_date:
            return Response(
                {"error": "Already acknowleged"}, status=status.HTTP_400_BAD_REQUEST
            )
        obj.acknowledgment_date = datetime.now()
        obj.save()
        Calculation(obj).calculate_response_time()
        return Response({"status": True})
