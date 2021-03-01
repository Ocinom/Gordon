mother = 'mama'
father = 'papa'
sister = 'sis'
brother = 'bro'

def showFamily(*args):
    for arg in args:
        print(arg)

def showParents(*args):
    for arg in args:
        print(arg)

def showSiblings(*args):
    for arg in args:
        print(arg)


showFamily(mother, father, sister, brother)
showParents(mother, father)
showSiblings(brother, sister)