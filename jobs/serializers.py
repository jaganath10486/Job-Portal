from rest_framework import serializers
from .models import JobPosts
from django.conf import settings

class UserSerializer():
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['email', 'gender', 'age', 'is_superuser']

class JobPostSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source="creator.email")
    is_superuser = serializers.ReadOnlyField(source="creator.is_superuser")
    class Meta:
        model = JobPosts
        fields = ['email', 'creator', 'category', 'expiry_date', 'image', 'description', 'location', 'role', 'company', 'is_superuser', 'id']
        extra_kwargs = {
            "creator" : {"read_only" : True},
            "id" : {"read_only" : True}
        }
