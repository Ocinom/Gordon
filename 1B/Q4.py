num1 = int(input('Type your first number: '))
num2 = int(input('Type your second number: '))

print('Your numbers are: %d and %d' % (num1, num2))

num1 += 10
num2 += 20

print('After adding 10 to the first number and 20 to the second number, you get:', end=' ')
print('%d and %d' % (num1, num2))

print('Adding both numbers together yields %d' % (num1 + num2))