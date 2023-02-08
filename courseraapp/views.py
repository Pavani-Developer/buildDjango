from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the pavani first website")

def ref(request):
    return HttpResponse("This page is for reference!")