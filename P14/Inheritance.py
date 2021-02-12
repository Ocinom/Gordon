class Trees():

    def __init__(self, name, fruit):
        self.name = name
        self.fruit = fruit

    def printEO(self):
        print('This plant can be used in the production of essential oils.')

class Eucalyptus(Trees):

    def __init__(self, name, fruit):
        super().__init__(name, fruit)

    def printEO(self):
        print('These essential oils are volatile.')

class pear(Trees):

    def __init__(self, name, fruit):
        super().__init__(name, fruit)

    def bev(self):
        print('Pears can be used to make \'Perry\' or pear cider')

#Test Trees
tree = Trees('test', 'fruity')
tree.printEO()
#Test Eucalyptus
euc = Eucalyptus('eucky', 'none')
euc.printEO()
#Test pear
pe = pear('peepy', 'pear')
pe.printEO()
pe.bev()