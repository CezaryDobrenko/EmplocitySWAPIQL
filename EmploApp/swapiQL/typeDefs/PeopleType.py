from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import People

class PeopleType(DjangoObjectType):
    class Meta:
        model = People