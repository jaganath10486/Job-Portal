from django.urls import path
from .views import JobPostsView, JobPostByIDView, getAllJobsView, FollowingJobPostsView

urlpatterns = [
    path('all-jobs/', getAllJobsView.as_view(), name='Get List of all Avilable Jobs'),
    path('following-jobs/', FollowingJobPostsView.as_view(), name='User Follwing Job Posts'),
    path('jobposts/',JobPostsView.as_view(), name='Employee Job Post List View' ),
    path('jobposts/<int:id>/', JobPostByIDView.as_view(), name='Employee Job Posts by Job ID' )
]