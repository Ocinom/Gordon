class trains():

    substrate = 'track'

    def __init__(self, fuelType, cargo, numberOfCarriages):
        self.fuel = fuelType
        self.cargo = cargo
        self.num = numberOfCarriages

    def printAll(self):
        print('fuel: %s\ncargo: %s\nnumber of carriages: %d' % (self.fuel, self.cargo, self.num))

passenger = trains('coal', 'people', 7)
freight = trains('coal', 'inventory', 10)
steam = trains('steam', 'general', 5)

print('passenger train:')
passenger.printAll()
print('\nfreight train:')
freight.printAll()
print('\nsteam')
steam.printAll()