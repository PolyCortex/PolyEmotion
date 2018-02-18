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
        app2 = QtGui.QApplication([])

        win2 = pg.GraphicsWindow(title="Basic plotting examples")
        win2.resize(1000,600)
        win2.setWindowTitle('pyqtgraph example: Plotting')
        p2 = win2.addPlot(title="Updating plot")
        curve = p2.plot(pen='y')

        x_np = []
        y_np = []

        def updateInProc(curve,q,x,y):
            item = q.get()
            x.append(item[1])
            y.append(item[0])
            curve.setData(x,y)

        timer = QtCore.QTimer()
        timer.timeout.connect(lambda: updateInProc(curve,self.dataQueue,x_np,y_np))
        timer.start(0.1)

        QtGui.QApplication.instance().exec_()
        
       
    def updateInProc(curve,q,x,y):
            item = q.get()
            x.append(item[0])
            y.append(item[1])
            
            self.curve.setData(x,y)    

    def join(self, timeout=None):
        super(plotterWorker, self).join(timeout)
