from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    motive = models.TextField(null=True)
    dob = models.DateField(null = True)
    age = models.IntegerField(null=True)
    website = models.URLField(null=True, max_length=250)
    degree = models.CharField(max_length=50, null=True)
    freelance = models.BooleanField(default=False)
    about = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    designation = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)
    email = models.URLField(max_length=250,null=True)
    twitter = models.URLField(max_length=250, null=True)
    facebook = models.URLField(max_length=250, null=True)
    instagram = models.URLField(max_length=250, null=True)
    skype = models.URLField(max_length=250, null=True)
    linkedin = models.URLField(max_length=250, null=True)    
