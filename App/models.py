from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    statut = models.CharField(max_length=25, default='simple')
    profile_photo = models.ImageField(blank=True)


class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)
    time_pub = models.DateTimeField('date published', default=timezone.now())
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    content =  models.CharField(max_length=1000)
    time_pub = models.DateTimeField('date published', default=timezone.now())