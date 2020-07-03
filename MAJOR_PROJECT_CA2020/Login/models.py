from django.db import models

# Create your models here.
class LoginApp(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Address=models.CharField(max_length=100)
    Email=models.CharField(max_length=30)

