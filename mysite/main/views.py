# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CubeType, UserResults
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

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


def send_time(request):
    time = request.POST.get('time', None)
    cube = request.POST.get('cube', None)

    record = UserResults(time=time, cubetype=cube, user_id=request.user.id)
    record.save()
    return JsonResponse({'result':"ok"})

def view(response):
    return render(response, "main/view.html", {})

def delete_record(response, record_id):
    record = UserResults.objects.get(pk=record_id)
    record.delete()
    return redirect("view")

def view_competitions(request):
    html_page = requests.get(
        "https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=Poland&search=&state=present&year=all+years&from_date=&to_date=&delegate=&display=list").text
    soup = BeautifulSoup(html_page, 'html.parser')
    # comps = soup.find_all(class_='list-group-item not-past')
    comps = soup.select("li span a")
    return render(request, "main/competitions.html", {"comps":comps})
