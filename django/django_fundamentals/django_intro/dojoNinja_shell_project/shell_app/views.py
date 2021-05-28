from django import http
from django.shortcuts import render, HttpResponse,redirect

def index(request):
    return HttpResponse(request,"hi")
