from django.contrib import admin
from .models import User, Location, Area, Crag, Route, Style, Grade
# Register your models here.

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Area)
admin.site.register(Crag)
admin.site.register(Route)
admin.site.register(Style)
admin.site.register(Grade)
