# Use tkinter libraries for GUI, Graph object from matplot.py
import tkinter as tk
from matplot import Graph, rooms

# Initalise master window with set dimensions, not resizable
win = tk.Tk()
win.geometry('1000x500')
win.resizable(False, False)

# Initialise global variables as parameters for the Graph object
roomQuery = ''
typeQuery = ''

# Command functions to set global variables
def setData(room):
    global roomQuery
    roomQuery = room
    data = rooms[room]#.set_index('Room')
    roomsResult.config(text=data)

def setType(type):
    global typeQuery
    typeQuery = type

# Initialise Graph object with global variables
def submit():
    if not roomQuery or not typeQuery:
        return
    result = Graph(roomQuery.replace('.', ''), typeQuery)
    result.getPlot()

# Command function to close program
def exit():
    win.destroy()

# Frame Object to contain the widgets on top (rooms, types, select)
optionsFrame = tk.Frame()

# Drop-down menu to select from the keys() list in the rooms dictionary
roomsvar = tk.StringVar(optionsFrame)
roomsvar.set('Select Room')
roomsMenu = tk.OptionMenu(optionsFrame, roomsvar, *sorted(rooms.keys()), command=setData)
roomsMenu.config(font=('Arial', 15))

# Drop-down menu to select from types in typeslist
typeslist = ['Line', 'Bar']
typesvar = tk.StringVar(optionsFrame)
typesvar.set('Select Graph Type')
types = tk.OptionMenu(optionsFrame, typesvar, *typeslist, command=setType)
types.config(font=('Arial', 15))

# Submit button and close button
select = tk.Button(optionsFrame, text='Plot Graph', command=submit, font=('Arial', 12))
close = tk.Button(win, text='Exit', command=exit, font=('Arial', 12))

# Initialise LabelFrame object to display results from the drop-down lists
resultFrame = tk.LabelFrame(win, text='Room data:', font=('Arial', 25))
roomsResult = tk.Label(resultFrame, text='', font=('Arial', 20))
# typesResult = tk.Label(resultFrame, text='Type: ', font=('Arial', 15))

# Use the pack() function to style and organise the widgets in the program
roomsMenu.pack(side='left', fill='both', expand=True, padx=10)
types.pack(side='left', fill='both', expand=True, padx=10)
select.pack(side='right', fill='both', expand=True, padx=10)
optionsFrame.pack(expand=True, fill='x')

roomsResult.pack()
# typesResult.pack()
resultFrame.pack(fill='x', expand=True)

close.pack(side='bottom', expand=True)

# Start the program with mainloop()
win.mainloop()