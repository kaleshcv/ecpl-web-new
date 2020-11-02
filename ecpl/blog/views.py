from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog(request):

    blogs = Blog.objects.all().order_by('date').reverse()
    return render(request, 'blog-home.html', {'blogs': blogs})

def blogdetails(request,pk):

    blogdetails=Blog.objects.get(pk=pk)
    return render(request,'blogdetails.html',{'blogdetails':blogdetails})

