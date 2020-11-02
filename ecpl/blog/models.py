from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=300)
    image=models.ImageField(upload_to='static/resources/blog-images')
    body=RichTextField(blank=True,null=True)

    date = models.DateTimeField()


    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:200]+'...'
