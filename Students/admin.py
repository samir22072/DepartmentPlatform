from django.contrib import admin

# Register your models here.
from .models import Student,StudentInformation

admin.site.register(Student)
admin.site.register(StudentInformation)