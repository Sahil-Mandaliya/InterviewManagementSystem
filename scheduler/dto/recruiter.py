from pydantic import BaseModel
from typing import List
from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from scheduler.models.recruiter_schedule import RecruiterSchedule as RecruiterScheduleModel
from scheduler.dto.day import DaySchedule

class RecruiterSchedule(BaseModel):
    recruiter_id: int
    schedule: List[DaySchedule]

class RecruiterScheduleRequest(RecruiterSchedule):
    pass

class GetRecruiterScheduleResponse(RecruiterSchedule):
    pass


def convert_recruiter_schedule_dto_to_model(recruiter_schedule_dto: RecruiterSchedule):
    model_list = []
    recruiter_id = recruiter_schedule_dto.recruiter_id
    schedule_list = recruiter_schedule_dto.schedule

    for day_schedule in schedule_list:
        day = day_schedule.day
        time_slots =day_schedule.time_slots
        for time_slot in time_slots:
            start_time = time_slot.start_time
            end_time = time_slot.end_time    
            dt = datetime.combine(datetime.today(), end_time)
            dt = dt - relativedelta(minutes=1)
            end_time=dt.time()

            model_list.append(RecruiterScheduleModel(
                id=time_slot.slot_id,
                day=day,
                recruiter_id=recruiter_id,
                start_time=start_time,
                end_time=end_time,
                is_deleted=time_slot.is_deleted if time_slot.is_deleted else False ,
            ))
    
    return model_list
