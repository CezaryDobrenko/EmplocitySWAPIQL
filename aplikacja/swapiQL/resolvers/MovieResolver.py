from aplikacja.swapiQL.models import Movie

def resolve_movie(self, info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return Movie.objects.get(pk=id)
    return None

def resolve_movies(self, info, **kwargs):
    return Movie.objects.all()