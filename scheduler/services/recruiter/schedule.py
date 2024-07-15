

from typing import List
from scheduler.dto.recruiter import RecruiterScheduleRequest, convert_recruiter_schedule_dto_to_model
from scheduler.models.recruiter_schedule import RecruiterSchedule


def day_to_time_map_from_model_list(schedule: List[RecruiterSchedule]):
    mapping = dict()
    for s in schedule:
        if s.day not in mapping:
            mapping[s.day] = []

        mapping[s.day].append(tuple(s.start_time, s.end_time))
    
    return mapping

def day_to_time_map_from_model_list(schedule: List[RecruiterSchedule]):
    mapping = dict()
    for s in schedule:
        if s.day not in mapping:
            mapping[s.day] = []

        mapping[s.day].append(tuple(s.start_time, s.end_time))
    
    return mapping
    

def filter_schedules(new_schedule):
    # new_schedule_map = day_to_time_map_from_model_list(new_schedule)
    # existing_schedule_map = day_to_time_map_from_model_list(existing_schedule)
    new_slots = []
    updated_slots = []
    deleted_slots = []
    for schedule in new_schedule:
        if not schedule.id or schedule.id ==0 :
            new_slots.append(schedule)
            continue
    
        if schedule.id > 0 and schedule.is_deleted == False:
            updated_slots.append(schedule)
            continue

        if schedule.id > 0 and schedule.is_deleted == True:
            deleted_slots.append(schedule)

    return new_slots, updated_slots, deleted_slots


def create_or_update_schedule(recruiter_id, schedule_request: RecruiterScheduleRequest):
    # recruiter_id= schedule_request.recruiter_id
    
    new_schedule = convert_recruiter_schedule_dto_to_model(schedule_request)
    # existing_schedule =  RecruiterSchedule.objects.filter(recruiter_id=recruiter_id)

    new_slots, updated_slots, deleted_slots = filter_schedules(new_schedule)
    for new_slot in new_slots:
        RecruiterSchedule.objects.create(recruiter_id=recruiter_id, day=new_slot.day, start_time=new_slot.start_time, end_time=new_slot.end_time)
    
    for updated_slot in updated_slots:
        RecruiterSchedule.objects.filter(id=updated_slot.id).update(start_time=updated_slot.start_time, end_time=updated_slot.end_time)
    
    deleted_ids = []
    for deleted_slot in deleted_slots:
        deleted_ids.append(deleted_slot.id)
    
    if len(deleted_ids):
        RecruiterSchedule.objects.filter(id__in=deleted_ids).update(is_deleted=True)

    
   





