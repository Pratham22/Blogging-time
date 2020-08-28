from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    designation = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField()
    email = models.URLField(max_length=250)
    twitter = models.URLField(max_length=250)
    facebook = models.URLField(max_length=250)
    instagram = models.URLField(max_length=250)
    skype = models.URLField(max_length=250)
    linkedin = models.URLField(max_length=250)    
