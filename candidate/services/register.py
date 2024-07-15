

from candidate.models.candidate import CandidateInfo


def register_candidate(candidate_data: CandidateInfo):
    return CandidateInfo.objects.create(name=candidate_data.name, email=candidate_data.email, phone=candidate_data.phone)
    

def invite_candidate(candidate_data: CandidateInfo):
    candidate_data = register_candidate(candidate_data)
    invitation_link = generate_invitation_link(candidate_data)
    return candidate_data, invitation_link

def generate_invitation_link(candidate_data: CandidateInfo):
    return "google.com"