from django.shortcuts import render,redirect
from .models import Dojos,Ninja

def index(request):
    context = {
        'dojos' : Dojos.objects.all(),
        'ninja' : Ninja.objects.all(),
    }
    return render(request,"index.html",context)
