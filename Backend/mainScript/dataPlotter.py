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
        app = QtGui.QApplication([])

        win = pg.GraphicsWindow(title="Basic plotting examples")
        win.resize(1000,600)
        win.setWindowTitle('pyqtgraph example: Plotting')
        p1 = win.addPlot(title="Channel 1", row = 0, col = 0)
        p2 = win.addPlot(title="Channel 2", row = 1, col = 0)
        p3 = win.addPlot(title="Channel 2", row = 0, col = 1)
        p4 = win.addPlot(title="Channel 2", row = 1, col = 1)
        curve1 = p1.plot(pen='y')
        curve2 = p2.plot(pen='r')
        curve3 = p3.plot(pen='g')
        curve4 = p4.plot(pen='b')

        curves = [curve1, curve2, curve3, curve4]


        x_np = np.arange(1000)
        # Le 56500 est une valeure moyenne qui est par rapport a notre fichier csv
        y_np1 = -56500*np.ones(1000)
        y_np2 = -56500*np.ones(1000)
        y_np3 = -56500*np.ones(1000)
        y_np4 = -56500*np.ones(1000)

        y_np = [y_np1, y_np2, y_np3, y_np4]
    

        def updateInProc(curves,q,x,y):
            item = q.get()
            idx = int(item[0])
            x[idx] = item[0]
            y[0][idx]=  item[1]
            y[1][idx]=  item[2]
            y[2][idx]=  item[3]
            y[3][idx]=  item[4]
            for i,curve in enumerate(curves):
                curve.setData(x,y[i])
            #curves[0].setData(x,y)
            #curves[1].setData(x,y)
        

        timer = QtCore.QTimer()
        timer.timeout.connect(lambda: updateInProc(curves,self.dataQueue,x_np,y_np))
        timer.start(0.004)

        QtGui.QApplication.instance().exec_()
        
       
 

    def join(self, timeout=None):
        super(plotterWorker, self).join(timeout)
