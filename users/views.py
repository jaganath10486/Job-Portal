from django.shortcuts import render
from rest_framework import generics, permissions, response, status
from .serializers import UserSerializer, FollowingSerializer, UserProfileSerializer
from .models import User, FollingModel
# Create your views here.


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class FollwingView(generics.ListAPIView):
    serializer_class = FollowingSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        return FollingModel.objects.filter(follower = self.request.user)
    
class FollowView(generics.CreateAPIView):
    serializer_class = FollowingSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'
    queryset = User.objects.all()
    def perform_create(self, serializer):
        return serializer.save(follower = self.request.user, following = self.get_object())
    
class unFollowView(generics.DestroyAPIView):
    serializer_class = FollowingSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        followingPerson = FollingModel.objects.filter(follower = request.user, following = self.get_object())
        if(followingPerson):
            followingPerson.delete()
            return response.Response(data='Deleted Successfully ', status=status.HTTP_204_NO_CONTENT)
        return response.Response(data='No Id Found', status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_object(self):
        return self.request.user
    
    