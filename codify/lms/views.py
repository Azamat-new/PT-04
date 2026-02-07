from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("Привет это работа views+urls")


def time(request):
    time_now = datetime.now()
    return HttpResponse(time_now)

