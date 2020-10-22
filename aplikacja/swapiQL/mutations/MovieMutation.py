import graphene
from aplikacja.swapiQL.inputs.modelsInput import MovieInput, PeopleInput
from aplikacja.swapiQL.typeDefs.PeopleType import PeopleType
from aplikacja.swapiQL.typeDefs.MovieType import MovieType 

class CreateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        peoples = []
        for people_input in input.MainCharacters:
          people = People.objects.get(pk=people_input.id)
          if people is None:
            return CreateMovie(ok=False, movie=None)
          peoples.append(people)
        movie_instance = Movie(
          title=input.title,
          year=input.year
          )
        movie_instance.save()
        movie_instance.MainCharacters.set(peoples)
        return CreateMovie(ok=ok, movie=movie_instance)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        movie_instance = Movie.objects.get(pk=id)
        if movie_instance:
            ok = True
            peoples = []
            for people_input in input.MainCharacters:
              people = People.objects.get(pk=people_input.id)
              if people is None:
                return UpdateMovie(ok=False, movie=None)
              peoples.append(people)
            movie_instance.title=input.title
            movie_instance.year=input.year
            movie_instance.save()
            movie_instance.MainCharacters.set(peoples)
            return UpdateMovie(ok=ok, movie=movie_instance)
        return UpdateMovie(ok=ok, movie=None)