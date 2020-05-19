from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post_title = models.CharField('Title', max_length=100)
    post_content = models.TextField('Content', max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    # delete all posts once author is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post_title
