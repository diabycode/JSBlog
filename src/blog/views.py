from django.http import HttpResponse
from django.shortcuts import render

from .forms import BlogPostCreateFrom
from .models import BlogPost


# Home view
def home(request):
    posts = BlogPost.objects.all()

    return render(request, "blog/home.html", context={"posts": posts})


# posts details view
def details(request, slug):
    post = BlogPost.objects.get(slug=slug)

    return render(request, "blog/details.html", context={"post": post})


# post create view
def create(request):
    form = BlogPostCreateFrom()

    return render(request, "blog/create.html", context={"form": form})
