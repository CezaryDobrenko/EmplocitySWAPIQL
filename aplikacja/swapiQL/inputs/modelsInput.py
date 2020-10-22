import graphene

class PeopleInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()

class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    MainCharacters = graphene.List(PeopleInput)
    year = graphene.Int()