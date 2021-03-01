class shellfish():
    location = 'ocean'
    skeleton = 'exoskeleton'

    def __init__(self, shape, type):
        self.shape = shape
        self.type = type

snail = shellfish('spiral', 'snail')
mussel = shellfish('flat-plates', 'tubular')

print('object1 type: {}\nobject1 shape: {}'.format(snail.type, snail.shape))

print('object2 location: {}\nobject2 type: {}\nobject2 shape: {}'.format(
    mussel.location, mussel.type, mussel.shape
))