class dog():

    species = 'Canis familiaris'

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def printVars(self):
        print('breed: {}\nname: {}\nage: {}'.format(self.breed, self.name, self.age))

fido = dog('breed 1', 'fido', 3)
spike = dog('breed 2', 'spike', 4)
dragon = dog('breed 3', 'dragon', 5)

fido.printVars()
spike.printVars()
dragon.printVars()

print(fido.species)