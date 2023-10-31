from typing import Any
from django.db import models
from django.db.models.query import QuerySet

class JobsManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()
    
    def create(self, **kwargs: Any) -> Any:
        print("Job Manager : ", kwargs)
        return super().create(**kwargs)