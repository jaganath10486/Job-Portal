from django.db import models
from .manager import AppliedModel
from jobs.models import JobPosts
from django.conf import settings

def custom_file_name(instance, filename):
            extension = filename.split('.')[-1]
            print(extension)
            new_file_name = f"{instance.pk}-{instance.name}.{extension}"
            return f"resume/{new_file_name}"

class AppliedCandidates(models.Model):
    
    mobile_number = models.CharField(max_length=20, blank=False)
    job = models.ForeignKey(JobPosts, on_delete=models.CASCADE)
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    year = models.IntegerField()
    name = models.CharField(max_length=255)
    resume = models.FileField(upload_to=custom_file_name)

    objects = AppliedModel()
    REQUIRED_FIELDS =['name', 'mobile_number']
    









