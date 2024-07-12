from django.db import models
from main.models import TimeStampModel, SoftDeleteModel


class RecruiterInfo(TimeStampModel, SoftDeleteModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, db_index=True, unique=True)
    email = models.CharField(max_length=100, db_index=True, unique=True)

    