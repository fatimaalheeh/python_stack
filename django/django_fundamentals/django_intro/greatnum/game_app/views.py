from django import http
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
import random
def index(request):
    if "auto_guess" not in request.session:
        request.session['auto_guess'] = random.randint(1,100)
        
    return render(request,"index.html")

def process(request):
    
    guess_n=request.POST['guess']
    if guess_n != "":
        if int(guess_n)>request.session['auto_guess']:
            request.session["result"]="Too high!"
            request.session["color"]="red"
        elif int(guess_n)==request.session['auto_guess']:
            request.session["result"]=guess_n + "was the number!"
            request.session["color"]="green"
        else:
            request.session["result"]=" Too low!"
            request.session["color"]="red"
    else:
        return redirect("/")
    return redirect("/")

def restart(request):
    request.session.clear()
    return redirect("/")
    