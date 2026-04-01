from django import forms
from .models import Genre, Track, Artist

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_ru', 'name_en', 'description']
        labels = {
            'name_ru': 'Название на русском',
            'name_en': 'Название на английском',
            'description': 'Описание',
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'artist', 'duration', 'genres']
        labels = {
            'title': 'Название трека',
            'artist': 'Автор',
            'duration': 'Длительность',
            'genres': 'Жанры',
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'name': 'Имя / название',
            'image': 'Фотография',
        }