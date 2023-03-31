from django.db import models
from django.contrib.auth.models import User




class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    adminId = models.IntegerField(default=None,unique=True)