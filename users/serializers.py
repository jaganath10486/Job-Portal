from rest_framework import serializers
from django.conf import settings
from .models import User, FollingModel
from django.contrib.auth.hashers import make_password



class FollowingSerializer(serializers.ModelSerializer):
    folower_email = serializers.ReadOnlyField(source='follower.email')
    class Meta:
        model = FollingModel
        fields = ['folower_email', 'id']
        extra_kwargs = {
            'id' : {'read_only' : True}
        }

    
class FollowerSeriliazer(serializers.ModelSerializer):
    folowing_email = serializers.ReadOnlyField(source='following.email')
    class Meta:
        model = FollingModel
        fields = ['folowing_email', 'id']
        extra_kwargs = {
            'id' : {'read_only' : True}
        }


class UserProfileSerializer(serializers.ModelSerializer):
    follower = FollowingSerializer(many=True)
    following = FollowerSeriliazer(many=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'gender', 'age', 'is_superuser', 'id', 'following', 'follower']
        extra_kwargs = {
            'password' : {'write_only':True},
            'id' : {"read_only" : True},
            'follower' : {"read_only" : True},
            'following' : {"read_only" : True}
        } 
    def validate(self, attrs):
        if(User.objects.filter(email = attrs.get('emaail')).exists()):
            print("Already Exists")
            raise serializers.ValidationError({'email' : 'already exists'})
        return super().validate(attrs)
    
    def validate_password(self, value: str) -> str:
       return make_password(value)
    

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
    



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password', 'gender', 'age', 'is_superuser', 'id']
        extra_kwargs = {
            'password' : {'write_only':True},
            'id' : {"read_only" : True}
        } 

    def validate(self, attrs):
        if(User.objects.filter(email = attrs.get('emaail')).exists()):
            print("Already Exists")
            raise serializers.ValidationError({'email' : 'already exists'})
        return super().validate(attrs)
    
    def validate_password(self, value: str) -> str:
       return make_password(value)
    

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
    









    
    