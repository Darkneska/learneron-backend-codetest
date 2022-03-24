from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    title = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
