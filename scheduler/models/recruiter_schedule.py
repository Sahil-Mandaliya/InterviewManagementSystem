from django.db import models
from main.models import SoftDeleteModel, TimeStampModel
from scheduler.models.types import DayChoices


class RecruiterSchedule(TimeStampModel, SoftDeleteModel):
    recruiter = models.ForeignKey(to=("recruiter.RecruiterInfo"), on_delete=models.RESTRICT)
    day = models.CharField(choices=DayChoices.choices, max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()