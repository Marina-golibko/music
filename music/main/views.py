from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Track, Artist
from .forms import GenreForm, TrackForm, ArtistForm

# Create your views here.
def main(request):
    return render(request, 'index.html', {'tab': 'main'})

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'janri.html', {'genres': genres, 'tab': 'genres'})

def tracks_list(request):
    #tracks = Track.objects.all().prefetch_related('genres')
    # получим список треков из базы
    t = Track.objects.all()
    # получим список исполнителей
    a = Artist.objects.all()
    artist = None
    # передали исполнителя
    if request.method == "POST":
        id_artist = request.POST.get('artist')
        # Проверяем: если id_artist не пустой (выбран конкретный артист)
        if id_artist: 
            artist = Artist.objects.get(id=id_artist)
            t = t.filter(artist=artist)
        # Если id_artist пустой, блок выше пропустится и 't' останется Track.objects.all()
    return render(request, 'treki.html', {'tracks': t, 'artists': a, 'current_artist': artist, 'tab': 'tracks'})

def artists(request):
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a, 'tab': 'artists'})

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
