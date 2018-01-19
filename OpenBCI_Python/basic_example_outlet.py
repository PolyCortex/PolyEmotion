#%% TEST_outlet
from random import random as rand
from pylsl import StreamInfo, StreamOutlet
import time
from math import pi, sin

info = StreamInfo('BioSemi', 'EEG', 8, 250, 'float32', 'myuid34234')
outlet = StreamOutlet(info)

i = 0.0
rep_time = 250
print("now sending data...")
while True:
    if i == rep_time: 
        i = 0.0

    time.sleep(0.004)
    
    sinus = sin(i/rep_time * 2 * pi)
    if 239 < i < 249: 
        mysample = [2, 2, 2, 2,
                    2, 2, 2, 2]
    else: 
        mysample = [sinus, rand(), sinus, rand(),
            sinus, sinus, rand(), sinus]
    outlet.push_sample(mysample)
    
    i += 1



