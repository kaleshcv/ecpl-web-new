from django.db import models

# Create your models here.

class Quickcontact(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.IntegerField()
    country=models.CharField(max_length=200)
    requirement=models.TextField()

class MainContact(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.IntegerField(null=True)
    country=models.CharField(max_length=200,null=True)
    company=models.CharField(max_length=200,null=True)
    service1=models.CharField(max_length=200,null=True)
    service2 = models.CharField(max_length=200,null=True)
    service3 = models.CharField(max_length=200,null=True)
    service4 = models.CharField(max_length=200,null=True)
    service5 = models.CharField(max_length=200,null=True)
    service6 = models.CharField(max_length=200,null=True)
    service7 = models.CharField(max_length=200,null=True)
    service8 = models.CharField(max_length=200,null=True)
    service9 = models.CharField(max_length=200,null=True)
    service10 = models.CharField(max_length=200,null=True)
    service11= models.CharField(max_length=200,null=True)
    service12 = models.CharField(max_length=200,null=True)
    description=models.TextField()
    attachment=models.FileField(upload_to='static/contactform/attachments',null=True)

