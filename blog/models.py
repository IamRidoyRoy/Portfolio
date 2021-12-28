from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class Blog(models.Model):
    Title       = models.CharField(max_length=250)
    pub_date    = models.DateTimeField()
    body        = models.TextField(max_length=5000)
    Image       = models.ImageField(upload_to = 'images/')

# Title

# Pub_date

# body

# Image
