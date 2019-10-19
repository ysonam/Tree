from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class userdata(models.Model):
    data = models.CharField(max_length=100)
   