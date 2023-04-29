from django.db import models

# Create your models here.

class Charities(models.Model):
    name =models.CharField(max_length=200, unique=True)
    email=models.EmailField(max_length=100, unique=True)
    password=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    certificates=models.CharField(max_length=200)
    confirmed = models.BooleanField()
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    full_description = models.TextField(null=True, blank=True)

class User(models.Model):
    email=models.EmailField(max_length=100, unique=True)
    password=models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    liked_charities = models.ManyToManyField(Charities, blank=True)
    