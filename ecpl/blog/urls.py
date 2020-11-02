
from django.urls import path
from .views import blog,blogdetails

urlpatterns = [
    path('',blog),

    path('blogdetails/<int:pk>',blogdetails,name="blogdetails"),

]
