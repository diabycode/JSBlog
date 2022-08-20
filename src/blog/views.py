from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import BlogPostCreateForm, BlogPostEditForm
from .models import BlogPost


# Home view
def home(request):
    posts = BlogPost.objects.filter(published=True)
    if request.user.is_authenticated:
        posts = BlogPost.objects.all()

    return render(request, "blog/home.html", context={"posts": posts})


# posts details view
def details(request, slug):
    post = BlogPost.objects.get(slug=slug)
    author = post.author if post.author else None
    date_formated = None
    if post.publish_date:
        date_formated = post.publish_date.strftime("%d/%m/%Y")

    return render(
        request,
        "blog/details.html",
        context={
            "post": post,
            "author": author,
            "date_formated": date_formated,
        }
    )


# post create view
@login_required
def create(request):
    form = None

    if request.method == "POST":
        form = BlogPostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:home")

    # getting user
    user_conected = request.user
    if not user_conected.is_authenticated:
        user_conected = None

    # getting posts creater form
    if not form:
        form = BlogPostCreateForm(initial={"author": user_conected})

    return render(request, "blog/create.html", context={"form": form})


@login_required
def edit(request, slug):
    post = BlogPost.objects.get(slug=slug)

    if request.method == "POST":
        form = BlogPostEditForm(request.POST, instance=post)

        # save new data
        if form.is_valid():
            post.save()
            return redirect("blog:details", slug=post.slug)
    else:
        form = BlogPostEditForm(initial={
            "author": post.author,
            "title": post.title,
            "sub_title": post.sub_title,
            "content": post.content,
            "published": post.published,
            "publish_date": post.publish_date,
        })

    return render(request, "blog/edit.html", context={"form": form})


@login_required
def delete(request, slug):
    post = BlogPost.objects.get(slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect("blog:home")

    return render(request, "blog/delete.html", context={"post": post})


# def logout(request):
#     if request.user.is_authenticated:
#         request.user = ""
#
#     return redirect("blog:home")

