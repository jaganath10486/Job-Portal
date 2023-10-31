from django.shortcuts import render
from rest_framework import generics
from .serializers import AppliedCandidatesSerializer
from rest_framework import permissions
from rest_framework import parsers
from .models import AppliedCandidates
from jobs.models import JobPosts

from django.shortcuts import get_object_or_404
from .permissions import ISOwner, isSuperUser

class AppliedCandidatesView(generics.CreateAPIView):
    serializer_class = AppliedCandidatesSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    permission_classes  = (permissions.IsAuthenticated, isSuperUser )
    
    def perform_create(self, serializer):
        obj = get_object_or_404(JobPosts, pk=self.kwargs["pk"])
        print(obj)
        return serializer.save(candidate = self.request.user, job = obj)
    
class AppliedJobsViews(generics.ListAPIView):
    serializer_class=AppliedCandidatesSerializer
    permission_classes = (permissions.IsAuthenticated, isSuperUser)
    def get_queryset(self):
        return AppliedCandidates.objects.filter(candidate = self.request.user)
    
class AppliedJobById(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppliedCandidatesSerializer
    permission_classes = (permissions.IsAuthenticated, ISOwner  )
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    queryset = AppliedCandidates.objects.all()
    lookup_field = 'id'


class AppliedCandidatesByJob(generics.ListAPIView):
    serializer_class = AppliedCandidatesSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'
    def get_queryset(self):
        jobpost = get_object_or_404(JobPosts, pk=self.kwargs['id'])
        print("Job Posts : ", jobpost)
        return AppliedCandidates.objects.filter(job = jobpost)

    
