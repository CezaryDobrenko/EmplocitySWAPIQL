from EmploApp.swapiQL.models import People, Movie

def resolve_movie(self, info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return Movie.objects.get(pk=id)
    return None

def resolve_movies(self, info, **kwargs):
    return Movie.objects.all()

def resolve_moviesFilter(self, info, **kwargs):
    name = kwargs.get('nameOfCharacter')
    if name is not None:
        result = []
        for e in Movie.objects.all():
            if e.MainCharacters.filter(name=name):
                result.append(e)
        return result
    return None
