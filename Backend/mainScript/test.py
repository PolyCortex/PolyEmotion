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


class PlotData:
    """
    Ploting data with pyqtgraph under a class format
    """
    def __init__(self):
        self._win = pg.GraphicsWindow()
        self._win.setWindowTitle('....')

        self._chunkSize = 100
        self._maxChunks = 10
        self._startTime = pg.ptime.time()
        self._win.nextRow()
        self._p = self._win.addPlot(colspan=2)
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
            curve = self._p.plot()
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


p = PlotData()

timer = pg.QtCore.QTimer()
timer.timeout.connect(p.update)
timer.start(10)


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
