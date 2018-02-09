import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
from collections import deque
from random import random
import time
from threading import Thread
from Queue import Queue
import dataFiller

                


# filtrer le signal
# def butter_lowpass(cutOff, fs, order=5):
#     nyq = 0.5 * fs
#     normalCutoff = cutOff / nyq
#     b, a = butter(order, normalCutoff, btype='low', analog = True)
#     return b, a
#
# def butter_lowpass_filter(data, cutOff, fs, order=4):
#     b, a = butter_lowpass(cutOff, fs, order=order)
#     y = lfilter(b, a, data)
#     return y
#
# eeg_data_filter = butter_lowpass_filter(data=eeg_data, cutOff=60, order=4)



bufferSize = 500
data = deque(np.zeros(bufferSize), maxlen=bufferSize)
plt = pg.plot()
plt.setRange(xRange=[0, bufferSize], yRange=[-60000, -53000])
curve = plt.plot()



def update():
    global data, curve, line, sample_no
    data.append(eeg_data[sample_no])
    curve.setData(data)
    sample_no += 1

timer = pg.QtCore.QTimer()

# def run():
    # timer.timeout.connect(update)
    # timer.start(4)

if __name__ == '__main__':
    import sys
    fichier = 'donne1.txt'
    queueSize = 500
    sample_no = 0
    dataQueue = Queue(queueSize)
    worker = dataFiller.fillerWorker(dataQueue, fichier)

    worker.start()
    print("on attend un peu..")
    time.sleep(2)
    worker.join()


    
    # if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    #     QtGui.QApplication.instance().exec_()
