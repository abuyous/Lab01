
from Animal import Animal

class AnimalShelter:
    
    def __init__(self):
        self.animal_dict = {}
        #species (str) -> list of animals

    def addAnimal(self, animal):
        specie = animal.species
        if specie not in self.animal_dict:
            self.animal_dict[specie] = [animal]
        else:
            self.animal_dict[specie].append(animal)

    def printDick(self):
        print(self.animal_dict)
    




    
        
a = Animal("dog", 12.2, 2, "Ruffles")
b = Animal("dog", None, None, None)
PYC = AnimalShelter()
PYC.addAnimal(a)
PYC.addAnimal(b)
PYC.printDick()
