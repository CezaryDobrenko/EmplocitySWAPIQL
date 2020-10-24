from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import Planet

class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet