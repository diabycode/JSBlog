from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost


# Create your views here.
def home(request):
    posts = BlogPost.objects.all()

    return render(request, "blog/home.html", context={"posts": posts})

