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
        return Movie.objects.all()


class ActorInput(graphene.InputObjectType):
    name = graphene.String()
    date_of_birth = graphene.Date()


class CreateActor(graphene.Mutation):
    class Arguments:
        actor_data = ActorInput(required=True)

    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root, info, actor_data=None):
        actor_instance = Actor(
            name=actor_data.name,
            date_of_birth=actor_data.date_of_birth
        )
        actor_instance.save()
        return CreateActor(actor=actor_instance)


class MovieInput(graphene.InputObjectType):
    id = graphene.ID
    name = graphene.String()
    year = graphene.String()


class CreateMovie(graphene.Mutation):
    class Arguments:
        movie_data = MovieInput(required=True)

    movie = graphene.Field(ActorType)

    @staticmethod
    def mutate(root, info, movie_data=None):
        movie_instance = Movie(
            id=movie_data.id,
            name=movie_data.name,
            year=movie_data.year
        )
        movie_instance.save()
        return CreateMovie(movie=movie_instance)


class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()
    create_movie = CreateMovie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
