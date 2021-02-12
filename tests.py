stuff = {
    #   Deck, Cards required
    'Hybrid forest' : ['72h1S.72h1S','72fJw.72fJw'],
    'Loxis Forest' : ['72h1S.72h1S.72h1S'],
}

def shite_algorithm(spaghetti):
    for key in stuff.keys():
        found = True
        for value in stuff[key]:
            if value not in spaghetti:
                found = False
                break
        if found:
            return key
