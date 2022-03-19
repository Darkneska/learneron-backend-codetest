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
        fields = ('id', 'name', 'date_of_birth')


class Query(graphene.ObjectType):
    movies = graphene.List(MovieType)
    actors = graphene.List(ActorType)

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_actors(self, info, **kwargs):
        return Actor.objects.all()


#
# class ActorInput(graphene.InputObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     date_of_birth = graphene.String()
#     title = graphene.String()
#
#
# class CreateActor(graphene.Mutation):
#     class Arguments:
#         actor_data = ActorInput(required=True)
#
#     actors = graphene.Field(ActorType)
#
#     @staticmethod
#     def mutate(root, info, actor_data=None):
#         actor_instance = Actor(
#             name=actor_data.name,
#             date_of_birth=actor_data.year,
#         )
#         actor_instance.save()
#         return CreateActor(actor=actor_instance)
#
#
# class Mutation(graphene.ObjectType):
#     create_actor = CreateActor.Field()
#
#
schema = graphene.Schema(query=Query)
