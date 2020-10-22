from aplikacja.swapiQL.models import Planet

def resolve_planets(self, info, **kwargs):
    return Planet.objects.all()