import graphene 
from graphene import ObjectType, String
from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import People, Movie
from EmploApp.swapiQL.typeDefs.PeopleType import PeopleType
from EmploApp.swapiQL.typeDefs.MovieType import MovieType 
from EmploApp.swapiQL.typeDefs.PlanetType import PlanetType 
from EmploApp.swapiQL.resolvers.PeopleResolver import resolve_people, resolve_peoples
from EmploApp.swapiQL.resolvers.MovieResolver import resolve_movie, resolve_movies, resolve_moviesFilter
from EmploApp.swapiQL.resolvers.PlanetResolver import resolve_planet, resolve_planets
from EmploApp.swapiQL.mutations.MovieMutation import CreateMovie, UpdateMovie
from EmploApp.swapiQL.mutations.PeopleMutation import CreatePeople, UpdatePeople

class Query(ObjectType):
    planet = graphene.Field(PlanetType, id=graphene.Int(), resolver=resolve_planet)
    people = graphene.Field(PeopleType, id=graphene.Int(), resolver=resolve_people)
    movie = graphene.Field(MovieType, id=graphene.Int(), resolver=resolve_movie)
    planets= graphene.List(PlanetType, resolver=resolve_planets)
    peoples = graphene.List(PeopleType, resolver=resolve_peoples)
    movies= graphene.List(MovieType, resolver=resolve_movies)
    moviesByCharacter= graphene.List(MovieType, nameOfCharacter=graphene.String(), resolver=resolve_moviesFilter)


class Mutation(graphene.ObjectType):
    create_people = CreatePeople.Field()
    create_movie = CreateMovie.Field()
    update_people = UpdatePeople.Field()
    update_movie = UpdateMovie.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
