from main.utils.db_models import model_to_json
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.utils.pydantic import convert_json_to_pydantic
from candidate.dto.register import RegisterCandidateRequest
from candidate.services.register import register_candidate


class RegisterCandidateView(GenericAPIView):
    def post(self, request):
        data = request.data
        request_data = convert_json_to_pydantic(data, RegisterCandidateRequest)
        new_candidate =  register_candidate(request_data)
        res = model_to_json(new_candidate)
        return Response(status=200, data=res)
