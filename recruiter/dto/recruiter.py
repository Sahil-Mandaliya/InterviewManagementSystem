from pydantic import BaseModel
from main.models import TimeStampModel, SoftDeleteModel


class RecruiterInfo(BaseModel):
    name: str
    phone: str
    email: str

    