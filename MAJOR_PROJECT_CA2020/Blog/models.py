from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details',args=(str(self.id)))