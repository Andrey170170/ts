from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import views
from . import views
from django.shortcuts import render
from django.conf.urls import include, url





urlpatterns = [
    path('', views.home_page, name='home_page'),
    
    path('signup/', views.signup_view, name='signup'),
    path('user_page/', views.user_page, name='user_page')
    
    
   
    
]