from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class Blog(models.Model):
    Title       = models.CharField(max_length=250)
    pub_date    = models.DateTimeField()
    body        = models.TextField(max_length=5000)
    Image       = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.Title # it shows the actual title in admin panel

    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        return self.pub_date.strftime('%b %e %Y')



# Title

# Pub_date

# body

# Image
