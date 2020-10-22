import graphene 
from graphene import ObjectType, String
from graphene_django.types import DjangoObjectType, ObjectType
from aplikacja.swapiQL.models import People, Movie
from aplikacja.swapiQL.typeDefs.PeopleType import PeopleType
from aplikacja.swapiQL.typeDefs.MovieType import MovieType 
from aplikacja.swapiQL.typeDefs.PlanetType import PlanetType 
from aplikacja.swapiQL.resolvers.PeopleResolver import resolve_peoples
from aplikacja.swapiQL.resolvers.MovieResolver import resolve_movies
from aplikacja.swapiQL.resolvers.PlanetResolver import resolve_planets

class Query(ObjectType):
    planets= graphene.List(PlanetType, resolver=resolve_planets)
    peoples = graphene.List(PeopleType, resolver=resolve_peoples)
    movies= graphene.List(MovieType, resolver=resolve_movies)

schema = graphene.Schema(query=Query)