from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Track
from .forms import GenreForm, TrackForm

# Create your views here.
def main(request):
    return render(request, 'index.html', {'tab': 'main'})

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'janri.html', {'genres': genres, 'tab': 'genres'})

def tracks_list(request):
    tracks = Track.objects.all().prefetch_related('genres')
    return render(request, 'treki.html', {'tracks': tracks, 'tab': 'tracks'})

# добавить жанр
def add_genre(request):
    # получили данные. нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    # это простой запрос, нужно показать форму
    else:
        genreform = GenreForm()
        return render(request, "add_genre.html", {'form': genreform})


def edit_genre(request, id):
    # 1. Находим конкретный жанр по ID из ссылки
    genre = get_object_or_404(Genre, id=id)
    
    if request.method == "POST":
        # 2. Связываем форму с этим конкретным жанром (instance=genre)
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('/genres/')
    else:
        # 3. Показываем форму, заполненную данными этого жанра
        form = GenreForm(instance=genre)
        return render(request, "edit_genre.html", {"form": form, "tab": "genres"})

def delete_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return redirect('/genres/')

# добавить трек
def add_track(request):
    # получили данные. нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        track = TrackForm(request.POST)
        if track.is_valid():
            track.save()
        return redirect('/tracks')
    # это простой запрос, нужно показать форму
    else:
        trackform = TrackForm()
        return render(request, "add_track.html", {'form': trackform})


def edit_track(request, id):
    # 1. Находим конкретный трек по ID из ссылки
    track = get_object_or_404(Track, id=id)
    
    if request.method == "POST":
        # 2. Связываем форму с этим конкретным жанром (instance=genre)
        track = TrackForm(request.POST, instance=track)
        if track.is_valid():
            track.save()
            return redirect('/tracks/')
    else:
        # 3. Показываем форму, заполненную данными этого жанра
        form = TrackForm(instance=track)
        return render(request, "edit_track.html", {"form": form, "tab": "genres"})

def delete_track(request, id):
    track = get_object_or_404(Track, id=id)
    track.delete()
    return redirect('/tracks/')

