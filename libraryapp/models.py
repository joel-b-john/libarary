from django.db import models

# Create your models here.
class library(models.Model):
    book = models.CharField(max_length=250)
    published = models.IntegerField()
    exsheet = models.TextField()