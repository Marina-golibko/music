from django import forms
from .models import Genre, Track

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
        fields = ['title', 'duration', 'genres']
        labels = {
            'title': 'Название трека',
            'duration': 'Длительность',
            'genres': 'Жанры',
        }