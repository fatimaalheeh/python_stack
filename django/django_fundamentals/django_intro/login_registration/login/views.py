from django.shortcuts import render,HttpResponse,redirect
from . import models
def index(request):
    return render(request, "index.html")
def login(request):
    if request.method =="POST":
        if request.POST["login_type"]=="login":
            if models.check_user(request.POST["name"],request.POST["password"]):
                request.session["user_name"]=request.POST["name"]
                return render(request,"welcome.html")
                
            else:
                return redirect("/login")
        if request.POST["login_type"]=="registration":
            models.register(request.POST["name"],request.POST["password"])
    return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')