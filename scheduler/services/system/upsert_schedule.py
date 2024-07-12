


from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta
from main.utils.db_models import db_model_to_pydantic
from recruiter.dto.recruiter import RecruiterInfo
from recruiter.models.recruiter import RecruiterInfo as RecruiterInfoModel
from recruiter.services.fetch import fetch_all_recruiter_schedule_for_a_day
from scheduler.dto.day import TimeSlot
from scheduler.dto.schedule import ScheduleInterviewRequest, ScheduleInterviewResponse, ScheduleInterviewResponseData
from scheduler.models.system_schedule import SystemSchedule
from scheduler.services.recruiter.fetch_schedule import get_recruiter_schedule_for_a_day
from scheduler.services.system.fetch_schedule import get_available_interviewer


def schedule_an_interview(data:ScheduleInterviewRequest):
    candidate_id = data.candidate_id
    interview_date = data.date
    start_time = data.start_time
    end_time = data.end_time

    dt = datetime.combine(datetime.today(), end_time)
    dt = dt - relativedelta(minutes=1)
    end_time=dt.time()

    return book_schedule(candidate_id, interview_date, start_time, end_time)

def book_schedule(candidate_id, interview_date, start_time, end_time):
    available_interviewer_id = get_available_interviewer(interview_date, start_time, end_time)
    if not available_interviewer_id:
        res = ScheduleInterviewResponse(
            message = "There is no interviwer available for your selected time slot, Kindly please select different time slot",
            success=False
        )
        return res

    obj = SystemSchedule.objects.create(
        recruiter_id=available_interviewer_id,
        candidate_id=candidate_id,
        interview_date=interview_date,
        interview_start_time=start_time,
        interview_end_time=end_time
    )
    
    recruiter = RecruiterInfoModel.objects.get(id=obj.recruiter_id)
    
    res = ScheduleInterviewResponse(
        message = "Your interview is scheduled successfully, You will receive an invite shortly for the same",
        success = True,
        data = ScheduleInterviewResponseData(
            recruiter=db_model_to_pydantic(recruiter, RecruiterInfo),
            interview_date = obj.interview_date, 
            interview_start_time = obj.interview_start_time, 
            interview_end_time = obj.interview_end_time
        )
    )
    return res
