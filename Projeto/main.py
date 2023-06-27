from database import Database
from writeAJson import writeAJson
from clinicaDAO import Animal
from animalCLI import AnimalCLI

db = Database(database="Clinica", collection="Animais")
animalModel = Animal(database=db)



animalCLI = AnimalCLI(animalModel)
animalCLI.run()