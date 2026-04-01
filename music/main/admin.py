from django.contrib import admin
from .models import Genre, Track, Artist

# Register your models here.
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Artist)
