from django.urls.conf import path,   include

urlpatterns = [
    path('',include('mycounter_app.urls')),
]
