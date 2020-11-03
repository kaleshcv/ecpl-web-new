from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Quickcontact(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.IntegerField()
    country=models.CharField(max_length=200,null=True)
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

class Infographics(models.Model):
    title = models.CharField(max_length=300)
    image=models.ImageField(upload_to='static/resources/infographics-images')
    body=RichTextField(blank=True,null=True)




    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:200]+'...'



class Careers(models.Model):
    designation=models.CharField(max_length=200)
    project=models.CharField(max_length=200)
    job_location=models.CharField(max_length=200)
    work_timing=models.CharField(max_length=200)
    weekly_off=models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    emp_type=models.CharField(max_length=200)
    salary=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    skills=models.CharField(max_length=200)
    requirement=models.TextField()
    interview_type=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    others=models.CharField(max_length=200)
