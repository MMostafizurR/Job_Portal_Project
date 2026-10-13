from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from JobPortal.models import Job, JobApplication
from JobPortal.forms import JobPostForm


# Create your views here.
@login_required
def job_list_view(request):
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(
            Q(title__icontains=query) |
            Q(job_designation__icontains=query) |
            Q(description__icontains=query) |
            Q(skills_required__icontains=query) |
            Q(location__icontains=query)
        )
    else:
        jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query})


@login_required
def post_job_view(request):
    if request.user.user_type != 'recruiter':
        return redirect('job_list')  # Redirect non-recruiters to the job list
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect('job_list')  # Redirect to the job list after posting
    else:
        form = JobPostForm()
    return render(request, 'jobs/post_job.html', {'form': form})


@login_required
def apply_job_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.user.user_type != 'job_seeker':
        return redirect('job_list')  # Redirect non-job seekers to the job list

    job = get_object_or_404(Job, id=job_id)
    # Check if the user has already applied for this job
    already_applied = JobApplication.objects.filter(job=job, job_seeker=request.user).exists()
    if not already_applied:
        JobApplication.objects.create(job=job, job_seeker=request.user)

    return redirect('job_list')  # Redirect to the job list after applying
