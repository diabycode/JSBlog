
from django.contrib import admin
from django.urls import path, include

from .views import index


urlpatterns = [
    path('', index, name="index"),
    path('blog/', include('blog.urls')),
    path('jsb-admin149/', admin.site.urls),
]
