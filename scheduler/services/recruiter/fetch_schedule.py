from main.utils.constants import WEEK_DAYS
from scheduler.dto.day import DaySchedule, TimeSlot
from scheduler.dto.recruiter import GetRecruiterScheduleResponse
from scheduler.models.recruiter_schedule import RecruiterSchedule

def get_recruiter_schedule_for_a_day(day):
    return RecruiterSchedule.objects.filter(day=day)

def get_recruiter_schedule_by_id_from_db(recruiter_id):
    return RecruiterSchedule.objects.filter(recruiter_id=recruiter_id)

def day_wise_time_slots_for_recruiter(schedule):
    day_wise_time_slots = dict()
    for day in WEEK_DAYS:
        day_wise_time_slots[day] = []

    for s in schedule:
        day_wise_time_slots[s.day].append(s)

    return day_wise_time_slots

def get_recruiter_schedule_by_id(recruiter_id):
    schedule = get_recruiter_schedule_by_id_from_db(recruiter_id)
    day_wise_time_slots  = day_wise_time_slots_for_recruiter(schedule)
    schedule_slots = []
    for key, time_slots in day_wise_time_slots.items():
        time_slots_dto = []
        for slot in time_slots:
            time_slots_dto.append(
                TimeSlot(
                    slot_id=slot.id,
                    start_time=slot.start_time,
                    end_time=slot.end_time
                )
            )

        schedule_slots.append(DaySchedule(
            day=key,
            time_slots=time_slots_dto
        ))

    response  = GetRecruiterScheduleResponse(
        recruiter_id=recruiter_id,
        schedule=schedule_slots
    )
    return response

