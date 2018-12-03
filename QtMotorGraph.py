import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
import numpy as np
import plotly.plotly
from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import Contours, Histogram2dContour, Marker, Scatter
import re

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",\
            "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.text.setFont(QtGui.QFont("Titillium", 30))
        self.button.setFont(QtGui.QFont("Titillium", 20))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.GraphFile)


    def GraphFile(self):

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open Log"), ".", self.tr("Log Files (*.txt);;All Files (*.*)"))
        fileName = fileName[0]
        #generate data
        f = open(fileName, 'r')
        header = f.readline()
        f.close()

        traceNames = re.findall('(?:[a-zA-Z]+ ?){1,2}[0-9]?', header)
        traceNames = traceNames[1:]



        #TODO figure out why this check is needed
        #It shouldn't need to do this, I'll ask stack overflow
        if len(fileName) == 0 and not ColabRuntime:
            fileName = text.value

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

        x_axis = np.linspace(0, np.size(MotorData, 0)-1, np.size(MotorData, 0))

        data = []

        # Create a trace
        for i in range(np.size(MotorData, 1)):
          data.append( Scatter(
              x = x_axis,
              y = MotorData[:, i],
              mode = 'lines+markers',
              name = traceNames[i]
          ))
        plotly.offline.plot(data, auto_open=True)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
