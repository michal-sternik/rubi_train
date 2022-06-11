# urls.py 
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', include('main.urls')), # main will be the name of your app
    path('', include('register.urls')), # main will be the name of your app
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]
