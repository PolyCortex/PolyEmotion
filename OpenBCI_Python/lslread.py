# -*- coding: utf-8 -*-
#%% # TODO: (ALEX)
"""
1. Remove thie file from the OPENBCI files and add the path to the required
   files so that the interpreter still can reach them

"""
#%%
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
import numpy as np
import time

def record_to_CSV_experiment_data(
        EXPERIMENT_TIME=5,
        SAVE_FILE_NAME='recorded_signal_data',
        SHOW_PLT_DATA=False,
        DO_PRINT_SAMPLE=False):
    """
    Resolve a pylsl stream coming from the plugin streamer lsl that can be
    activate by starting the user.py function (in OPENBCI) with the command
    -add (ex: for Windows:  python user.py -p=COM3 --add streamer_lsl).
    Then append this data to a list that is converted to a numpy array
    to then save as a CSV file

    Parameters:
        EXPERIMENT_TIME : int
            The duration of streaming of the electrical signal
        SAVE_FILE_NAME : str
            The name of the file where you want to save the electrical
            signal data
        SHOW_PLT_DATA : bool
            To indicate if you want to plot the acquired data with matplotlib
        DO_PRINT_SAMPLE : bool
            Toggle this bool if you want to show all the pulled sample
    Returns:
        all_eeg : np.array
            Array containing all the 8 channel data recorded from the
            OPENBCI board. These are the same value saved by the function
            in the CSV file
        timestamps : np.array
            Array containing the timestamps for all the acquiered signal values
    """
    print("Looking for an EEG stream...")
    # Create a new inlet to read from the outlet stream
    streams = resolve_stream('type', 'EEG')
    inlet = StreamInlet(streams[0])
    # Initialisation of values
    all_eeg = []
    timestamps = []
    time_init = time.time()
    # Collect data for the duration of the experiment
    while time.time() - time_init < EXPERIMENT_TIME:
        sample, timestamp = inlet.pull_sample()
        if timestamp:
            if DO_PRINT_SAMPLE:
                print('chunk: ', sample)
            timestamps.append(timestamp)
            all_eeg.append(sample)
    # Show the data for all the cython chanels
    all_eeg = np.array(all_eeg)
    timestamps = np.array(timestamps)
    timestamps_and_eeg = np.concatenate((all_eeg.T, timestamps[:,None].T))
    # Show matplotlib of the acquiered data
    if SHOW_PLT_DATA:
        for i in range(all_eeg.shape[1]):
            plt.figure(i)
            # Use int(len(all_eeg) * 0.2) avoid showing the noise
            # at the beginning                                                 # HINT: this should be remove if real testing
            plt.plot(all_eeg[int(len(all_eeg) * 0.2):, i])
            plt.plot()
    # Save as csv
    np.savetxt('{SAVE_FILE_NAME}.csv'.format(SAVE_FILE_NAME=SAVE_FILE_NAME),
               timestamps_and_eeg.T, delimiter=',' )

    return timestamps, all_eeg


timestamps, all_eeg = record_to_CSV_experiment_data(EXPERIMENT_TIME=1,
                                                    SAVE_FILE_NAME='record_test',
                                                    SHOW_PLT_DATA=True,
                                                    DO_PRINT_SAMPLE=True)

#%% Implement a code to show the FFT of a signal (matplotlib)
# See: https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

## Number of samplepoints
#N = 600
## sample spacing
#T = 1.0 / 800.0
#x = np.linspace(0.0, N*T, N)
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
y = all_eeg[:, 1]

yf = scipy.fftpack.fft(y)

xf = np.linspace(0.0,
                 250, # ????: 1.0/2 * freq d'échantillonage
                 len(y)//2) # Utiliser la moitié pour ne pas répéter la symétrie
plt.plot(xf, 2.0/len(y) * np.abs(yf[:len(y)//2])) # ????: Facteur est pour normaliser?

plt.show()



#%% PLOTING the EEG data
# Graph the data
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
app = QtGui.QApplication([])
# For the EEG feed
from pylsl import StreamInlet, resolve_stream
import numpy as np
from collections import deque
import time

# inlet variables
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

win = pg.GraphicsWindow()
win.setWindowTitle('Visualisation of OPENBCI signals widget')
win.useOpenGL()
# =============================================================================
# Create 8 scrolling plot at the left of the screen to display all channels
# =============================================================================
# Initialize the differents array required to show all channels
N_DATA = 500
N_SIGNALS = 8
p = [[]] * N_SIGNALS
data = [None] * N_SIGNALS
curve = [None] * N_SIGNALS
update_func = []
# Create all the  8 plots
for i in range(N_SIGNALS):
    p[i] = win.addPlot(row=i, col=0)
    # add axis labels
    p[i].setLabel('left', 'ch {i}'.format(i=i))
    if i == 0:
        p[i].setTitle("""Electrical amplitude of the signal for the 8 channels
                       of the OPENBCI""")
    if i == 7:
        p[i].setLabel('bottom', 'Time', 's')
    p[i].showGrid(x=True, y=True, alpha=0.3)

    data[i] = deque(np.zeros(N_DATA), maxlen=N_DATA)
    curve[i] = p[i].plot(data[i])
    def update(sample, timestamp, i):
        global curve
        p[i].setLabel('right',
                      '{mean_ampl:.2f} µVrms'.format(mean_ampl=np.mean(data[i])))      # TODO: verifier l'unité
        data[i].append(sample)
        curve[i].setData(data[i])
    # Use the property of first member citizen of functions
    update_func.append(update)

# =============================================================================
# Create a frequency plot on the side
# =============================================================================
import scipy.fftpack
p_freq = win.addPlot(rowspan=4, row=4, col=1)
p_freq.setLabel('bottom', 'Frequency', 'hz')
p_freq.setTitle('FFT for all channels')
p_freq.showGrid(x=True, y=True, alpha=0.5)
data_freq = deque(np.zeros(N_DATA), maxlen=N_DATA)
curve_freq = p_freq.plot(data_freq)
def update_freq_plot(sample, timestamp):
    global curve_freq
    data_freq.append(sample)
    yf = scipy.fftpack.fft(data_freq)
    # Set x axis
    xf = np.linspace(0.0, 250.0, len(data_freq)//2)
    p_freq.setRange(xRange=xf)
    curve_freq.setData(2.0/len(data_freq) * np.abs(yf[:len(data_freq)//2]))

# =============================================================================
# Add a dock with some button widgets
# =============================================================================
"""
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
from pyqtgraph.dockarea import *

d1 = Dock("Dock1", size=(1, 1))     ## give this dock the minimum possible size
area.addDock(d1, 'right')
d1 = Dock("Dock6 (tabbed) - Plot", size=(500,200))
w1 = pg.LayoutWidget()
label = QtGui.QLabel(' -- DockArea Example --')
w1.addWidget(label, row=0, col=1)
d1.addWidget(w1)
"""

# =============================================================================
#  UPDATE the graph for the 8 signals (one for each signal channel)
# =============================================================================
num_itt = 0
def update():
    global inlet, num_itt
    # Using chunk to avoid laging behind time by having a displaying rate
    # lower than the sampling rate
    DISPLAY_RATE = 5
    samples, timestamp = inlet.pull_sample()
    if timestamp and num_itt % DISPLAY_RATE == 0: # plot every 5 samples                  # ????: (ALEX) is it better to pull in chunk
        num_itt = 0                                                            # Like that we are sure that we are never lagging behind (but the jump between the samples is variable)
        # Update the 8 signal channels                                         # Or should there be a variable sample rate base on the lagg
        for i in range(N_SIGNALS):                                             # or use the downsampling parameter
            update_func[i](samples[i], timestamp, i)
        # Update the frequency plot
        if num_itt % 2 * DISPLAY_RATE == 0:
            update_freq_plot(samples[2], timestamp)
    num_itt += 1


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()






