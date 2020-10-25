from EmploApp.swapiQL.models import People, Movie

def checkForPresenceOfMaceWinduInMoviesData():
    
    People1 = People()
    People1.name = "Mace Windu"
    People1.age = 37
    People1.save()

    People2 = People()
    People2.name = "Anakin Skywalker"
    People2.age = 23
    People2.save()

    People3 = People()
    People3.name = "Sheev Palpatine"
    People3.age = 52
    People3.save()

    People4 = People()
    People4.name = "Obi-Wan Kenobi"
    People4.age = 27
    People4.save()

    Movie1 = Movie()
    Movie1.id = 1
    Movie1.title = "Gwiezdne wojny część I – Mroczne widmo"
    Movie1.MainCharacters.set([People2.id, People4.id])
    Movie1.year = 1999
    Movie1.save()

    Movie2 = Movie()
    Movie2.id = 2
    Movie2.title = "Gwiezdne wojny część II – Atak klonów"
    Movie2.MainCharacters.set([People1.id, People2.id, People4.id])
    Movie2.year = 2002
    Movie2.save()

    Movie3 = Movie()
    Movie3.id = 3
    Movie3.title = "Gwiezdne wojny część III – Zemsta Sithów"
    Movie3.MainCharacters.set([People1.id, People2.id, People3.id, People4.id])
    Movie3.year = 2005
    Movie3.save()