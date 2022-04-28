import strawberry
from .types import *
from strawberry_django_plus import gql
from .models import Artist, Album, Song
from strawberry.django import auto
from typing import List

@gql.django.type(Artist)
class ArtistType:
    name: auto
    albums: "List[AlbumType]"

@gql.django.type(Album)
class AlbumType:
    name: auto
    release_date: auto
    artist: ArtistType
    songs: "List[SongType]"

@gql.django.type(Song)
class SongType:
    name: auto
    duration: auto
    album_type: AlbumType

