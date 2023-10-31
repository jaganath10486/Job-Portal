from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

from .managers import CustomUserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=255, blank=True )
    last_name = models.CharField(max_length=255, blank=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other') ], default='O', max_length=1)
    age = models.IntegerField(default=10)


    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

class FollingModel(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    created_at = models.DateField(auto_now=True)



    