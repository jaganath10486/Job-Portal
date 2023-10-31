from django.db import models
from .manager  import JobsManager
from django.conf import settings, Settings
from django.contrib.auth import get_user_model

MODEL = get_user_model()

# Create your models here.
class JobPosts(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=200)
    expiry_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200)
    creator = models.ForeignKey(settings.MODEL, on_delete=models.CASCADE)
    
    objects = JobsManager()
    REQUIRED_FIELDS = ['company', 'role']




