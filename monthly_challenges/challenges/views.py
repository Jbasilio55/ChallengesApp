from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("New Years Resolution, Start working out and get that body on point.")

def february(request):
    return HttpResponse("Work on algorithms and become a pro!!")
