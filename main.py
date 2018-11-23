from tkinter import filedialog
from tkinter import *
import numpy as np
import plotly
import plotly.graph_objs as go
fileName = ""


root = Tk()
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
