from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    image = models.CharField(max_length=1000, blank=True, default="https://www.shutterstock.com/image-vector/default-avatar-profile-trendy-style-260nw-1759726295.jpg")
