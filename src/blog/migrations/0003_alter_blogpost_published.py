# Generated by Django 4.1 on 2022-08-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_options_alter_blogpost_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Publié'),
        ),
    ]
