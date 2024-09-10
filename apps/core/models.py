from django.db import models

from django_extensions.db.fields import ShortUUIDField


class UUIDModel(models.Model):
    uuid = ShortUUIDField(db_index=True, editable=False, unique=True)

    class Meta:
        abstract = True
