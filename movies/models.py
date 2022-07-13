from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250, blank=False)
    year = models.DateField(blank=False)

    class Meta:
        db_table = "movies"
