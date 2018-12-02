from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import numpy as np
import plotly
import plotly.graph_objs as go
fileName = ""

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("RoboteQ Log Graphing Application")

mainframe = ttk.Frame(root, padding= "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable = feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky =(W, E))
ttk.Button(mainframe, text ="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
print (root.filename)

fileName = root.filename


#generate data
try:
    MotorData = np.genfromtxt(fileName, skip_header = 1)
    MotorData = MotorData[:, 3:] #skip time frame columns
except OSError:
    print("could not find file, using exampleArray data")
    MotorData = np.array([[1, 2, 3, 4, 5],
                         [2, 3, 4, 1, 5],
                         [3, 4, 1, 2, 5],
                         [4, 1, 2, 3, 5]])

#plot Data

x_axis = np.linspace(0, np.size(MotorData, 0), np.size(MotorData, 0))

data = []

# Create a trace
for i in range(np.size(MotorData, 1)):
  data.append( go.Scatter(
      x = x_axis,
      y = MotorData[:, i],
      mode = 'lines+markers',
      name = 'Data series ' + str(i)
  ))

plotly.offline.plot(data, auto_open=True)
