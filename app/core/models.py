from django.db import models


class BaseModel(models.Model):
    """
    The Base model class for all other models
    to inherit including created and updated timestamp
    with active or not
    """

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
