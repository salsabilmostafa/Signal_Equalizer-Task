# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
import pyqtgraph as pg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure


class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
        self.axes.set_facecolor('black')
        self.fig.patch.set_facecolor('black')
        self.axes.spines['bottom'].set_color('white')
        self.axes.tick_params(axis='x', colors='white')
        self.axes.spines['left'].set_color('white')
        self.axes.tick_params(axis='y', colors='white')
    # def plot_specgram(self, data, Fs):
    #     power_spectrum, frequencies_found, _, image_axis = self.axes.specgram(data, Fs=Fs)
    #     self.draw()

# Matplotlib widget
# Ensure using PyQt5 backend

# Matplotlib widget


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def plot_spectrogram(self, data, sample_rate, ecg):
        # Compute the spectrogram
        spectrogram, freq, time, im = plt.specgram(data, Fs=sample_rate)

        # Clear the previous plot
        self.figure.clear()

        # Create a new axis for the spectrogram plot
        ax = self.figure.add_subplot(111)

        if ecg == True:
            # Plot the spectrogram with frequency on the y-axis and time on the x-axis
            im = ax.imshow(np.log(spectrogram), origin='lower', aspect='auto',
                           cmap='jet')
        elif ecg == False:
            im = ax.imshow(np.log(spectrogram), origin='lower', aspect='auto',
                           cmap='jet', extent=[time[0], time[-1], freq[0], freq[-1]])

        # Set the labels and title
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Frequency (Hz)')
        ax.set_title('Spectrogram')

        # # Add colorbar
        # cbar = self.figure.colorbar(im)
        # cbar.set_label('Intensity (dB)')

        # Redraw the canvas
        self.canvas.draw()
