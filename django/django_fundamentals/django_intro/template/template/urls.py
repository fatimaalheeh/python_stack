from django.urls import path,include

urlpatterns = [
    path('', include("template_app.urls")),
]
