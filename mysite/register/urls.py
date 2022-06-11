from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as v

urlpatterns = [
    # path('', views.home, name='index'),
    path('register/', v.register, name='register'),
]