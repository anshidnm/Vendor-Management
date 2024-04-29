from datetime import datetime, timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from .calcualtions import Calculation
from .models import PurchaseOrder


@receiver(signal=post_save, sender=PurchaseOrder)
def generate_po_number(sender, instance, created, **kwargs):
    if created:
        instance.po_number = f"VND-PO-{str(instance.pk).zfill(6)}"
        instance.save()
        Calculation(instance).calculate_fulfillment_rate()


@receiver(signal=post_save, sender=PurchaseOrder)
def update_completed_time(sender, instance, created, **kwargs):
    if instance.status == "completed" and not instance.completed_date:
        instance.completed_date = datetime.now()
        instance.save()
