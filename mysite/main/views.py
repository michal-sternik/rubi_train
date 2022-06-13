# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CubeType, UserResults
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup


# homepage
def home(response):
    return render(response, "main/home.html", {})

# base page with navbar and footer to extend from
def base(response):
    return render(response, "main/base.html", {})

# timer page
def timer(response):
    cube_types = CubeType.objects.all()
    return render(response, "main/timer.html", {"cube_types":cube_types})

# view to receive data from timer and push it to database
def send_time(request):
    time = request.POST.get('time', None)
    cube = request.POST.get('cube', None)

    record = UserResults(time=time, cubetype=cube, user_id=request.user.id)
    record.save()
    return JsonResponse({'result':"ok"})

# site to view times from specified user
def view(response):
    return render(response, "main/view.html", {})

# view to handle delete button near every record on /view/ page
def delete_record(response, record_id):
    record = UserResults.objects.get(pk=record_id)
    record.delete()
    return redirect("view")

# site with listed competitions that are planned, using beautifulsoup
def view_competitions(request):
    html_page = requests.get(
        "https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=Poland&search=&state=present&year=all+years&from_date=&to_date=&delegate=&display=list").text
    soup = BeautifulSoup(html_page, 'html.parser')
    # comps = soup.find_all(class_='list-group-item not-past')
    comps = soup.find_all('div', class_="competition-link")
    dates = soup.find_all('span', class_="date")
    compsToPass = []

    for comp, date in zip(comps, dates):
        compsToPass.append((comp.a.text, "https://www.worldcubeassociation.org/"+str(comp.a).split('"')[1], date.text))
        # print(date.text)
    # print(compsToPass[0][1])
    for comp in compsToPass:
        print(comp[0])
    return render(request, "main/competitions.html", {"comps":compsToPass})

# site to display pdf documents with tutorials/algorithms
def display_algs(response):
    return render(response, "main/algorithms.html", {})
