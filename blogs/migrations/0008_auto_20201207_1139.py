# Generated by Django 3.1.4 on 2020-12-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20201207_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default='blog_thumbnails/blog.jpg', upload_to='blog_thumbnails'),
        ),
    ]
