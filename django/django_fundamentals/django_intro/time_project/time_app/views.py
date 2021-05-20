from django import http
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from time import gmtime, strftime
    
def time(request):
    context = {
        "time": strftime("%Y-%m-%d", gmtime()),
        "date": strftime("%H:%M %p", gmtime())
        }
    return render(request,'index.html', context)
