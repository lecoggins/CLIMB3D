from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    image = models.CharField(max_length=1000, blank=True, default="https://www.shutterstock.com/image-vector/default-avatar-profile-trendy-style-260nw-1759726295.jpg")
    savedCrags = models.ManyToManyField("Crag", blank=True, related_name="saved_crags")
    savedRoutes = models.ManyToManyField("Route", blank=True, related_name="saved_routes")

class Location(models.Model):
    location = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{ self.id}: {self.location}"
    
class Area( models.Model):
    location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="area_location")
    area = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{ self.id}: {self.area}"

class Crag( models.Model):
    area = models.ForeignKey("Area", on_delete=models.CASCADE, related_name="crag_location")
    crag = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{ self.id}: {self.crag}"
    
class Style(models.Model):
    style = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{ self.id}: {self.style}"
    
class Grade(models.Model):
    grade = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.id}: {self.grade}"

class Route(models.Model):
    crag = models.ForeignKey("Crag", on_delete=models.CASCADE, related_name="route_location")
    route = models.CharField(max_length=200, blank=False)
    grade = models.ForeignKey("Grade", blank=True, on_delete=models.PROTECT, related_name="route_grade")
    style = models.ForeignKey("Style", on_delete=models.PROTECT, related_name="route_style")


    def __str__(self):
        return f"{ self.id}: {self.route}"
    