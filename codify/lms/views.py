from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import *


def hello(request):
    return HttpResponse("Привет это работа views+urls")


def time(request):
    time_now = datetime.now()
    return HttpResponse(time_now)


def info_student(request):
    student = Student.objects.all()
    return render(request,
                  'index.html',
                  {"student": student})


def mentor_info(request):
    mentor = Mentor.objects.all()
    return render(request,
                  'mentor.html',
                  {"mentor": mentor})



