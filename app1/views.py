from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def app_response(request):
    return HttpResponse("<h1><marquee>This is app1 http response</marquee></h1>")