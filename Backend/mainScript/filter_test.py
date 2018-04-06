import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class FilterData:
    def __init__(self, filt_order, filt_cutoff, filt_type):
        self.order = filt_order
        self.cutoff = filt_cutoff
        self.type = filt_type

low_pass_butter_data = FilterData(4,100,'low')
high_pass_butter_data = FilterData(4,1,'high')

filters_data = [low_pass_butter_data, high_pass_butter_data]

for i,filt in enumerate(filters_data,1):
    # Pour générer les filtres
    b,a = signal.butter(filt.order,filt.cutoff,filt.type,analog=True)
    
    # Affichage du diagramme en fréquence des filtres
    w, h = signal.freqs(b, a)
    plt.subplot(2,1,i)
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(filt.cutoff, color='green')

plt.show()