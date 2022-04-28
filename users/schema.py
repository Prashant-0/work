from strawberry_django_plus import gql
from .models import Artist, Album, Song
import strawberry
from strawberry_django_plus.directives import SchemaDirectiveExtension
from typing import List
from .types import ArtistType, SongType, AlbumType

@gql.type
class Query:
    artist: Artist = gql.django.field()
    songs: List[SongType] = gql.django.field()
    
@gql.django.type(Artist)
class SomeModelType(gql.Node):
    name: gql.auto

@gql.django.input(Song)
class SomeModelInput:
    name: gql.auto

@gql.django.partial(Album)
class SomeModelInputPartial(gql.NodeInput):
    name: gql.auto

@gql.type
class Mutations:
    create_model: ArtistType = gql.django.create_mutation(SomeModelInput)
    update_model: SongType = gql.django.update_mutation(SomeModelInputPartial)
    delete_model: AlbumType = gql.django.delete_mutation(gql.NodeInput)
    
# schema = Schema(types=[ArtistType, AlbumType, SongType, Query])
schema = strawberry.Schema(query=Query)
