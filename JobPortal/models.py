from django.db import models
from accounts.models import User


# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    job_designation = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.TextField()
    location = models.CharField(max_length=100)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    date_posted = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    date_applied = models.DateTimeField(auto_now_add=True)