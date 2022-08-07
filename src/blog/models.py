from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur")
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    sub_title = models.CharField(max_length=255, blank=True, verbose_name="Sous titre")
    content = models.TextField(verbose_name="Contenu")
    published = models.BooleanField(default=False, verbose_name="Publié")
    last_edit = models.DateTimeField(auto_now=True, verbose_name="Dernière modif")
    publish_date = models.DateField(blank=True, null=True, verbose_name="Publié le")

    class Meta:
        verbose_name = "Post"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
