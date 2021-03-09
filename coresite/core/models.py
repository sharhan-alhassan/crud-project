from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Core(models.Model):
    title = models.CharField(max_length=200)