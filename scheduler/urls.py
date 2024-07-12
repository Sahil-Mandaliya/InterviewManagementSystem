from django.urls import path

from scheduler.views.recruiter.scheduler import GetRecruiterScheduleView, UpdateRecruiterScheduleView
from scheduler.views.system.scheduler import GetSystemScheduleView, BookATimeSlot

urlpatterns = [
    path("recruiter/<int:recruiter_id>/update", UpdateRecruiterScheduleView.as_view()),
    path("recruiter/<int:recruiter_id>/get", GetRecruiterScheduleView.as_view()),
    path("get", GetSystemScheduleView.as_view()),
    path("create", BookATimeSlot.as_view())
]