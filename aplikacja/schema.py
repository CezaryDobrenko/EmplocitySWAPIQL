import graphene
import aplikacja.swapiQL.schema

class Query(aplikacja.swapiQL.schema.Query, graphene.ObjectType):
    pass

class Mutation(aplikacja.swapiQL.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)  