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

    sinus1 = sin(10 * 2 * pi * i/rep_time)
    sinus2 = sin(20 * 2 * pi * i/rep_time)
    if 239 < i < 249:
        mysample = [sinus2, sinus1+2 * sinus2, 3, 4,
                    2, 2, 2, 2]
    else:
        mysample = [sinus2, sinus1 + sinus2, sinus1, rand(),
                    sinus1, sinus1, rand(), sinus1]
    outlet.push_sample(mysample)

    i += 1


#%% TEST fft ploting  TODO: (ALEX)




