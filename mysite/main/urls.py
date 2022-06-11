# urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('', views.home, name='index'),
    path('<int:id>', views.index, name='index'),
    path('home/', views.home, name='home'),

    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('timer/', views.timer, name='base'),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)