

from candidate.models.candidate import CandidateInfo


def register_candidate(candidate_data: CandidateInfo):
    return CandidateInfo.objects.create(name=candidate_data.name, email=candidate_data.email, phone=candidate_data.phone)
    