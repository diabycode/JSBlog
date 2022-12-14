# Generated by Django 4.1 on 2022-08-07 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('sub_title', models.CharField(blank=True, max_length=255, verbose_name='Sous titre')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('published', models.BooleanField(default=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
