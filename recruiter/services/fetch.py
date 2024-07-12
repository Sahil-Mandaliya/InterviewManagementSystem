


from scheduler.models.recruiter_schedule import RecruiterSchedule


def fetch_all_recruiter_schedule_for_a_day(day:str):
    return RecruiterSchedule.objects.filter(day=day)

    