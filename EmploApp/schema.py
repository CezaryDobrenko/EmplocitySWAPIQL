import graphene
import EmploApp.swapiQL.schema

class Query(EmploApp.swapiQL.schema.Query, graphene.ObjectType):
    pass

class Mutation(EmploApp.swapiQL.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)