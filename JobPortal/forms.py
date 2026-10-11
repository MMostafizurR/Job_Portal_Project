from django import forms
from JobPortal.models import Job

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'job_designation', 'description', 'skills_required', 'location', 'deadline']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'skills_required': forms.Textarea(attrs={'placeholder': 'List the skills required for this job.'}),
        }