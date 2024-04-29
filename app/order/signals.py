from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PurchaseOrder


@receiver(signal=post_save, sender=PurchaseOrder)
def generate_po_number(sender, instance, created, **kwargs):
    if created:
        instance.po_number = f"VND-PO-{str(instance.pk).zfill(6)}"
        instance.save()
