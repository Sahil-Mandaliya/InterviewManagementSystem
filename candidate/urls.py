from django.urls import path

from candidate.views.candidate import RegisterCandidateView

urlpatterns = [
    path("register",RegisterCandidateView.as_view())
]