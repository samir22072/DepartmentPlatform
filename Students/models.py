from django.db import models
from django.contrib.auth.models import User
from Faculty.models import Faculty


class deptChoices(models.IntegerChoices):
    CE = 1, 'CE'
    IT = 2, 'IT'
    ENTC = 3, 'ENTC'


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    department = models.IntegerField(default=None, choices=deptChoices.choices)
    rollNo = models.IntegerField(default=None, unique=True)
    batch = models.CharField(max_length=2, default=None)


class StudentInformation(models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, primary_key=True)
    division = models.CharField(max_length=2, default=None)
    phone = models.CharField(max_length=12, default=None)
    email = models.EmailField(unique=True, default=None)
    dob = models.DateTimeField(default=None)
    bloodGroup = models.CharField(max_length=3, default=None)
    permanentAddress = models.TextField(default=None)
    localAddress = models.TextField(default=None)

    fatherName = models.CharField(default=None, max_length=100)
    foccupation = models.CharField(default=None, max_length=100)
    fphone = models.CharField(default=None, max_length=12)
    femail = models.EmailField(default=None)

    motherName = models.CharField(default=None, max_length=100)
    moccupation = models.CharField(default=None, max_length=100)
    mphone = models.CharField(default=None, max_length=12)
    memail = models.EmailField(default=None)

    tenPercent = models.FloatField(default=None)
    twelvePercent = models.FloatField(default=None)

    feS1 = models.FloatField(default=None)
    feS2 = models.FloatField(default=None)
    seS1 = models.FloatField(default=None)
    seS2 = models.FloatField(default=None)
    teS1 = models.FloatField(default=None)
    teS2 = models.FloatField(default=None)
    beS1 = models.FloatField(default=None)
    beS2 = models.FloatField(default=None)

    achievements = models.TextField(default=None)
    extraCurricular = models.TextField(default=None)
