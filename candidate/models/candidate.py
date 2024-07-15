from django.db import models
from main.models import TimeStampModel


class CandidateInfo(TimeStampModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, db_index=True, unique=True)
    email = models.CharField(max_length=100, db_index=True, unique=True)

    
class CandidateInvitations(TimeStampModel):
    candidate = models.ForeignKey(to=("candidate.CandidateInfo"), on_delete=models.RESTRICT)
    invitation_link = models.CharField(max_length=200, db_index=True, unique=True)
    