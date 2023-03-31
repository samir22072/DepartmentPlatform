from django.db import models
from django.contrib.auth.models import User

class deptChoices(models.IntegerChoices):
    CE = 1,'CE'
    IT = 2,'IT'
    ENTC = 3,'ENTC'


class Faculty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    department = models.IntegerField(default=None,choices=deptChoices.choices)
    facultyId = models.IntegerField(default=None,unique=True)


