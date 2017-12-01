"""Example program to show how to read a multi-channel time series from LSL."""
from pylsl import StreamInlet, resolve_stream
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
eeg_queue =  deque(np.zeros(100))

while True:
    # get a new sample 
    sample, timestamp = inlet.pull_sample()
    print(timestamp, sample)
    # Show received data (and show only one channel: here channel 0)
    eeg_queue.appendleft(sample[0])
    eeg_queue.pop()
    plt.scatter(range(len(eeg_queue)), eeg_queue)
    plt.clf()
    #TODO Voir Trello (OpenBCI)
    
    
   
    
    
#%%
    
## (ALEXM): TODO: try with this code after because it is a more efficient version for eeg
#
#
#"""Example program to demonstrate how to read a multi-channel time-series
#from LSL in a chunk-by-chunk manner (which is more efficient)."""   
import matplotlib.pyplot as plt
#from pylsl import StreamInlet, resolve_stream
import numpy as np
import matplotlib.animation as animation
from collections import deque

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
d = deque(np.zeros(100))
    
while True:
    # get a new sample
    chunk, timestamps = inlet.pull_chunk()
    if timestamps:    # TODO: sert a quoi ????
        print(chunk)
#        for one_eeg in chunk:
#            d.appendleft(one_eeg)
#            d.pop()
#            plt.scatter(range(len(d)), d)
#            plt.clf()
            
#    
            


