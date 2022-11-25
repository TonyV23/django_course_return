from django.http import HttpRequest
from django.shortcuts import render


def index(request):
    return render(
        request,
        'app/home/index.html'
    )