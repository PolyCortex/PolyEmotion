import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
from collections import deque
from random import random
import time
from threading import Thread
from Queue import Queue
import dataFiller
import dataPlotter
import multiprocessing
from multiprocessing import Process
                

if __name__ == '__main__':
    import sys
    fichier = 'donne1.txt'
    dataQueue = multiprocessing.Queue()


    pFiller = dataFiller.fillerWorker(dataQueue, fichier)
    pConsumer = dataPlotter.plotterWorker(dataQueue)
    pFiller.start()
    pConsumer.start()



    print("on attend un peu..")
    time.sleep(5)
    pFiller.join()
    pConsumer.join()
    

    
   
            
    #if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
   
    

    

