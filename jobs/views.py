from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework import parsers
from .serializers import JobPostSerializer
from .models import JobPosts
from .permission import isSuperUser, IsOwner
from rest_framework import filters
from django.shortcuts import get_object_or_404
from users.models import FollingModel

# Create your views here.

class JobPostsView(generics.ListCreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = (permissions.IsAuthenticated, isSuperUser )
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)

    def get_queryset(self):
        print(self.request.user)
        return JobPosts.objects.filter(creator=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)
    
class JobPostByIDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobPostSerializer
    permission_classes = (permissions.IsAuthenticated, isSuperUser, IsOwner)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    lookup_field = 'id'
    queryset = JobPosts.objects.all()

class getAllJobsView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = JobPostSerializer
    queryset = JobPosts.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['^role', '=company']
    ordering_fields = ['id']
    # ordering = ['']


class FollowingJobPostsView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['role', 'company']
    ordering_fields = ['id']

    def get_queryset(self):
        followingUsers = FollingModel.objects.filter(follower = self.request.user).values('following')
        print("Follwing Users: ", followingUsers)
        return JobPosts.objects.filter(creator__in = followingUsers)
    

    



    

