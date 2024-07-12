from typing import Optional
from pydantic import BaseModel
from datetime import date, time

from recruiter.dto.recruiter import RecruiterInfo

class ScheduleDto(BaseModel):
    recruiter_id: Optional[int]
    candidate_id: int
    date: date
    start_time: time
    end_time: time

class ScheduleInterviewRequest(ScheduleDto):
    pass

class ScheduleInterviewResponseData(BaseModel):
    recruiter: RecruiterInfo
    interview_date: date
    interview_start_time: time
    interview_end_time: time


class ScheduleInterviewResponse(BaseModel):
    message:str
    success: bool
    data: Optional[ScheduleInterviewResponseData]

        

class ReScheduleInterviewRequest(ScheduleDto):
    schedule_id: int