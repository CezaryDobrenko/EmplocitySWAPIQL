import pytest
import graphene 
from graphene import ObjectType, String
from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.models import People, Movie
from EmploApp.swapiQL.typeDefs.PeopleType import PeopleType
from EmploApp.swapiQL.typeDefs.MovieType import MovieType 
from EmploApp.swapiQL.resolvers.MovieResolver import resolve_moviesFilter

@pytest.mark.django_db
def test_checkForPresenceOfMaceWinduInMovies():

    class Query(ObjectType):
        moviesByCharacter= graphene.List(MovieType, nameOfCharacter=graphene.String(), resolver=resolve_moviesFilter)

    schema = graphene.Schema(query=Query)
    result = schema.execute(
        '''
        query testMoviesByCharacter{
            moviesByCharacter(nameOfCharacter:"Mace Windu"){
                title
                MainCharacters {
                    name
                }
            }
        }
        '''
    )
    
    countPresenceInMovies = len(list(result.data.items())[0][1])

    assert countPresenceInMovies > 0
