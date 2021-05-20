from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,'index.html')
def get_res(request):
    context={
            "name" : request.POST['name'],
            "location" : request.POST['location'],
            "language":request.POST['language'],
            "comment":request.POST['comment'],

    }

    return render(request,'result.html',context)