from django.urls import path,include

urlpatterns = [
    path('', include("greater_number_app.urls")),
]
