from graphene_django.types import DjangoObjectType, ObjectType
from aplikacja.swapiQL.models import People

class PeopleType(DjangoObjectType):
    class Meta:
        model = People