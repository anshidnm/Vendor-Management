from rest_framework import serializers

from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """
    Serializer for managing vendor operations
    """

    class Meta:
        model = Vendor
        fields = "__all__"
        read_only_fields = [
            "is_active",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
