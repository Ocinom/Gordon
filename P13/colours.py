colours = """red
orange
yellow
green
blue
indigo
violet""".title()

file = open('colours.txt', 'w')
file.write(colours)

file = open('colours.txt', 'r')
print(file.readline())
for line in file.readlines():
    print(line)
file.close()