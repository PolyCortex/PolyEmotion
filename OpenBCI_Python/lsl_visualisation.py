# -*- coding: utf-8 -*-
"""
Created on Friday Jan 26 00:34:23 2018

@author: Alexandre Marcotte
"""
#%% ***************************************************************************
# =============================================================================
# TO TEST THE CODE RUN basic_example_outlet.py AND THEN THIS CODE SO THAT YOU HAVE RANDOM SAMPLES TO PLOT
# =============================================================================
# *****************************************************************************
#%% PLOTING the EEG data
# Pyqtgraph related functions
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
app = QtGui.QApplication([])
# For the EEG feed
from pylsl import StreamInlet, resolve_stream
from collections import deque
# To create a frequency plot 
import scipy.fftpack

# ----Initialisation of inlet object----                                       # TODO: for the real program this needs to be remove and replace by the values of the callback function
streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])


class EEG_viewer(object): 
    
    def __init__(
            self, 
            N_DATA=500, 
            N_CH=8,
            PLOT_FREQ=True,
            CH_GRAPH_TO_PLOT='ALL',
            PLOT_1_EVERY=10):
        """
        Attributes: 
            
        N_DATA : int
            the number of sample contain on the x axis of the graph
        N_CH : int
            the number of channel to plot on the graph
        plt : 
        data : 
        curve : 
        update_ch_functs : 
        win : 
            A Pyqtgraph window object
        PLOT_FREQ : bool
            A bool to toggle if you want or not to plot the freq graph
        freq_plot : 
        """
        self.N_DATA = N_DATA
        self.N_CH = N_CH
        # show only certain graph you want to plot
        self.CH_GRAPH_TO_PLOT = CH_GRAPH_TO_PLOT
        # frequence of the ploting 
        self.PLOT_1_EVERY=PLOT_1_EVERY # frequence impose                      # TODO find a way to have a frequency so that we don't lag behind
        self.plot_1_every=0            # loop over
        # initialize arrays required to show all channels
        self.plt = [[]] * self.N_CH
        self.data = [None] * self.N_CH
        self.curve = [None] * self.N_CH
        # create a LIST OF UPDATE FUNCTIONS to control every channel graph
        self.update_ch_functs = [self.update_one_ch_func] * self.N_CH
        # -------Create pyqt objects-------
        # window
        self.win = self.init_window()
        # freq_plot
        self.PLOT_FREQ = PLOT_FREQ
        self.freq_plot, self.freq_data, self.freq_curve = self.init_freq_plot()
        self.init_title_axis_data_curve()

    def init_window(self): 
        """
        Creation of a pyqtgraph window object
        
        Returns: 
            
            win : pyqtgraph window object
        """
        win = pg.GraphicsWindow()
        win.setWindowTitle('Visualisation of OPENBCI signals widget')
        win.useOpenGL()
        return win
    
    def init_freq_plot(self): 
        """
        frequency plot initialization
        
        Returns: 
            freq_plot : 
            freq_data : 
            freq_curve : 
        """
        freq_plot = self.win.addPlot(rowspan=4, row=4, col=1)
        freq_plot.setLabel('bottom', 'Frequency', 'hz')
        freq_plot.setTitle('FFT for all channels')
        freq_plot.showGrid(x=True, y=True, alpha=0.5)
        freq_data = deque(np.zeros(self.N_DATA), maxlen=self.N_DATA)
        freq_curve = freq_plot.plot(freq_data)
        return freq_plot, freq_data, freq_curve
    
    def init_title_axis_data_curve(self): 
        """
        Create all the  8 plots
        """
        for ch_no in range(self.N_CH):
            # add each channel plot one under the other on the same colonne
            self.plt[ch_no] = self.win.addPlot(row=ch_no, col=0)
            # add axis labels
            self.plt[ch_no].setLabel('left', 'ch {ch_no}'.format(ch_no=ch_no))
            # write the title only over the first channel
            if ch_no == 0:
                self.plt[ch_no].setTitle("""Electrical amplitude of the signal 
                                    for the 8 channels of the OPENBCI""")
            # write the axis label only under the last channel
            if ch_no == self.N_CH - 1:
                self.plt[ch_no].setLabel('bottom', 'Time', 's')
            # add a grid
            self.plt[ch_no].showGrid(x=True, y=True, alpha=0.3)
            # initialize data and curve                                        # TODO: look more into this
            self.data[ch_no] = deque(np.zeros(self.N_DATA), maxlen=self.N_DATA)
            self.curve[ch_no] = self.plt[ch_no].plot(self.data[ch_no])

    def update_freq_plot(
            self, 
            sample):
        """
        Create a frequency plot on the right side of the window
        
        Parameters:
            
        sample : list -> [ch_1, ch_2, .... ch_N_CH]   
            A list containing the channel value for all channels for
            one specific timestamp
        """
        self.freq_data.append(sample)
        # find the FFT of the one of the channel
        yf = scipy.fftpack.fft(self.freq_data)
        # set x axis
        xf = np.linspace(0.0, 250.0, len(self.freq_data)//2)
        self.freq_plot.setRange(xRange=xf)
        # set y data
        self.freq_curve.setData(2.0/len(self.freq_data) \
                             * np.abs(yf[:len(self.freq_data)//2]))
    
    def update_one_ch_func(
            self,
            sample, 
            ch_no):
        """
        Update a single channel
        
        Parameters:

        sample : list -> [ch_1, ch_2, .... ch_N_CH]
            A list containing the channel value for all channels for
            one specific timestamp
        ch_no : int
            The number of the channels that is updated
        """
        self.plt[ch_no].setLabel('right',
            '{mean_ampl:.2f} uVrms'\
            .format(mean_ampl=np.mean(self.data[ch_no])))
        self.data[ch_no].append(sample)
        self.curve[ch_no].setData(self.data[ch_no])
          
    def update_all(
            self):
        global inlet
        """Update the graph for the 8 signals (one for each signal channel)"""
        samples, timestamp = inlet.pull_sample()
        # update only if the pull contains a value
        print('timestamp: ', timestamp)
        if timestamp and self.plot_1_every==self.PLOT_1_EVERY:                 # Find a cleaner way to stay on track of the ploting (and plot data depending of the timestamp)
            print('---------------------')
            self.plot_1_every=0                                                # Like that we are sure that we are never lagging behind (but the jump between the samples is variable)
            # Update the 8 signal channels                                     # Or should there be a variable sample rate base on the lagg
            for ch_no in range(self.N_CH): 
                # Update only certain graph to have a faster rendering possible
                if self.CH_GRAPH_TO_PLOT == 'ALL' or ch_no in self.CH_GRAPH_TO_PLOT:   # or use the downsampling parameter
                    self.update_ch_functs[ch_no](samples[ch_no], ch_no)
            # Update the frequency plot  (only for the second channel)         # TODO: explain why the if is present there 
            if self.PLOT_FREQ: 
                self.update_freq_plot(samples[1])
        self.plot_1_every += 1


#--------main-----------
# Create a eeg viewer object
my_eeg_viewer = EEG_viewer(PLOT_FREQ=True, PLOT_1_EVERY=10, 
                           CH_GRAPH_TO_PLOT = [0,1,2,6])
# pyqtgraph events
timer = pg.QtCore.QTimer()
timer.timeout.connect(my_eeg_viewer.update_all)
timer.start(0) # The argument is the frequency of update



# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
        
        











# =============================================================================# TODO: Try to implement qt push button
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

