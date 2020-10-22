from aplikacja.swapiQL.models import Movie

def resolve_movies(self, info, **kwargs):
    return Movie.objects.all()