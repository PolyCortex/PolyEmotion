import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
import numpy as np
from collections import deque
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
    """
    print("Looking for an EEG stream...")
    # Create a new inlet to read from the outlet stream
    streams = resolve_stream('type', 'EEG')
    inlet = StreamInlet(streams[0])
    # Initialisation of values
    all_eeg = []
    time_init = time.time()
    # Collect data for the duration of the experiment
    while time.time() - time_init < EXPERIMENT_TIME:
        sample, timestamp = inlet.pull_sample()
        if timestamp:
            if DO_PRINT_SAMPLE:
                print('chunk: ', sample)
            all_eeg.append(sample)
    # Show the data for all the cython chanels 
    all_eeg = np.array(all_eeg)
    if SHOW_PLT_DATA: 
        for i in range(all_eeg.shape[1]): 
            plt.figure(i)
            # Use int(len(all_eeg) * 0.2) avoid showing the noise at the beginning      NOTE: this should be remove if real testing
            plt.plot(all_eeg[int(len(all_eeg) * 0.2):, i])
            plt.plot()
    # Save as csv
    np.savetxt('{SAVE_FILE_NAME}.csv'.format(SAVE_FILE_NAME=SAVE_FILE_NAME),
               np.array(all_eeg), delimiter=',' )
    
    return all_eeg


all_eeg = record_to_CSV_experiment_data(EXPERIMENT_TIME=5, 
                                        SAVE_FILE_NAME='record_test',
                                        SHOW_PLT_DATA=True,
                                        DO_PRINT_SAMPLE=True)

#%% Show the data for all the cython chanels    

for i in range(all_eeg.shape[1]): 
    plt.figure(i)
    # Use int(len(all_eeg) * 0.2) avoid showing the noise at the beginning      NOTE: this should be remove if real testing
    plt.plot(all_eeg[int(len(all_eeg) * 0.2):, i])
    plt.plot()

#%% PLOTING the EEG data
# Graph the data
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
app = QtGui.QApplication([])

N_DATA = 1000
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

# CREATE PLOTS FOR ALL 8 CHANNELS
# initialise list required for ploting

# =============================================================================
# Create 8 scrolling plot at the left of the screen to display all channels
# =============================================================================
# Initialize the differents array required to show all channels
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
    if i == 7: 
        p[i].setLabel('bottom', 'Time', 's')
        
    data[i] = deque(np.zeros(N_DATA), maxlen=N_DATA)
    curve[i] = p[i].plot(data[i])
    def update(sample, timestamp, i):
        global curve
        data[i].append(sample)
        curve[i].setData(data[i])
    # Use the property of first member citizen of functions
    update_func.append(update)
    

# =============================================================================
# Create a frequency plot on the side   
# =============================================================================
#from numpy.fft import fft
p_freq = win.addPlot(rowspan=4, col=1)
p_freq.setLabel('bottom', 'Frequency', 'hz')
data_freq = deque(np.zeros(N_DATA), maxlen=N_DATA)
curve_freq = p_freq.plot(data_freq)
def update_freq_plot(sample, timestamp):  
    global curve_freq
    data_freq.append(sample)
#    data_fft = fft(data_freq)
    curve_freq.setData(data_freq)
    
# FOR 8 PLOTS (one for each signal channel)
def update():
    global inlet
    # Using chunk to avoid laging behind time by having a displaying rate 
    # lower than the sampling rate
    chunk, timestamps = inlet.pull_chunk()
    if timestamps: 
        samples = chunk[-1]  # keeping only the last element of the chunk that
                             # can have different size                         # TODO: (ALEX) would be better to have process in parallel
        timestamp = timestamps[-1]
        for i in range(N_SIGNALS): 
            update_func[i](samples[i], timestamp, i) 
        
        update_freq_plot(samples[0], timestamp)


# CREATE ONLY ONE PLOT
"""
p1 = win.addPlot()
data1 = deque(np.zeros(N_DATA), maxlen=N_DATA)
curve1 = p1.plot(data1)
def update():
    global data1, curve1
    chunk, timestamp = inlet.pull_chunk()

    if timestamp:
        print('_______________________')
        print('timestamp: ', timestamp)
        print('chunk: ', chunk)
        data1.append(chunk[-1][0])
        curve1.setData(data1)
"""

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1)

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()






