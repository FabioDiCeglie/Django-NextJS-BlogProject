from datetime import timezone
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    coverImage = models.URLField(default="")
    date = models.DateTimeField(auto_now=True)
    author_name = models.CharField(max_length=100, default="")
    author_picture = models.CharField(max_length=300,default="")
    description = models.TextField(default="")

