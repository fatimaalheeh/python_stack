from django import http
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
    
def index(request):
    return render(request, 'index.html')

    
def submitted_info(request):
    context={
            'name' : request.POST['name'],
            'location' : request.POST['location'],
            'language':request.POST['language'],
            'comment':request.POST['comment'],
    }
    print('context')
    return render(request,'result.html', context)
