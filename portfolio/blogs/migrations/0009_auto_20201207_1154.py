# Generated by Django 3.1.4 on 2020-12-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20201207_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Programming', 'Programming'), ('Travel', 'Travel'), ('Education', 'Education'), ('Others', 'Others')], max_length=15),
        ),
    ]