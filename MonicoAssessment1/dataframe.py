import pandas as pd

data = pd.read_excel('RoomTemperature.xlsx')

# We're only using the Room, Temperature, and Humidity columns for this exercise.
table = pd.DataFrame(data, columns=['Room', 'Temperature', 'Humidity'])

# Get a set of the room string values for roomColumn and their respective data values
roomColumn = list(set(table['Room']))
tables = [table[table['Room'] == col] for col in roomColumn]
