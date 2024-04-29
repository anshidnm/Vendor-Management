from rest_framework.viewsets import ModelViewSet

from .models import PurchaseOrder
from .serializers import OrderSerializer


class OrderViewset(ModelViewSet):
    queryset = PurchaseOrder.objects.filter(is_active=True)
    serializer_class = OrderSerializer
    # http_method_names = ["get", "post", "put", "delete"]
