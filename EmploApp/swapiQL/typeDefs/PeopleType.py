from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import People
from graphene import Node

class PeopleType(DjangoObjectType):
    class Meta:
        model = People
        interfaces = (Node,)
        filter_fields = ["name","age"]