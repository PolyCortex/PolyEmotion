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
               timestamps_and_eeg.T, delimiter=',' )                           # TODO: use pickle.dump instead

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










