from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import Movie

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie