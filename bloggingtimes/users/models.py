from django.db import models
import datetime

# Create your models here.
class userData(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    dateOfJoining = models.DateField(default=datetime.datetime.now)
    phone = models.IntegerField()