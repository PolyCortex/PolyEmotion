import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtGui
plt = pg.plot()
plt1 = pg.plot()
bufferSize = 1000
data = np.zeros(bufferSize)
curve = plt.plot()
line = plt.addLine(x=0)
plt.setRange(xRange=[0, bufferSize], yRange=[-50, 50])
plt1.setRange(xRange=[0, bufferSize], yRange=[-50, 50])
i = 0
def update():
    global data, curve, line, i
    n = 10  # update 10 samples per iteration
    rand = np.random.normal(size=n)
    data[i:i+n] = np.clip(data[i-1] + rand, -50, 50)
    curve.setData(data)
    i = (i+n) % bufferSize
    line.setValue(i)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()