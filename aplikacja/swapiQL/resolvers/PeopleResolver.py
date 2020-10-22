from aplikacja.swapiQL.models import People

def resolve_people(self, info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return People.objects.get(pk=id)
    return None

def resolve_peoples(self, info, **kwargs):
    return People.objects.all()