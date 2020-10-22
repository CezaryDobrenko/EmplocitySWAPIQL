from aplikacja.swapiQL.models import Planet

def resolve_planet(self, info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return Planet.objects.get(pk=id)
    return None

def resolve_planets(self, info, **kwargs):
    return Planet.objects.all()