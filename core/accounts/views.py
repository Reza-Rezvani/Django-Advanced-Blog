from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import time
from .tasks import sendEmail
import requests


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<p>sended email</p>")


@cache_page(60)
def test(request):
    response = requests.get(
        "https://bcd67f90-2d41-4a98-94a0-c44e477dfd56.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())
