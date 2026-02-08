from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('time/', views.time, name='time'),
    path('student/', views.info_student, name='student'),
    path('mentor/', views.mentor_info, name='mentor'),


]

