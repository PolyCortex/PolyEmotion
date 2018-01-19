#%% TEST_outlet
from random import random as rand
from pylsl import StreamInfo, StreamOutlet
import time
from math import pi, sin

info = StreamInfo('BioSemi', 'EEG', 8, 100, 'float32', 'myuid34234')
outlet = StreamOutlet(info)

i = 0.0
rep_time = 100
print("now sending data...")
while True:
    if i == rep_time: 
        i = 0.0

    time.sleep(0.004)
#    mysample = [rand(), rand(), rand(), rand(), 
#                rand(), rand(), rand(), rand()]
    sinus = sin(i/rep_time * 2 * pi)
    mysample = [sinus, rand(), sinus, rand(),
                sinus, sinus, sinus, sinus]
    outlet.push_sample(mysample)
    
#    print(sinus)
    i += 1



