from email.policy import default
from enum import auto
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='blog_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
# Create your models here.
