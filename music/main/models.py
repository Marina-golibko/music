from django.db import models

# жанр музыки
class Genre(models.Model):
    name_en = models.CharField(max_length=500, unique=True)
    name_ru = models.CharField(max_length=500, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name_ru
    
# исполнитель (группа или человек)
class Artist(models.Model):
    name = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='artists/', null=True)

    def __str__(self):
        return self.name

# музыкальные треки
class Track(models.Model):
    title = models.CharField(max_length=500, unique=True)
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
