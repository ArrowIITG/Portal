from django.contrib import admin

# Register your models here.

from .models import About , Student

admin.site.register(About)

admin.site.register(Student)
