from django.db import models

class People (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    MainCharacters = models.ManyToManyField(People)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Planet (models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    residents = models.ManyToManyField(People)
    gravity = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)