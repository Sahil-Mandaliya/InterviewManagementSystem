from django.db import models
from main.models import SoftDeleteModel, TimeStampModel

class SystemSchedule(TimeStampModel, SoftDeleteModel):
    recruiter = models.ForeignKey(to="recruiter.RecruiterInfo", db_index=True, on_delete=models.RESTRICT)
    candidate = models.ForeignKey(to="candidate.CandidateInfo", db_index=True, on_delete=models.RESTRICT)
    interview_date = models.DateField(db_index=True)
    interview_start_time = models.TimeField()
    interview_end_time = models.TimeField()
