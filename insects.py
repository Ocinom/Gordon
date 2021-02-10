insects = 'beetle bug mayfly stonefly dragonfly'.split()

print('insects start', insects)

insects.append('butterfly')
insects.append('wasp')
print('insects with additions ', insects)

insects[-3] = 'damsel fly'
print('insects with replacement ', insects)

insects.remove('wasp')
print('insects with removal ', insects)

for i, j in enumerate(insects):
    print('%d  :  %s' % (i, j))