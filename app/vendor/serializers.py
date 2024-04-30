from rest_framework import serializers

from .models import Vendor, PerformanceHistory


class VendorSerializer(serializers.ModelSerializer):
    """
    Serializer for managing vendor operations
    """

    class Meta:
        model = Vendor
        fields = "__all__"
        read_only_fields = [
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class VendorPerformanceSerializer(serializers.ModelSerializer):
    """
    Serializer for listing vendor performance
    """

    class Meta:
        model = Vendor
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class VendorPerformanceHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for listing vendor performance history
    """

    class Meta:
        model = PerformanceHistory
        fields = [
            "date",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
