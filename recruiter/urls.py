from django.urls import path

from recruiter.views.recruiter import RegisterRecruiterView

urlpatterns = [
    path("register",RegisterRecruiterView.as_view())
]