
class Animal:

    def __init__(self, species = None, weight = None, age = None, name = None):
        self.species = species
        if self.species != None:
            self.species = self.species.upper()
        self.weight = weight
        if self.weight != None:
            self.weight = float(self.weight)
        self.age = age
        if self.age != None:
            self.age = int(self.age)
        self.name = name
        if self.name != None:
            self.name = self.name.upper()

    def setSpecies(self, species):
        self.species = species
        if self.species != None:
            self.species = self.species.upper()

    def setWeight(self, weight):
        self.weight = weight
        if self.weight != None:
            self.weight = float(self.weight)

    def setAge(self, age):
        self.age = age
        if self.age != None:
            self.age = int(self.age)

    def setName(self, name):
        self.name = name
        if self.name != None:
            self.name = self.name.upper()

    def toString(self):
        return("Species = {}, Name: {}, Age: {}, Weight: {}" \
            .format(self.species, self.name, self.age, self.weight))

a = Animal("dog", 12.2, 2, "Ruffles")
print(a.toString())
