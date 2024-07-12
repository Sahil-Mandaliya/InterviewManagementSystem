from main.utils.db_models import model_list_to_json
from main.utils.pydantic import convert_json_to_pydantic, pydantic_to_json
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from scheduler.dto.recruiter import RecruiterScheduleRequest
from scheduler.services.recruiter.fetch_schedule import get_recruiter_schedule_by_id
from scheduler.services.recruiter.schedule import create_or_update_schedule


class GetRecruiterScheduleView(GenericAPIView):
    def get(self, request, recruiter_id):
        schedule  = get_recruiter_schedule_by_id(recruiter_id)
        schedule = pydantic_to_json(schedule)
        return Response(data={"schedule":schedule})


class UpdateRecruiterScheduleView(GenericAPIView):
    def post(self, request, recruiter_id):
        data=request.data

        request_data = convert_json_to_pydantic(data, RecruiterScheduleRequest)
        create_or_update_schedule(recruiter_id, request_data)
        return Response(data={"message":"Update Successfully"}, status=200)