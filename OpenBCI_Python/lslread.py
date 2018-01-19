"""Example program to show how to read a multi-channel time series from LSL."""
#from pylsl import StreamInlet, resolve_stream
#import numpy as np
#from collections import deque
#import matplotlib.pyplot as plt
#
## first resolve an EEG stream on the lab network
#print("looking for an EEG stream...")
#streams = resolve_stream('type', 'EEG')
#
## create a new inlet to read from the stream
#inlet = StreamInlet(streams[0])
#eeg_queue =  deque(np.zeros(100))
#
#while True:
#    # get a new sample
#    sample, timestamp = inlet.pull_sample()
#    print(timestamp, sample)
#    # Show received data (and show only one channel: here channel 0)
#    eeg_queue.appendleft(sample[0])
#    eeg_queue.pop()
#    plt.scatter(range(len(eeg_queue)), eeg_queue)
#    plt.clf()
    #TODO Voir Trello (OpenBCI)


#%%

## (ALEXM): TODO: try with this code after because it is a more efficient version for eeg
#
#
#"""Example program to demonstrate how to read a multi-channel time-series
#from LSL in a chunk-by-chunk manner (which is more efficient)."""
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
import numpy as np
import matplotlib.animation as animation
from collections import deque
import time

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
d = deque(np.zeros(100))

all_eeg = []
time_init = time.time()
while time.time() - time_init < 5: 
    chunk, timestamps = inlet.pull_sample()
    if timestamps: 
        print('chunk: ', chunk)
        all_eeg.append(chunk)
        print(len(all_eeg))

#%%
all_eeg = np.array(all_eeg)
#np.savetxt('all_eeg.csv', np.array(all_eeg), delimiter=',' )
for i in range(all_eeg.shape[1]): 
    plt.figure(i)
    # Use int(len(all_eeg) * 0.2) avoid showing the noise at the beginning
    plt.plot(all_eeg[int(len(all_eeg) * 0.2):, i])
    plt.plot()


#%%
plt.plot(all_eeg[:, 0])
plt.plot()

#%%






#    if timestamps: # si on reçoit de l'information
#        cnt += 1
#        print(cnt)
#        buf.append(chunk[0])
#        if cnt % 10 == 0:
#            print('average: ', sum(buf)/len(buf))
#            print('---------------------')
#            buff = []

#        print(chunk)

#        for i, (timestamp, EEG_seq) in enumerate(zip(timestamps, chunk)):
#            if FIRST_TIMESTAMP:
#                init_time = timestamp
#                FIRST_TIMESTAMP = False
#            print(i)
#            print('timestamps', timestamp - init_time)
#            print(EEG_seq)
#



    #        ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8 =  EEG_seq
    #        print('timestamp', timestamp)
    #        print('ch1', round(ch1), 'ch2', round(ch2), 'ch3', round(ch3),
    #              'ch4', round(ch4), 'ch5', round(ch5), 'ch6', round(ch6),
    #              'ch7', round(ch7), 'ch8', round(ch8))

    #        print('chunk_len: ', len(chunk))
    #        print('\n')
    #        for one_eeg in chunk:

                # Create a small scrolling graph with a single EEG value
    #        print(chunk[0][0])
    #        d.appendleft(chunk[0][0])
    #        d.pop()
    #        print(d)
    #        plt.scatter(range(len(d)), d)
    #        plt.clf()

 #%%
import numpy as np
a = [1,2,3,4,5]
b = [6,6,6,6,6]
c = [1,1,1,1,1]
x = []
x.append(a)
x.append(b)
x.append(c)
x = np.array(x)
np.savetxt('all_eeg.csv', x, delimiter=',')



#%% PLOTING the EEG data
# Graph the data
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
app = QtGui.QApplication([])

N_DATA = 500
win = pg.GraphicsWindow()
win.setWindowTitle('EEG scrolling plot')

# For the EEG feed
from pylsl import StreamInlet, resolve_stream
import numpy as np
from collections import deque
import time

# inlet variables
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

p1 = win.addPlot()
data1 = deque(np.zeros(N_DATA), maxlen=N_DATA)
curve1 = p1.plot(data1)
def update():
    global data1, curve1
    chunk, timestamps = inlet.pull_sample()
    if timestamps:
        print(timestamps)
        data1.append(chunk[1])
        curve1.setData(data1)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(3)

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()



