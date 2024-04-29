from core.utils import none_to_zero
from django.db.models import Q, Sum, Count, F, ExpressionWrapper, FloatField
from django.db.models.functions import Extract

from .models import PurchaseOrder


class Calculation:
    """
    Utility class for calculate vendor perfomance
    metrics according purchase order updates
    """

    def __init__(self, order: PurchaseOrder, updated_data=None):
        self._order = order
        self._data = updated_data
        self._vendor = order.vendor

    def _is_status_updated(self):
        return self._order.status != self._data["status"]

    def _is_quality_provided(self):
        return self._order.quality_rating != self._data["quality_rating"]

    def get_aggregated_data(self):
        rating_data = PurchaseOrder.objects.filter(vendor=self._vendor).aggregate(
            on_time_count=Count(
                "id",
                filter=Q(delivery_date__gte=F("completed_date"), status="completed"),
            ),
            total_quality_rating=Sum("quality_rating", filter=Q(status="completed")),
            total_completed_po=Count("id", filter=Q(status="completed")),
            total_po=Count("*"),
        )
        return rating_data

    def calculate_on_time_delivery(self):
        rating_data = self.get_aggregated_data()
        average_rating = (
            none_to_zero(rating_data["on_time_count"])
            / none_to_zero(rating_data["total_completed_po"])
            if rating_data["total_completed_po"]
            else 0
        )
        self._vendor.on_time_delivery_rate = average_rating
        self._vendor.save()

    def calculate_quality_rating(self):
        rating_data = self.get_aggregated_data()
        average_rating = (
            none_to_zero(rating_data["total_quality_rating"])
            / none_to_zero(rating_data["total_completed_po"])
            if rating_data["total_completed_po"]
            else 0
        )
        self._vendor.quality_rating_avg = average_rating
        self._vendor.save()

    def calculate_fulfillment_rate(self):
        rating_data = self.get_aggregated_data()
        average_rating = (
            none_to_zero(rating_data["total_completed_po"])
            / none_to_zero(rating_data["total_po"])
            if rating_data["total_po"]
            else 0
        )
        self._vendor.fulfillment_rate = average_rating
        self._vendor.save()

    def calculate_response_time(self):
        data = (
            PurchaseOrder.objects.filter(
                vendor=self._vendor, acknowledgment_date__isnull=False
            )
            .annotate(
                response_time=ExpressionWrapper(
                    Extract("acknowledgment_date", "epoch")
                    - Extract("issue_date", "epoch"),
                    output_field=FloatField(),
                )
            )
            .aggregate(total_seconds=Sum("response_time"), total_po=Count("*"))
        )
        average_time = (
            none_to_zero(data["total_seconds"]) / none_to_zero(data["total_po"])
            if data["total_po"]
            else 0
        )
        average_minutes = average_time / 60
        self._vendor.average_response_time = average_minutes
        self._vendor.save()

    def execute(self):
        if self._is_status_updated() and self._data["status"] == "completed":
            self.calculate_on_time_delivery()
            self.calculate_fulfillment_rate()
        if self._is_quality_provided():
            self.calculate_quality_rating()
