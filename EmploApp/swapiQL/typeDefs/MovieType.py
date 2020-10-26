from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import Movie
from graphene import Node
from graphene import relay

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        interfaces = (relay.Node, )
        filter_fields = ["MainCharacters__name","title","year"]