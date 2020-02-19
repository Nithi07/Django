from django.db import models

# Create your models here.

class Edata(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    dob = models.DateField()