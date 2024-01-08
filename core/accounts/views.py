from django.shortcuts import render
from django.http import HttpResponse
import time
from .tasks import sendEmail


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<p>sended email</p>")
