from django.contrib import admin
from .recruiter_schedule import RecruiterSchedule
from .system_schedule import SystemSchedule


admin.register(RecruiterSchedule)
admin.register(SystemSchedule)