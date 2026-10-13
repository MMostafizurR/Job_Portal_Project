from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from accounts.forms import UserRegistrationForm, RecruiterProfileForm, JobSeekerProfileForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            login(request, user)

            return redirect('create_profile')  # Redirect to a success page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def create_profile(request):
    user = request.user
    if user.user_type == 'recruter':
        if request.method == 'POST':
            form = RecruiterProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('job_list')  # Redirect to a success page after profile creation
        else:
            form = RecruiterProfileForm()
    elif user.user_type == 'job_seeker':
        if request.method == 'POST':
            form = JobSeekerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('job_list')  # Redirect to a success page after profile creation
        else:
            form = JobSeekerProfileForm()
    else:
        form = JobSeekerProfileForm()  # Default to JobSeekerProfileForm if user_type is not set

    return render(request, 'accounts/create_profile.html', {'form': form})   


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
