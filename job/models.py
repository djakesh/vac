from PIL.Image import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(AbstractUser):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    image = models.ImageField(upload_to='companies', default='company.png')




