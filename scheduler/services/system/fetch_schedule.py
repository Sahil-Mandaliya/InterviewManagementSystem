
from datetime import date, time
from typing import List
from dateutil.relativedelta import relativedelta
from main.utils.date import weekday_from_date
from recruiter.services.fetch import fetch_all_recruiter_schedule_for_a_day
from scheduler.dto.day import DaySchedule, TimeSlot
from scheduler.models.system_schedule import SystemSchedule


MAX_MINUTES = 1445
DAY_START_TIME = 60 * 9
DAY_END_TIME = 60 * 21

def get_all_booked_slots_for_a_date(curr_date):
    booked_slots = SystemSchedule.objects.filter(interview_date=curr_date)
    return booked_slots

def convert_time_to_int(t:time):
    h = t.hour
    m = t.minute
    return h*60+m

def convert_int_to_time(time_num):
    h=time_num//60
    m=time_num%60
    return time(h,m,0)


def get_available_slots_from_schedules(available_schedule: List[TimeSlot], booked_schedule: List[TimeSlot]):
    available_time = [0 for _ in range(MAX_MINUTES)]

    for schedule in available_schedule:
        start_time = convert_time_to_int(schedule.start_time)
        end_time = convert_time_to_int(schedule.end_time)
        available_time[start_time]+=1
        available_time[end_time+1]-=1
    
    for i in range(MAX_MINUTES):
        if i<=DAY_START_TIME:
            continue
        if i>DAY_END_TIME:
            continue

        available_time[i]=available_time[i]+available_time[i-1]

    for slot in booked_schedule:
        start_time = convert_time_to_int(slot.start_time)
        end_time = convert_time_to_int(slot.end_time)
        for i in range(start_time, end_time+1,1):
            available_time[i]=-10

        # available_time[start_time]-=1000000
        # available_time[end_time+1]+=1000000
    
    for i in range(MAX_MINUTES):
        available_time[i]=min(1,max(available_time[i],0))
    
    available_slots = []
    start = 0
    end = 1440
    f=0
    for i in range(MAX_MINUTES):
        if f==0 and available_time[i]==1:
            f=1
            start=i
        elif f==1 and available_time[i]==0:
            end=i-1
            f=0            
            available_slots.append(TimeSlot(start_time=convert_int_to_time(start), end_time=convert_int_to_time(end)))

    return available_slots
    
def get_available_slots_for_a_date(curr_date: date):
    weekday_name = weekday_from_date(curr_date)
    schedules_for_a_day = fetch_all_recruiter_schedule_for_a_day(weekday_name)
    slots_for_a_day = []
    for slot in schedules_for_a_day:
        slots_for_a_day.append(TimeSlot(
                start_time = slot.start_time,
                end_time = slot.end_time,
            )
        )

    booked_system_slots = get_all_booked_slots_for_a_date(curr_date) 
    booked_slots = []
    for slot in booked_system_slots:
        booked_slots.append(TimeSlot(
                slot_id = slot.id,
                start_time = slot.interview_start_time,
                end_time = slot.interview_end_time,
            )
        )

    return get_available_slots_from_schedules(slots_for_a_day, booked_slots)
    # available_time = [0 for _ in range(MAX_MINUTES)]
    # for schedule in schedules_for_a_day:
    #     start_time = convert_time_to_int(schedule.start_time)
    #     end_time = convert_time_to_int(schedule.end_time)
    #     available_time[start_time]+=1
    #     available_time[end_time+1]-=1
    
    # for i in range(MAX_MINUTES):
    #     if i==0:
    #         continue

    #     available_time[i]=available_time[i]+available_time[i-1]

    # booked_slots = get_all_booked_slots_for_a_date(curr_date) 
    # for slot in booked_slots:
    #     start_time = convert_time_to_int(slot.start_time)
    #     end_time = convert_time_to_int(slot.end_time)
    #     available_time[start_time]-=1000000
    #     available_time[end_time]-=1000000
    
    # for i in range(MAX_MINUTES):
    #     available_time[i]=min(1,max(available_time[i],0))
    
    # available_slots = []
    # start = 0
    # end = 1440
    # f=0
    # for i in range(MAX_MINUTES):
    #     if f==0 and available_time[i]==1:
    #         f=1
    #         start=i
    #     elif f==1 and available_time[i]==0:
    #         end=i-1
    #         f=0            
    #         available_slots.append(TimeSlot(start_time=convert_int_to_time(start), end_time=convert_int_to_time(end)))
    
    # return available_slots



def get_available_slots_for_a_date_for_a_recruiter(curr_date: date, recruiter_id):
    weekday_name = weekday_from_date(curr_date)
    schedules_for_a_day = fetch_all_recruiter_schedule_for_a_day(weekday_name)
    available_time = [0 for _ in range(MAX_MINUTES)]
    for schedule in schedules_for_a_day:
        start_time = convert_time_to_int(schedule.start_time)
        end_time = convert_time_to_int(schedule.end_time)
        available_time[start_time]+=1
        available_time[end_time+1]-=1
    
    for i in range(MAX_MINUTES):
        if i==0:
            continue

        available_time[i]=available_time[i]+available_time[i-1]

    booked_slots = get_all_booked_slots_for_a_date(curr_date) 
    for slot in booked_slots:
        start_time = convert_time_to_int(slot.start_time)
        end_time = convert_time_to_int(slot.end_time)
        available_time[start_time]-=1000000
        available_time[end_time]-=1000000
    
    for i in range(MAX_MINUTES):
        available_time[i]=min(1,max(available_time[i],0))
    
    available_slots = []
    start = 0
    end = 1440
    f=0
    for i in range(MAX_MINUTES):
        if f==0 and available_time[i]==1:
            f=1
            start=i
        elif f==1 and available_time[i]==0:
            end=i-1
            f=0            
            available_slots.append(TimeSlot(start_time=convert_int_to_time(start), end_time=convert_int_to_time(end)))
    
    return available_slots

def get_recruiter_id_to_recruiter_schedule_map(schedules):
    id_to_slots_map = dict()
    for s in schedules:
        if s.recruiter_id not in id_to_slots_map:
            id_to_slots_map[s.recruiter_id] = []
        
        id_to_slots_map[s.recruiter_id].append(TimeSlot(start_time=s.start_time, end_time=s.end_time))
            
    return id_to_slots_map

def get_recruiter_id_to_system_schedule_map(schedules):
    id_to_slots_map = dict()
    for s in schedules:
        if s.recruiter_id not in id_to_slots_map:
            id_to_slots_map[s.recruiter_id] = []
        
        id_to_slots_map[s.recruiter_id].append(TimeSlot(start_time=s.interview_start_time, end_time=s.interview_end_time))
            
    return id_to_slots_map


def get_available_interviewer(interview_date: date, interview_start_time: time, interview_end_time: time):
    weekday_name = weekday_from_date(interview_date)
    schedules_for_a_day = fetch_all_recruiter_schedule_for_a_day(weekday_name)
    booked_slots = get_all_booked_slots_for_a_date(interview_date)

    schedule_mapping = get_recruiter_id_to_recruiter_schedule_map(schedules_for_a_day)
    booked_mapping = get_recruiter_id_to_system_schedule_map(booked_slots)

    for recruiter_id, available_schedule in schedule_mapping.items():
        booked_slot = booked_mapping[recruiter_id] if recruiter_id in booked_mapping else []
        is_slot_available = False

        available_slots = get_available_slots_from_schedules(available_schedule, booked_slot)
        for available_slot in available_slots:
            if interview_start_time >=available_slot.start_time and interview_end_time <= available_slot.end_time:
                is_slot_available = True
                break

        if is_slot_available:
            return recruiter_id
    
    return None


def get_available_schedule(curr_date:date = date.today(), nums_of_days:int=15):
    schedules = []
    for i in range(nums_of_days):
        curr_date=curr_date+relativedelta(days=1)
        schedules.append(DaySchedule(
            date=curr_date,
            day = weekday_from_date(curr_date),
            time_slots=get_available_slots_for_a_date(curr_date))
        )

    return schedules