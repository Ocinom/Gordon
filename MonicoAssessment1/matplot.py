import matplotlib.pyplot as plt
from dataframe import tables, roomColumn

# We'll be using a class object to generate different graphs based on the room selected and the type of graph selected
class Graph():

    # Initialise a dictionary to reference the respective tables from the string values of the room numbers
    rooms = {string : obj for string in roomColumn for obj in tables}

    # Object variables: room number, graph type, plot
    def __init__(self, room: str, type: str):
        self.room = room
        self.type = type
        self.plot = plt

    # Method to plot a line graph on matplotlib
    def makeLine(self):
        fig, ax = self.plot.subplots()
        graph = self.rooms[self.room]
        ax.plot(graph['Temperature'], graph['Humidity'], label=self.room.upper())
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Humidity')
        ax.set_title(self.room)
        ax.legend()

    # Method to plot a bar graph on matplotlib
    def makeHist(self):
        fig, ax = self.plot.subplots()
        graph = self.rooms[self.room]
        ax.bar(graph['Temperature'], graph['Humidity'])
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Humidity')
        ax.set_title(self.room)

    # Display the plotted graph
    def show(self):
        self.plot.show()

    # Display plotted graph based on the type of graph in the object variable
    def getPlot(self):
        if self.type.lower() == 'line':
            self.makeLine()
        else:
            self.makeHist()
        self.show()