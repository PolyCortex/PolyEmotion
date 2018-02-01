from pylsl import StreamInlet, resolve_stream, resolve_byprop
# Sauvegarder dans des .csv avec tag: 
import pandas as pd
import numpy as np
import time

print("looking for a stream...")
streams_eeg = resolve_byprop('type', 'EEG', timeout=2)
marker_streams = resolve_byprop('type', 'Markers', timeout=20) # wait 2s for a stream
# Create a new inlet to read from the stream
inlet_eeg = StreamInlet(streams_eeg[0])
inlet_marker = StreamInlet(marker_streams[0])

# =============================================================================
# SAVE DATA TO CSV FILE
# =============================================================================
file_name = 'eeg_data.csv'
eeg_data = {'timestamps': [], 'ch1':[], 'ch2':[], 'ch3':[], 'ch4':[],
                              'ch5':[], 'ch6':[], 'ch7':[], 'ch8':[],
                              'marker':[]}
timeInit = float(time.time())

def save_data_frame(eeg_data, fileName):
    dataFrame = pd.DataFrame(eeg_data, columns=['timestamps', 'ch1', 'ch2',
                                                'ch3', 'ch4', 'ch5', 'ch6',
                                                'ch7', 'ch8', 'marker'])
    dataFrame.to_csv(fileName)
    print('saved {fileName}.csv file'.format(fileName=fileName))

# =============================================================================
# APPEND VALUE TO DATA DICTIONNARY
# =============================================================================

def append_value_to_data_dictionnary(samples):
    for channel_num, sample in enumerate(samples):
        key = 'ch{}'.format(str(channel_num+1))
        eeg_data[key].append(sample)
       
# =============================================================================
# STREAM LSL
# =============================================================================

for i in range(20000): 
    time.sleep(0.001) # use only if its the test with the random samples
    print(i)
    # eeg
    samples_eeg, timestamp_eeg = inlet_eeg.pull_sample(timeout=1.0)
    print('EEG: ', timestamp_eeg, [round(samp) for samp in samples_eeg])
    eeg_data['timestamps'].append(timestamp_eeg)
    append_value_to_data_dictionnary(samples_eeg)
    # marker
    samples_marker, timestamp_marker = inlet_marker.pull_sample(timeout=0.0)
    if timestamp_marker:
        print('MARKER: ', timestamp_marker, samples_marker[0])
        eeg_data['marker'].append(samples_marker[0])
    else: 
        eeg_data['marker'].append(0)   # No visual event
        
    
save_data_frame(eeg_data, file_name)
    
    
#%% TEST (how to play a mp4 video)

#import cv2
#
#cap = cv2.VideoCapture("Joel Grus - Advent of Livecoding - 2017 Day 25.mp4")
#ret, frame = cap.read()
#while(1):
#   ret, frame = cap.read()
#   cv2.imshow('frame',frame)
#   if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
#       cap.release()
#       cv2.destroyAllWindows()
#       break
#   cv2.imshow('frame',frame)