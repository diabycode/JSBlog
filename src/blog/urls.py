
from django.urls import path

from .views import home, details, create

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('<str:slug>/', details, name="details"),
]



