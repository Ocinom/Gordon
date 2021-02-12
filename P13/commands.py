file = open('commands.txt', 'w')

file.write('This is file.write.')

file = open('commands.txt', 'r')

print('this is file.readline() : ', file.readline())

print('this is file.read(10)', file.read(10))

print('this is file.read()', file.read())

file.close()

file = open('commands.txt', 'a+')
file.write('this is file.write() in a+ mode')

file = open('commands.txt', 'r')

print(file.read())

file.close()