from random import shuffle

words = 'bacon lettuce tomato shoe cream box pin'.split()

print(words)

shuffle(words)

print('words shuffled: ', end=' ')
print(words)