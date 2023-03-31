from django.db import models
from django.contrib.auth.models import User
from Faculty.models import Faculty

class deptChoices(models.IntegerChoices):
    CE = 1,'CE'
    IT = 2,'IT'
    ENTC = 3,'ENTC'


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    department = models.IntegerField(default=None,choices=deptChoices.choices)
    rollNo = models.IntegerField(default=None,unique=True)
    domain = models.CharField(max_length=100,default=None)
    mentor = models.ForeignKey(Faculty,null=False)

