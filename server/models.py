# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SuperHero(models.Model):
    name = models.CharField(default='',max_length=60,unique=True)
    alias = models.CharField(default='',max_length=60)
    photo = models.ImageField(upload_to="gallery")
    description = models.CharField(default='',max_length=120)
    favorite = models.BooleanField(default=False)
