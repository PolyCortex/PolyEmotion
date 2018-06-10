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
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('....')

        self.chunkSize = 100
        self.maxChunks = 10
        self.startTime = pg.ptime.time()
        self.win.nextRow()
        self.p5 = self.win.addPlot(colspan=2)
        self.p5.setLabel('bottom', '...', '...')
        self.p5.setXRange(-10, 0)
        self.curves = []
        self.data5 = np.empty((self.chunkSize + 1, 2))
        self.ptr5 = 0

    def update(self):
        now = pg.ptime.time()
        for c in self.curves:
            c.setPos(-(now - self.startTime), 0)

        i = self.ptr5 % self.chunkSize
        if i == 0:
            curve = self.p5.plot()
            self.curves.append(curve)
            last = self.data5[-1]
            self.data5[0] = last
            while len(self.curves) > self.maxChunks:
                c = self.curves.pop(0)
                self.p5.removeItem(c)
        else:
            curve = self.curves[-1]
        self.data5[i + 1, 0] = now - self.startTime
        self.data5[i + 1, 1] = np.random.normal()
        curve.setData(x=self.data5[:i + 2, 0], y=self.data5[:i + 2, 1])
        self.ptr5 += 1


p = PlotData()

timer = pg.QtCore.QTimer()
timer.timeout.connect(p.update)
timer.start(10)


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
