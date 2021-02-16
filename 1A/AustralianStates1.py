states = 'Australian Capital Territory,New South Wales,Northern Territory,South Australia,Tasmania,Victoria,Western Australia'.split(',')
abbr = 'ACT NSW NT Qld SA Tas Vic WA'.split(' ')
capital = 'Canberra Sydney Darwin Brisbane Adelaide Hobart Melbourne Perth'.split(' ')
pops = '390,800 7,618,200 244,600 4,779,400 1,698,600 516,600 5,938,100 2,591,600'.split(' ')

for sets in zip(states, abbr, capital, pops):
    for details in sets:
        print(details)
    print('')