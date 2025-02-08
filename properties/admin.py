from django.contrib import admin
from properties import *
from .models import Property , PropertyImage
admin.site.register(Property)
admin.site.register(PropertyImage)