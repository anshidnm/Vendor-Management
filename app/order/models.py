from core.models import BaseModel
from django.db import models
from vendor.models import Vendor

from .enum import ORDER_STATUSES


class PurchaseOrder(BaseModel):
    """
    Model for storig purchase order details
    """

    po_number = models.CharField(max_length=100, blank=False, null=False, unique=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="purchase_orders"
    )
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField(default=dict)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=ORDER_STATUSES, default="pending")
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
