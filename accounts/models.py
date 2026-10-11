from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('recruter', 'Recruiter'),
        ('job_seeker', 'Job Seeker'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    display_name = models.CharField(max_length=100, blank=True, null=True)

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
