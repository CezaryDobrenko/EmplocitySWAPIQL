import pytest
import json
import graphene 
from graphene_django.types import ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from EmploApp.swapiQL.typeDefs.PeopleType import PeopleType
from EmploApp.swapiQL.typeDefs.MovieType import MovieType 
from EmploApp.swapiQL.data.dataForUnitTests import checkForPresenceOfMaceWinduInMoviesData

@pytest.mark.django_db
def test_checkForPresenceOfMaceWinduInMovies():
    checkForPresenceOfMaceWinduInMoviesData()

    class Query(ObjectType):
        moviesByCharacter = DjangoFilterConnectionField(MovieType)

    schema = graphene.Schema(query=Query)
    result = schema.execute(
        '''
        query unitTestForMovieFilterByCharacter{
            moviesByCharacter(MainCharacters_Name:"Mace Windu"){
                edges{
                    node{
                        title
                        year
                        MainCharacters(name:"Mace Windu"){
                            edges{
                                node{
                                    name
                                }
                            }
                        }
                    }
                }
            }
        }
        '''
    )
    
    recivedResult = list(result.data.items())

    expectedResult = [('moviesByCharacter', {'edges': [
        {'node': {'title': 'Gwiezdne wojny cz II', 'year': 2002, 'MainCharacters': {'edges': [{'node': {'name': 'Mace Windu'}}]}}}, 
        {'node': {'title': 'Gwiezdne wojny cz III', 'year': 2005, 'MainCharacters': {'edges': [{'node': {'name': 'Mace Windu'}}]}}}
    ]})]

    assert not result.errors
    assert recivedResult == expectedResult

