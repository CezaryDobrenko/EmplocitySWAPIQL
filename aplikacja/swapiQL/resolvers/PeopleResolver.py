from aplikacja.swapiQL.models import People

def resolve_peoples(self, info, **kwargs):
    return People.objects.all()