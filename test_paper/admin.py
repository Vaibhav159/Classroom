from django.contrib import admin
from .models import Question, Module

# Register your models here.
admin.site.register([Question, Module])
