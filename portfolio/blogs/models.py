from django.db import models
from django.utils import timezone


# Blog model for portfolio
class Blog(models.Model):
    blog_category = [
        ('Programming', 'Programming'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Others', 'Others')
    ]
    category = models.CharField(max_length=15, choices=blog_category)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    post = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails', default='blog_thumbnails/blog.jpg')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
