from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import People
from graphene import Node
from graphene import relay

class PeopleType(DjangoObjectType):
    class Meta:
        model = People
        interfaces = (relay.Node, )
        filter_fields = ["name","age"]