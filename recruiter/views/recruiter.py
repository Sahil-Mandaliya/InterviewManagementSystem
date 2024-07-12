from main.utils.db_models import model_to_json
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.utils.pydantic import convert_json_to_pydantic
from recruiter.dto.register import RegisterRecruiterRequest
from recruiter.services.register import register_recruiter


class RegisterRecruiterView(GenericAPIView):
    def post(self, request):
        data = request.data
        request_data = convert_json_to_pydantic(data, RegisterRecruiterRequest)
        new_recruiter =  register_recruiter(request_data)
        res = model_to_json(new_recruiter)
        return Response(status=200, data=res)
