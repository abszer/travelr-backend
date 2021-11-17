from django.db import models

# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=20)
     image_url = models.TextField()
     likes = models.IntegerField()
     public = models.BooleanField()
     description = models.CharField(max_length=200)
     location = models.CharField(max_length=128)