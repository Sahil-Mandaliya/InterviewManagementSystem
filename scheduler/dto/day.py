from pydantic import BaseModel
from typing import List, Optional
from datetime import time,date

class TimeSlot(BaseModel):
    slot_id: Optional[int]
    start_time: Optional[time]
    end_time: Optional[time]
    is_deleted: Optional[bool]

class DaySchedule(BaseModel):
    date: Optional[date]
    day: str
    time_slots: List[TimeSlot]