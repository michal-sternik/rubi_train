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
    path('send_time/', views.send_time, name='send_time'),
    path("view/", views.view, name="view"),
    path("view_competitions/", views.view_competitions, name="view_competitions"),
    path("delete_record/<record_id>",views.delete_record, name="delete_record"),
    path("algorithms/",views.display_algs, name="display_algs")
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)