# urls.py 
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', include('main.urls')),
    path('', include('register.urls')), # link urlpatterns from register app urls
    path('', include("django.contrib.auth.urls")),  #needed for login
    path('admin/', admin.site.urls),
]
