from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns =[
    path("",views.index),
    path("process_money",views.process),
]