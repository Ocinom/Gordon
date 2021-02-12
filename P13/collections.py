file = open('collections.txt', 'w')

file.write("""deque : A list that can be altered from both ends
Counter: An object that tallies the total number of each instance of a list
defaultdict : An object that creates key a missing key is called""")

file = open('collections.txt', 'r')
print(file.read())

print(file.close())