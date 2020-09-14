from django.db import models

# Create your models here.



class Story(models.Model):
  title = models.CharField(max_length=150)
  desc = models.TextField()

class Post(models.Model):
  title = models.CharField(max_length=150)
  desc = models.TextField()
  image = models.ImageField( upload_to='img')