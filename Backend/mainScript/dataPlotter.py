import time
import threading
import pyqtgraph as pg
import multiprocessing 
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
from Queue import Queue
import sys

class plotterWorker(multiprocessing.Process):
    """ A worker thread that takes directory names from a queue, finds all
        files in them recursively and reports the result.

        Input is done by placing directory names (as strings) into the
        Queue passed in dir_q.

        Output is done by placing tuples into the Queue passed in result_q.
        Each tuple is (thread name, dirname, [list of files]).

        Ask the thread to stop by calling its join() method.
    # """
    def __init__(self, dataQueue):
        super(plotterWorker, self).__init__()
        self.dataQueue = dataQueue       
  

    def run(self):
        self.plotting()
        
    def plotting(self):

        CHANNEL_SIZE = 4
        app = QtGui.QApplication([])

        win = pg.GraphicsWindow(title="Basic plotting examples")
        win.resize(1000,600)
        win.setWindowTitle('pyqtgraph example: Plotting')
    
        curves = []
        
        color = ['y', 'r', 'g', 'b']
        curves = []
        for i in range(CHANNEL_SIZE):
            p = win.addPlot(title="Channel" + str(i+1), row=i, col=0)
            curve = p.plot(pen=color[i])
            curves.append(curve)    

        def updateInProc(curves,q,x,y):
            items = q.get()
            idx = int(items[0])
            x[idx] = items[0]


            for i in range(len(y)):
                y[i][idx]=  items[i+1]
            

            for i,curve in enumerate(curves):
                curve.setData(x,y[i])
            
        y_np = []

        x_np = np.arange(1000)
        # Le 56500 est une valeure moyenne qui est par rapport a notre fichier csv

        for i in range(CHANNEL_SIZE):
            y_np.append(-56500*np.ones(1000))

        timer = QtCore.QTimer()
        timer.timeout.connect(lambda: updateInProc(curves,self.dataQueue,x_np,y_np))
        timer.start(0.004)

        QtGui.QApplication.instance().exec_()
 

    def join(self, timeout=None):
        super(plotterWorker, self).join(timeout)
