import pytest
import json
import graphene 
from graphene import ObjectType
from graphene_django.types import DjangoObjectType, ObjectType
from EmploApp.swapiQL.typeDefs.PeopleType import PeopleType
from EmploApp.swapiQL.typeDefs.MovieType import MovieType 
from EmploApp.swapiQL.resolvers.MovieResolver import resolve_moviesFilter
from EmploApp.swapiQL.data.dataForUnitTests import checkForPresenceOfMaceWinduInMoviesData

@pytest.mark.django_db
def test_checkForPresenceOfMaceWinduInMovies():
    checkForPresenceOfMaceWinduInMoviesData()

    class Query(ObjectType):
        moviesByCharacter= graphene.List(MovieType, nameOfCharacter=graphene.String(), resolver=resolve_moviesFilter)

    schema = graphene.Schema(query=Query)
    result = schema.execute(
        '''
        query unitTestForMovieFilterByCharacter{
            moviesByCharacter(nameOfCharacter:"Mace Windu"){
                title
                year
                MainCharacters {
                    name
                }
            }
        }
        '''
    )
    
    countPresenceInMovies = len(list(result.data.items())[0][1])
    recivedResult = list(result.data.items())[0][1]

    expectedValueOfMovies = 2
    expectedResult = [
        {'title': 'Gwiezdne wojny cz II', 'year': 2002, 'MainCharacters': [{'name': 'Anakin Skywalker'}, {'name': 'Mace Windu'}, {'name': 'Obi-Wan Kenobi'}]},
        {'title': 'Gwiezdne wojny cz III', 'year': 2005, 'MainCharacters': [{'name': 'Anakin Skywalker'}, {'name': 'Mace Windu'}, {'name': 'Obi-Wan Kenobi'}, {'name': 'Sheev Palpatine'}]}
    ]

    assert not result.errors
    assert countPresenceInMovies == expectedValueOfMovies
    assert recivedResult == expectedResult
