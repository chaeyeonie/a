from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    img = models.FileField(null=True)
    contents = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()