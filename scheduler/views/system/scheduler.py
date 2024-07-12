from datetime import date
from main.utils.pydantic import convert_json_to_pydantic, pydantic_list_to_json, pydantic_to_json
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from scheduler.dto.schedule import ScheduleInterviewRequest
from scheduler.services.system.fetch_schedule import get_available_schedule
from scheduler.services.system.upsert_schedule import schedule_an_interview


class GetSystemScheduleView(GenericAPIView):
    def get(self, request):
        schedule = get_available_schedule()
        res_schedule = pydantic_list_to_json(schedule)
        return Response(data={"message":"Fetched Successfully", "schedule":res_schedule}, status=200)
    
class BookATimeSlot(GenericAPIView):
    def post(self, request):
        request_data = request.data
        data = convert_json_to_pydantic(request_data,ScheduleInterviewRequest)
        res = schedule_an_interview(data)
        json_res = pydantic_to_json(res)
        return Response(data={"message":"Your interview has been successfully scheduled", "details":json_res}, status=200)

       