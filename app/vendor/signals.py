from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Vendor


@receiver(signal=post_save, sender=Vendor)
def generate_vender_code(sender, instance, created, **kwargs):
    if created:
        instance.vendor_code = f"VND-MGT-{str(instance.pk).zfill(6)}"
        instance.save()
