from socket import AddressFamily
from django.db import models
from datetime import datetime

from django.forms import CharField, EmailField, ImageField


class Register(models.Model):

    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    ProfilePicture=models.ImageField(upload_to="images")
    UserName=models.CharField(max_length=20)
    Email_ID=models.EmailField()
    Password=models.CharField(max_length=20)
    Confirm_password=models.CharField(max_length=20)
    Address=models.CharField(max_length=100)

    def __str__(self):
        return self.Username


# Create your models here.
