class trees():
    kingdom = 'Plantae'

    def __init__(self, type, height, locations):
        self.type = type
        self.height = height
        self.locations = locations

    def printAll(self):
        print('type: %s\nheight: %s\nlocations: %s' % (self.type, self.height, self.locations))

tree1 = trees('very big', 'very tall', 'very far')
tree2 = trees('kinda big', 'a little bit tall', 'not too far')
tree3 = trees('small-ish', 'short', 'pretty near')

print('tree1: ')
tree1.printAll()
print('\ntree2: ')
tree2.printAll()
print('\ntree3: ')
tree3.printAll()