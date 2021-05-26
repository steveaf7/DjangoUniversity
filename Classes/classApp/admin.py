from django.contrib import admin

# Register your models here.
from .models import DjangoClasses

# tells Django to look for the class I created.
admin.site.register(DjangoClasses)