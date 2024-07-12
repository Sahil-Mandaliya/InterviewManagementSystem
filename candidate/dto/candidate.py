from pydantic import BaseModel
from main.models import TimeStampModel, SoftDeleteModel


class CandidateInfo(BaseModel):
    name: str
    phone: str
    email: str

    