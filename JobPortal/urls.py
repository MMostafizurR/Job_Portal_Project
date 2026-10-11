from django.urls import path
from JobPortal.views import *

urlpatterns = [
    path('', job_list_view, name='job_list'),
    path('post_job/', post_job_view, name='post_job'),
    path('apply_job/<int:job_id>/', apply_job_view, name='apply_job'),
]