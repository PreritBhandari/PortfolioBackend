from django.db import models
from django.utils import timezone


# Blog model for portfolio
class Blog(models.Model):
    blog_category = [
        ('P', 'Programming'),
        ('T', 'Travel'),
        ('E', 'Education'),
        ('O', 'Others')
    ]
    category = models.CharField(max_length=1, choices=blog_category)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    post = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
