from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.http import JsonResponse


from .models import User
from .models import Location
from .models import Area
from .models import Crag
from .models import Route
from .models import Style
from .models import Grade

# Create your views here.

def index(request):
    locations = Location.objects.all()
    areas = Area.objects.all()
    crags = Crag.objects.all()
    return render(request, "climb3d/index.html",{
        "locations": locations,
        "areas": areas,
        "crags": crags,
    })
    
def indexLocation(request):
    if request.method == "POST":
        location = request.POST['location']
        areas = Area.objects.filter(location=location)
        crags = []
        for area in areas:
            crag = Crag.objects.filter(area=area)
            crags.append(crag)
        return render(request, "climb3d/index.html",{
            "locations": location,
            "areas": areas,
            "crags": crags,
        })
    
def indexArea(request):
    area = request.POST['area']
    locations = Location.objects.all()
    crags = Crag.objects.filter(area=area)
    return render(request, "climb3d/index.html",{
        "locations": locations,
        "areas": area,
        "crags": crags,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "climb3d/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "climb3d/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "climb3d/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "climb3d/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "climb3d/register.html")
