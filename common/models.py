from django.db import models
from uuid import uuid4
from common import helper


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, max_length=255, default = helper.generate_id)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True