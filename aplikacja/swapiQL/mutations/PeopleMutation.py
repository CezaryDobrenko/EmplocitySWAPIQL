import graphene
from aplikacja.swapiQL.models import People
from aplikacja.swapiQL.inputs.modelsInput import PeopleInput
from aplikacja.swapiQL.typeDefs.PeopleType import PeopleType


class CreatePeople(graphene.Mutation):
    class Arguments:
        input = PeopleInput(required=True)

    isCompleted = graphene.Boolean()
    people = graphene.Field(PeopleType)

    @staticmethod
    def mutate(root, info, input=None):
        isCompleted = True
        people_instance = People(name=input.name,age=input.age)
        people_instance.save()
        return CreatePeople(isCompleted=isCompleted, people=people_instance)

class UpdatePeople(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PeopleInput(required=True)

    isCompleted = graphene.Boolean()
    peoples = graphene.Field(PeopleType)

    @staticmethod
    def mutate(root, info, id, input=None):
        isCompleted = False
        peoples_instance = People.objects.get(pk=id)
        if peoples_instance:
            isCompleted = True
            peoples_instance.name = input.name
            peoples_instance.age = input.age
            peoples_instance.save()
            return UpdatePeople(isCompleted=isCompleted, peoples=peoples_instance)
        return UpdatePeople(isCompleted=isCompleted, peoples=None)