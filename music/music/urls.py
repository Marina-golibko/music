"""
URL configuration for music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('genres/', views.genres_list),
    path('tracks/', views.tracks_list),
    path('add_genre/', views.add_genre),
    path('edit_genre/<int:id>/', views.edit_genre),
    path('delete_genre/<int:id>/', views.delete_genre),
    path('add_track/', views.add_track),
    path('edit_track/<int:id>/', views.edit_track),
    path('delete_track/<int:id>/', views.delete_track),
    path('artists/', views.artists),
]
