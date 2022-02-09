from django.contrib import admin

from app.models import User
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Contact)