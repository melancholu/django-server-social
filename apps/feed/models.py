from django.db import models

from apps.core.models import UUIDModel


class Feed(UUIDModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "feed"
        ordering = ["-created"]
