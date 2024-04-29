from rest_framework import serializers

from .models import PurchaseOrder


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for managing purchase order operations
    """

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        read_only_fields = [
            "po_number",
            "order_date",
            "issue_date",
            "acknowledgment_date",
            "fulfillment_rate",
        ]
