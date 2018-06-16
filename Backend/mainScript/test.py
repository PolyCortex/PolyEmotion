#
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.fftpack
#
# # Number of samplepoints
# N = 600
# # sample spacing
# T = 1.0 / 800.0
# x = np.linspace(0.0, N*T, N)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
# yf = scipy.fftpack.fft(y)
#
# xf = np.linspace(0.0, 1.0/(2.0*T), 300)
#
# fig, ax = plt.subplots()
# ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
#
# plt.show()


# -*- coding: utf-8 -*-


import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

import multiprocessing
from multiprocessing import Process, Lock, Queue
from random import random

import pyqtgraph.multiprocess
#
#
# class CreateData(multiprocessing.Process):
#
#     def __init__(self, dataQueue):
#         super(CreateData, self).__init__()
#         self.dataQueue = dataQueue
#
#     def create_data(l):
#         l.acquire()
#         dataQueue.put(random(1))
#         print('hello world')
#         l.release()
#
#         for num in range(10):
#             Process(target=f, args=(lock, num)).start()


class PlotData(multiprocessing.Process):
    """
    Ploting data with pyqtgraph under a class format
    """
    def __init__(self, dataQueue):
        super(PlotData, self).__init__()
        self.dataQueue = dataQueue

        self._win = pg.GraphicsWindow(title='...', size=(600,600))
        self._chunkSize = 100
        self._maxChunks = 10
        self._startTime = pg.ptime.time()
        # self._win.nextRow()
        self._p = self._win.addPlot()
        self._p.setLabel('bottom', '...', '...')
        self._p.setXRange(-10, 0)
        self._curves = []
        self._data = np.empty((self._chunkSize + 1, 2))
        self._ptr = 0

    def update(self):
        now = pg.ptime.time()
        for c in self._curves:
            c.setPos(-(now - self._startTime), 0)

        i = self._ptr % self._chunkSize
        if i == 0:
            curve = self._p.plot(pen='g')
            self._curves.append(curve)
            last = self._data[-1]
            self._data[0] = last
            while len(self._curves) > self._maxChunks:
                c = self._curves.pop(0)
                self._p.removeItem(c)
        else:
            curve = self._curves[-1]
        self._data[i + 1, 0] = now - self._startTime
        self._data[i + 1, 1] = np.random.normal()
        curve.setData(x=self._data[:i + 2, 0], y=self._data[:i + 2, 1])
        self._ptr += 1


    def run(self):
        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)

        QtGui.QApplication.instance().exec_()



# class ExecutePlot(multiprocessing.Process):
#     def __init__(self, dataQueue, plotData):
#         super(ExecutePlot, self).__init__()
#         # self.dataQueue = dataQueue
#         self.plotData = plotData
#         timer = pg.QtCore.QTimer()
#         timer.timeout.connect(self.plotData.update)
#         timer.start(10)
#
#     def run(self):
#         # The following line is repeated as a loop (use as a process)
#         QtGui.QApplication.instance().exec_()
#         print('allo')


if __name__ == '__main__':
    lock = Lock()

    q = Queue(maxsize=10)
    p = PlotData(q)
    p.run()
    # e = ExecutePlot(q, p)
    # c = CreateData(q)

    # e.start()
    # e.run()
    # e.join()



