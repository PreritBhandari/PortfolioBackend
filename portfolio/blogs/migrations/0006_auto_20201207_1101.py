# Generated by Django 3.1.4 on 2020-12-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20201207_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(upload_to='blog_thumbnails'),
        ),
    ]