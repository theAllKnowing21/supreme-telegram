from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(requrest):
    return HttpResponse("G'day, this is the BSIT-4B Activity 2 of Pietro Vicente")