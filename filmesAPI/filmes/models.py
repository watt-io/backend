from django.db import models

# Create your models here.
class Movie(models.Model):
    MovieId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    yearRelease = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    budgetCost = models.IntegerField()
    countryOrigin = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)

