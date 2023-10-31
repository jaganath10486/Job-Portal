from typing import Any
from django.db import models

class AppliedModel(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        return super().create(**kwargs)