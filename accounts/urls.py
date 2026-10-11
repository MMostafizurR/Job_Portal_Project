from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('create_profile/', create_profile, name='create_profile'),

    path('logout/', logout_view, name='logout'),
]