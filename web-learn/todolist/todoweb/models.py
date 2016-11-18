from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    task = models.CharField(max_length=500)

