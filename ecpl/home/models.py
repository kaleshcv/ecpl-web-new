from django.db import models

# Create your models here.

class Quickcontact(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.IntegerField()
    country=models.CharField(max_length=200)
    requirement=models.TextField()


