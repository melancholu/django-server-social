from django.db import models

from apps.core.models import UUIDModel


class User(UUIDModel):
    name = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "user"
        ordering = ["-created"]
