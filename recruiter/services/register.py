

from recruiter.models.recruiter import RecruiterInfo


def register_recruiter(recruiter_data: RecruiterInfo):
    return RecruiterInfo.objects.create(name=recruiter_data.name, email=recruiter_data.email, phone=recruiter_data.phone)
    