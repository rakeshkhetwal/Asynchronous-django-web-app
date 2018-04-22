from django.db import models

# Create your models here.


class names(models.Model):
    your_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwod = models.CharField(max_length=100)
