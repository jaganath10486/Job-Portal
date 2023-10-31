from django.urls import path
from .views import AppliedCandidatesView, AppliedJobsViews, AppliedJobById, AppliedCandidatesByJob

urlpatterns = [
    path('apply-job/<int:pk>', AppliedCandidatesView.as_view(), name='Apply Jobs'),
    path('applied-jobs', AppliedJobsViews.as_view(), name='List of Applied Jobs'),
    path('applied-job/<int:id>', AppliedJobById.as_view(), name='Applied Job By Id'),
    path('applied-candidates/<int:id>/', AppliedCandidatesByJob.as_view(), name='Applied Candidates For the Job Posts')
]
