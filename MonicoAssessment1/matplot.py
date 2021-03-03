import matplotlib.pyplot as plt
from dataframe import tables, roomColumn

# Initialise a dictionary to reference the respective tables from the string values of the room numbers
rooms = {string : obj for string, obj in zip(roomColumn, tables)}

# We'll be using a class object to generate different graphs based on the room selected and the type of graph selected
class Graph():

    # Object variables: room number, graph type, plot
    def __init__(self, room: str, type: str):
        self.room = room
        self.type = type
        self.title = room[:2] + '.' + room[2:]

    def __str__(self):
        return self.title

    # Method to plot a line graph on matplotlib
    def makeLine(self):
        fig, ax = plt.subplots()
        graph = rooms[self.room]
        ax.plot(graph['Temperature'], graph['Humidity'], label=self.title)
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Humidity')
        ax.set_title(self.title)
        ax.legend()

    # Method to plot a bar graph on matplotlib
    def makeHist(self):
        fig, ax = plt.subplots()
        graph = rooms[self.room]
        ax.bar(graph['Temperature'], graph['Humidity'], label=self.title)
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Humidity')
        ax.set_title(self.title)

    # Display the plotted graph
    def show(self):
        plt.show()

    # Display plotted graph based on the type of graph in the object variable
    def getPlot(self):
        if self.type.lower() == 'line':
            self.makeLine()
        elif self.type.lower() == 'bar':
            self.makeHist()
        self.show()
