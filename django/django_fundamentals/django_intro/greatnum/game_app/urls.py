from django.urls import path    
from django.conf.urls import url 
from . import views
urlpatterns = [
    path('',views.index),
     path('process',views.process),
     path('restart',views.restart),

]
