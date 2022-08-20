
from django.urls import path

from .views import home, details, create, edit, delete

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('<str:slug>/edit', edit, name="edit"),
    path('<str:slug>/delete', delete, name="delete"),
    path('<str:slug>/', details, name="details"),
]



