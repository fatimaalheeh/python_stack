import random

from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def randmethod(request):
    if "guess" not in request.session:
        request.session['guess'] = random.randint(1,100)
    return render(request,"index.html")
