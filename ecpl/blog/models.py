from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300)
    image=models.ImageField(upload_to='static/resources/blog-images')
    body=models.TextField()
    head1=models.CharField(max_length=200,blank=True)
    para1=models.TextField(blank=True)
    image1 = models.ImageField(upload_to='static/resources/blog-images',blank=True)
    head2 = models.CharField(max_length=200,blank=True)
    para2=models.TextField(blank=True)
    image2 = models.ImageField(upload_to='static/resources/blog-images', blank=True)
    head3 = models.CharField(max_length=200,blank=True)
    para3=models.TextField(blank=True)
    image3 = models.ImageField(upload_to='static/resources/blog-images', blank=True)
    head4 = models.CharField(max_length=200,blank=True)
    para4 = models.TextField(blank=True)
    image4 = models.ImageField(upload_to='static/resources/blog-images', blank=True)
    head5 = models.CharField(max_length=200,blank=True)
    para5 = models.TextField(blank=True)
    image5 = models.ImageField(upload_to='static/resources/blog-images', blank=True)

    date = models.DateTimeField()


    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:200]+'...'
