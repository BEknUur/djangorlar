# Python modules
from typing import Any

# from datetime import datetime, timezone

# Django modules
from django.db.models import Model, DateTimeField,Manager
from django.utils import timezone as django_timezone


class SoftDeleteManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)



class AbstractBaseModel(Model):
    """
    Abstract base model with common fields.
    """
    created_at=DateTimeField(auto_now_add=True)
    updated_at=DateTimeField(auto_now=True)
    deleted_at=DateTimeField(null=True,blank=True)

    objects=SoftDeleteManager()
    all_objects=Manager()
    

    class Meta:
        """Meta class for AbstractBaseModel."""

        abstract = True

    def delete(self, *args: tuple[Any, ...], **kwargs: dict[Any, Any]) -> None:
        """Soft delete the object by setting deleted_at timestamp."""

      
        self.deleted_at = django_timezone.now()
        self.save(update_fields=["deleted_at"])

