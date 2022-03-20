import graphene
from graphene_django import DjangoObjectType
from .models import Movie, Actor


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year')


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'date_of_birth', 'title')


class Query(graphene.ObjectType):
    movies = graphene.List(MovieType)

    def resolve_movies(root, info):
        # Querying a list
        return Movie.objects.all()


schema = graphene.Schema(query=Query)

