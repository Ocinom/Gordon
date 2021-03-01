class sport():
    activity = 'physical'
    games = 'competitive'

    def __init__(self, name, numberOfPlayers, ballShape):
        self.name = name
        self.numberOfPlayers = numberOfPlayers
        self.ballShape = ballShape

    def printAll(self):
        print('name: %s\nnumber of players: %d\nball shape: %s' % (self.name, self.numberOfPlayers, self.ballShape))

    def __str__(self):
        return 'activity: %s\ngames: %s' % (self.activity, self.games)

footy = sport('footy', 12, 'spherical')
rugby = sport('rugby', 20, 'oblong')

print('footy: ')
footy.printAll()
print('\nrugby: ')
rugby.printAll()

cricket = sport('cricket', 12, 'round')
print('\ncricket: ')
print(cricket)
cricket.printAll()