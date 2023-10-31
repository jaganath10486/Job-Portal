from rest_framework import serializers
from .models import AppliedCandidates


class AppliedCandidatesSerializer(serializers.ModelSerializer):
    job_company = serializers.ReadOnlyField(source="job.company")
    candidate_email = serializers.ReadOnlyField(source="candidate.email")

    class Meta:
        model = AppliedCandidates
        fields = ['job_company', 'candidate_email', 'mobile_number', 'name', 'resume', 'year', 'id']
        extra_kwargs = {
            'id' : {'read_only' : True}
        }

        