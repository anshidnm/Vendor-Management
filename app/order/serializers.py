from rest_framework import serializers

from .models import PurchaseOrder


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for managing purchase order operations
    """

    def validate_quality_rating(self, value):
        if value > 5 or value < 1:
            raise serializers.ValidationError("Rating should be in between 1 and 5")

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        read_only_fields = [
            "is_active",
            "po_number",
            "order_date",
            "issue_date",
            "acknowledgment_date",
            "fulfillment_rate",
            "completed_date",
        ]
