# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import CubeType, Record


# Create your views here.

def index(response, id):
    return HttpResponse(id)


def home(response):
    return render(response, "main/home.html", {})

def base(response):
    return render(response, "main/base.html", {})

def timer(response):
    cube_types = CubeType.objects.all()
    return render(response, "main/timer.html", {"cube_types":cube_types})
