from datetime import datetime
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .calcualtions import Calculation
from .models import PurchaseOrder
from .serializers import OrderSerializer


class OrderViewset(ModelViewSet):
    queryset = PurchaseOrder.objects.select_related("vendor").order_by("-id")
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = self.get_object()
                res = super().update(request, *args, **kwargs)
                Calculation(obj, res.data).execute()
                return res
        except Exception as e:
            return Response({"error": str(e)})

    @action(methods=["PATCH"], detail=True, serializer_class=None)
    def acknowledge(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.acknowledgment_date:
            obj.acknowledgment_date = datetime.now()
            obj.save()
        Calculation(obj).calculate_response_time()
        return Response({"status": True})
