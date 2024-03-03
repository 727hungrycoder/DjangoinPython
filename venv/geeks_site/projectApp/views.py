from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    print("Entering index function")
    response = "Hello Geeks"
    print("Preparing response:", response)
    return HttpResponse(response)
