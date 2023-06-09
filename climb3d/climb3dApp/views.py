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
        "selectedLocation": "Select Location",
        "selectedArea": "Select Area"
    })
    
def indexLocation(request):
    if request.method == "POST":
        location = int(request.POST['location'])
        selectedLocation = Location.objects.filter(id=location)
        for location in selectedLocation:
            selected = location.location
        locations = Location.objects.all()
        areas = Area.objects.filter(location=location)
        crags = []
        for area in areas:
            crag = Crag.objects.filter(area=area)
            crags.append(crag)
        return render(request, "climb3d/index.html",{
            "locations": locations,
            "areas": areas,
            "crags": crags,
            "selectedLocation": selected,
            "selectedArea": "Select Area"
        })
    
    else:
        return HttpResponseRedirect(reverse("index"))
    
def indexArea(request):
    if request.method == "POST":
        area = request.POST['area']
        locations = Location.objects.all()
        selectedArea = Area.objects.filter(id=area)
        for area in selectedArea:
            selected = area.area
            selectedLocation = area.location.location
        crags = Crag.objects.filter(area=area)
        areas= Area.objects.all()
        return render(request, "climb3d/index.html",{
            "locations": locations,
            "areas": areas,
            "crags": crags,
            "selectedLocation": selectedLocation,
            "selectedArea": selected
        })
    else:
        return HttpResponseRedirect(reverse("index"))
    
def crag(request):
    if request.method == "POST":
        selectedCrag = request.POST['crag']
        cragData = Crag.objects.filter(id=selectedCrag)
        for crag in cragData:
            crag = crag.crag
            area = crag.area.area
            location = crag.area.location.location

        return render(request,"climb3d/crag.html",{
            "crag": crag,
            "area": area,
            "location": location
        })
    
    
    else:
        return HttpResponseRedirect(reverse("index"))


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
    
