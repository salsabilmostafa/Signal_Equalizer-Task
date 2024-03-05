from datetime import datetime
import numpy as np
import pyqtgraph as pg
import pandas as pd
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import time
from scipy.fft import fft, rfft
from scipy.fft import fftfreq, rfftfreq
from scipy.io import wavfile
import sys
import os
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioFormat, QMediaResource, QAudioBuffer
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QBuffer, QIODevice
import wfdb
# import app_framework as af
import matplotlib
from PyQt5 import QtWidgets
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from mplwidget import MplWidget
import matplotlib.pyplot as plt
# import mplwidget


x_values = []
y_values = []
timer = None
max_data_points = 0
Xplotted = 0
Xplotted2 = 0
x1 = []
y1 = []
y2 = []
x2 = []
x1_values = []
y1_values = []
plot_iteration = 0
timer = QtCore.QTimer()
signal = []
audio_data = []
running = True
current_tab_index = 0
new_mag = []
ecg = False
wav = False
output_filename = None
file_path = 0
slider_range = []
Smoothing_Mode = False
sample_rate = 0
# scaled_data = []


def update_current_tab_index(self, index):
    global current_tab_index
    # Store the current tab index in a variable for later use
    current_tab_index = index


def zoom_in(self):
    current_range = self.Input_Graph.viewRange()
    self.Input_Graph.setXRange(
        current_range[0][0] * 0.9, current_range[0][1] * 0.9, padding=0)
    self.Input_Graph.setYRange(
        current_range[1][0] * 0.9, current_range[1][1] * 0.9, padding=0)

    current_range2 = self.Output_Graph.viewRange()
    self.Output_Graph.setXRange(
        current_range2[0][0] * 0.9, current_range2[0][1] * 0.9, padding=0)
    self.Output_Graph.setYRange(
        current_range2[1][0] * 0.9, current_range2[1][1] * 0.9, padding=0)


def zoom_out(self):
    current_range = self.Input_Graph.viewRange()
    current_range2 = self.Output_Graph.viewRange()

    self.Input_Graph.setXRange(
        current_range[0][0] * 1.1, current_range[0][1] * 1.1, padding=0)
    self.Input_Graph.setYRange(
        current_range[1][0] * 1.1, current_range[1][1] * 1.1, padding=0)

    self.Output_Graph.setXRange(
        current_range2[0][0] * 1.1, current_range2[0][1] * 1.1, padding=0)
    self.Output_Graph.setYRange(
        current_range2[1][0] * 1.1, current_range2[1][1] * 1.1, padding=0)


def browsefiles(self):
    global x_values, y_values, timer, max_data_points, signal, x1_values, y1_values, audio_data, file_path, original_data_x, original_data_y, ecg, wav, y1, sample_rate

    file_path, _ = QFileDialog.getOpenFileName(
        None, caption='Open File', directory='Task1DSP')

    if file_path:
        file_extension = file_path.split('.')[-1].lower()

        Normal_Ecg = 'ecg-id-database-1.0.0'
        Arrhythmia_1 = 'Sinus Rhythm'
        Arrhythmia_2 = 'Myocardial infarction'
        Arrhythmia_3 = 'Atrial Fibrillation'
        if file_extension != 'wav':
            ecg = True
            if Normal_Ecg in file_path:
                self.ECG = 1
                record_data, record_fields = wfdb.rdsamp(
                    file_path[:-4], channels=[1])
            elif Arrhythmia_1 in file_path:
                self.ECG = 2
                record_data, record_fields = wfdb.rdsamp(
                    file_path[:-4], channels=[1])
            elif Arrhythmia_2 in file_path:
                self.ECG = 3
                record_data, record_fields = wfdb.rdsamp(
                    file_path[:-4], channels=[1])
            elif Arrhythmia_3 in file_path:
                self.ECG = 4
                record_data, record_fields = wfdb.rdsamp(
                    file_path[:-4], channels=[1])
            sample_rate = record_fields['fs']
            duration = record_fields['sig_len']/sample_rate
            y1 = list(record_data[:, 0])
            # y1_modified = y1.copy()
            x1 = np.linspace(0, duration, len(y1), endpoint=False)

        elif file_extension == 'wav':
            wav = True
            self.sample_rate, audio_data = wavfile.read(file_path)
            channels = len(audio_data.shape)  # Check number of audio channels
            if channels == 1:
                # Mono audio
                self.audio_flag = "mono"
                time = np.arange(0, len(audio_data)) / self.sample_rate
                x1 = time
                y1 = audio_data  # Store the audio data in y1
                self.audio = audio_data

            elif channels == 2:
                self.audio_flag = "stereo"
                # Stereo audio - split into two channels
                time = np.arange(0, len(audio_data[:, 0])) / self.sample_rate
                x1 = time
                y1 = audio_data[:, 0]  # Separate left and right channels
                self.audio = audio_data[:, 0]
            else:
                print("Unsupported number of audio channels")
                return

        else:
            print("Unsupported file format")
            return

        if file_extension == "wav":

            # self.player = QMediaPlayer()
            self.mplWidget.plot_spectrogram(y1, self.sample_rate, ecg)
            self.mplWidget_out.plot_spectrogram(y1, self.sample_rate, ecg)
            Fourier(self, y1, x1)
        elif ecg == True:
            # Append new data to existing data arrays with a rolling buffer
            if len(x_values) > 0:
                max_data_points = max(len(x1), len(x_values[0]))
            else:
                max_data_points = len(x1)

            x_values = x_values[:max_data_points]
            y_values = y_values[:max_data_points]
            Fourier_ECG(self, y1, x1)
            original_data_y = y1
            original_data_x = x1
            self.mplWidget.plot_spectrogram(y1, sample_rate, ecg)
            self.mplWidget_out.plot_spectrogram(y1, sample_rate, ecg)

            x_values = []
            y_values = []
        x_values.insert(0, x1)
        y_values.insert(0, y1)
        self.Input_Graph.clear()
        self.Output_Graph.clear()
        # self.Input_Graph.plot(original_data_x, original_data_y, pen='r')

        if timer is None or not timer.isActive():
            setup_timer(self)


def play_audio(self):
    global output_filename, sample_rate, ecg
    if self.Input_RadioBtn.isChecked():
        media = QMediaContent(QUrl.fromLocalFile(file_path))
        self.player.setMedia(media)
        self.player.play()
        self.mplWidget_out.clear()
        self.mplWidget_out.plot_spectrogram(y1, self.sample_rate, ecg)
        print("input clicked")

    elif self.Output_RadioBtn.isChecked():
        self.player.setMedia(QMediaContent(
            QUrl.fromLocalFile(output_filename)))
        self.player.play()

        if ecg == True:
            self.mplWidget_out.plot_spectrogram(y1_values, sample_rate, ecg)
        else:
            self.mplWidget_out.plot_spectrogram(
                self.scaled_data, self.sample_rate, ecg)


def Fourier(self, y_values, x_values):
    global fourier_y, Smoothing_Mode
    if Smoothing_Mode == False:
        fourier_y = np.fft.fft(y_values)
        dt = x_values[1]-x_values[0]
        fourier_x = np.fft.fftfreq(len(fourier_y), dt)
        N = len(signal)
    else:
        fourier_y = y_values
        fourier_x = x_values
   # normalize = N/0.02
    pen = pg.mkPen('r')
    self.x_range = [0, 8000]
    self.y_range = [0, 8000]
    self.Frequency_Graph.setXRange(
        *self.x_range)

    n = len(y_values)
    self.freq = np.fft.rfftfreq(n, d=1/self.sample_rate)
    self.mag = np.abs(np.fft.rfft(y_values))
    # self.Frequency_Graph.setYRange(
    #      yMin=0, yMax=10000)
    self.Frequency_Graph.clear()
    self.Frequency_Graph.plot(fourier_x, np.abs(fourier_y), pen=pen)

    Fourier_Inverse(self)
   # min_frequency = np.min(np.abs(frequencies))
   # max_frequency = np.max(np.abs(frequencies))


def Fourier_ECG(self, y_values, x_values):
    global Smoothing_Mode, fourier_x_ecg, fourier_y_ecg, ecg
    ecg = True
    if Smoothing_Mode == False:
        # Perform Fourier transform
        fourier_y_ecg = np.fft.fftshift(np.fft.fft(y_values))
        sample_rate = 1 / (x_values[1] - x_values[0])
        dt = 1 / sample_rate
        fourier_x_ecg = np.fft.fftshift(np.fft.fftfreq(len(fourier_y_ecg), dt))
    else:
        fourier_y_ecg = y_values
        fourier_x_ecg = x_values
    # Plot the frequency spectrum
    pen = pg.mkPen('r')
    # Set the x-axis range symmetrically around zero
    self.x_range = [np.min(np.abs(fourier_y_ecg)),
                    np.max(np.abs(fourier_y_ecg))]
    # Set the y-axis range based on the maximum magnitude of the Fourier transform
    self.y_range = [0,  np.max(np.abs(fourier_y_ecg))]
    self.Frequency_Graph.setXRange(*self.x_range)
    self.Frequency_Graph.setYRange(*self.y_range)
    # Calculate a scaling factor to adjust y-values
    max_value = np.max(np.abs(fourier_y_ecg))
    desired_max_value = 5  # The desired maximum value on the y-axis
    scaling_factor = max_value / desired_max_value

    # Scale the y-values
    scaled_y_values = np.abs(fourier_y_ecg) / scaling_factor

    n = len(y_values)
    self.freq = np.fft.rfftfreq(n, d=1/sample_rate)
    self.mag = np.abs(np.fft.rfft(y_values))

    self.Frequency_Graph.plot(fourier_x_ecg, np.abs(fourier_y_ecg), pen=pen)
    Fourier_Inverse_Ecg(self, fourier_y_ecg)


def Fourier_Inverse_Ecg(self, fourier):
    global y1_values, x1_values, x_values, y_values, max_data_points, ecg, output_filename, Inversed_data_x, Inversed_data_y, original_data_x, original_data_y
    inverse_transform = np.fft.ifft(np.fft.ifftshift(fourier))
    # Store magnitude data in separate x and y arrays
    x1 = np.arange(len(inverse_transform))
    y1 = inverse_transform.real + inverse_transform.imag
    x1_values = []
    y1_values = []
    y1_values.append(y1)
    Inversed_data_y = y1
    Inversed_data_x = x1
    # self.Output_Graph.plot(Inversed_data_x,Inversed_data_y, pen='r')


def Fourier_Inverse(self):
    global output_filename, y1, y1_values
    if self.mag is not None and self.freq is not None:
        freq_ranges, count = Ranges(self)

        complex_array = np.zeros_like(
            self.mag) + 1j * np.zeros_like(self.mag)
        modified_regions = np.zeros_like(
            self.mag) + 1j * np.zeros_like(self.mag)

        if current_tab_index == 3:
            if self.ECG == 1:
                lower_bound = np.searchsorted(self.freq, freq_ranges[0][0])
                upper_bound = np.searchsorted(self.freq, freq_ranges[0][1])
                modified_regions[lower_bound:upper_bound] = True
                complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                    np.exp(1j * np.angle(np.fft.rfft(y1)[lower_bound:upper_bound])) * \
                    (self.ECG_Sliders[0].value() / 100)
                print("slider 1")
                print(self.ECG_Sliders[0].value())
            if self.ECG == 2:
                lower_bound = np.searchsorted(self.freq, freq_ranges[1][0])
                upper_bound = np.searchsorted(self.freq, freq_ranges[1][1])
                modified_regions[lower_bound:upper_bound] = True
                complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                    np.exp(1j * np.angle(np.fft.rfft(y1)[lower_bound:upper_bound])) * \
                    (self.ECG_Sliders[1].value() / 100)
                print("slider 2")
                print(self.ECG_Sliders[1].value())
            if self.ECG == 3:
                lower_bound = np.searchsorted(self.freq, freq_ranges[2][0])
                upper_bound = np.searchsorted(self.freq, freq_ranges[2][1])
                modified_regions[lower_bound:upper_bound] = True
                complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                    np.exp(1j * np.angle(np.fft.rfft(y1)[lower_bound:upper_bound])) * \
                    (self.ECG_Sliders[2].value() / 100)
                print("slider 3")
                print(self.ECG_Sliders[2].value())
            if self.ECG == 4:
                lower_bound = np.searchsorted(self.freq, freq_ranges[3][0])
                upper_bound = np.searchsorted(self.freq, freq_ranges[3][1])
                modified_regions[lower_bound:upper_bound] = True
                complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                    np.exp(1j * np.angle(np.fft.rfft(y1)[lower_bound:upper_bound])) * \
                    (self.ECG_Sliders[3].value() / 100)
                print("slider 4")
                print(self.ECG_Sliders[3].value())

            unmodified_indices = np.logical_not(modified_regions)
            original_complex_array = self.mag * \
                np.exp(1j * np.angle(np.fft.rfft(y1)))
            complex_array[unmodified_indices] = original_complex_array[unmodified_indices]

            modified_signal = np.fft.irfft(complex_array)
            y1_values.insert(0, modified_signal)
        else:
            for i in range(count):
                lower_bound = np.searchsorted(self.freq, freq_ranges[i][0])
                upper_bound = np.searchsorted(self.freq, freq_ranges[i][1])
                modified_regions[lower_bound:upper_bound] = True
                if current_tab_index == 1:
                    complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                        np.exp(1j * np.angle(np.fft.rfft(self.audio)[lower_bound:upper_bound])) * \
                        (self.Musical_Sliders[i].value() / 100)
                elif current_tab_index == 2:
                    complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                        np.exp(1j * np.angle(np.fft.rfft(self.audio)[lower_bound:upper_bound])) * \
                        (self.Animal_Sliders[i].value() / 100)
                elif current_tab_index == 3:

                    complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                        np.exp(1j * np.angle(np.fft.rfft(self.audio)[lower_bound:upper_bound])) * \
                        (self.ECG_Sliders[i].value() / 100)

                elif current_tab_index == 0:
                    complex_array[lower_bound:upper_bound] = self.mag[lower_bound:upper_bound] * \
                        np.exp(1j * np.angle(np.fft.rfft(self.audio)[lower_bound:upper_bound])) * \
                        (self.Uniform_Sliders[i].value() / 100)
            unmodified_indices = np.logical_not(modified_regions)
            original_complex_array = self.mag * \
                np.exp(1j * np.angle(np.fft.rfft(self.audio)))
            complex_array[unmodified_indices] = original_complex_array[unmodified_indices]

            modified_signal = np.fft.irfft(complex_array)
            self.scaled_data = np.int16(
                modified_signal / np.max(np.abs(modified_signal)) * 32767)
            output_directory = 'C:\\Users\\Pavilion\\Desktop\\Dsp_Task3'
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_wav_filename = f"output_audio_{timestamp}.wav"
            output_filename = os.path.join(output_directory, new_wav_filename)

            wavfile.write(output_filename,
                          self.sample_rate, self.scaled_data)


def Ranges(self):
    global slider_range
    print("ana gowa el ranges")
    if current_tab_index == 0:
        slider_range = [
            (195, 205), (395, 405), (595, 605), (795, 805), (995, 1005), (1195,
                                                                          1205), (1395, 1405), (1595, 1605), (1795, 1805), (1995, 2005)
        ]

        sliders = 10

    elif current_tab_index == 1:
        slider_range = [
            (1, 500), (500, 950), (950, 2050), (2050, 16000)
        ]
        sliders = 4

    elif current_tab_index == 2:
        slider_range = [
            (1000, 2000), (500, 1000), (1, 500), (2000, 16000)
        ]
        sliders = 4

    elif current_tab_index == 3:
        slider_range = [
            (0, 100), (25, 250), (20, 300), (25, 490)
        ]
        sliders = 4

    return slider_range, sliders


def Equalise(self):
    global slider_range, window
    if Smoothing_Window == True:
        new_mag = (self.mag.copy())*window

    new_mag = self.mag.copy()
    if current_tab_index == 0:
        slider_range = [
            (195, 205), (395, 405), (595, 605), (795, 805), (995, 1005), (1195,
                                                                          1205), (1395, 1405), (1595, 1605), (1795, 1805), (1995, 2005)
        ]
    elif current_tab_index == 1:
        slider_range = [
            (1, 500), (500, 950), (950, 2050), (2050, 16000)
        ]
    elif current_tab_index == 2:
        slider_range = [
            (1000, 2000), (500, 1000), (1, 500), (2000, 16000)
        ]
    elif current_tab_index == 3:
        slider_range = [
            (0, 100), (25, 250), (20, 300), (25, 490)
        ]

    if current_tab_index == 0:
        for i in range(10):
            lower_bound = np.searchsorted(self.freq, slider_range[i][0])
            upper_bound = np.searchsorted(self.freq, slider_range[i][1])
            new_mag[lower_bound:upper_bound] *= self.Uniform_Sliders[i].value() / \
                100
    elif current_tab_index == 1:
        for i in range(4):
            lower_bound = np.searchsorted(self.freq, slider_range[i][0])
            upper_bound = np.searchsorted(self.freq, slider_range[i][1])
            new_mag[lower_bound:upper_bound] *= self.Musical_Sliders[i].value() / \
                100
    elif current_tab_index == 2:
        for i in range(4):
            lower_bound = np.searchsorted(self.freq, slider_range[i][0])
            upper_bound = np.searchsorted(self.freq, slider_range[i][1])
            new_mag[lower_bound:upper_bound] *= self.Animal_Sliders[i].value() / \
                100
    elif current_tab_index == 3:
        if self.ECG == 1:
            lower_bound = np.searchsorted(self.freq, slider_range[0][0])
            upper_bound = np.searchsorted(self.freq, slider_range[0][1])
            new_mag[lower_bound:upper_bound] *= self.ECG_Sliders[0].value() / \
                100
        elif self.ECG == 2:
            lower_bound = np.searchsorted(self.freq, slider_range[1][0])
            upper_bound = np.searchsorted(self.freq, slider_range[1][1])
            new_mag[lower_bound:upper_bound] *= self.ECG_Sliders[1].value() / \
                100
        elif self.ECG == 3:
            lower_bound = np.searchsorted(self.freq, slider_range[2][0])
            upper_bound = np.searchsorted(self.freq, slider_range[2][1])
            new_mag[lower_bound:upper_bound] *= self.ECG_Sliders[2].value() / \
                100
        elif self.ECG == 4:
            lower_bound = np.searchsorted(self.freq, slider_range[3][0])
            upper_bound = np.searchsorted(self.freq, slider_range[3][1])
            new_mag[lower_bound:upper_bound] *= self.ECG_Sliders[3].value() / \
                100

    self.Frequency_Graph.clear()
    self.Frequency_Graph.plot(self.freq, new_mag, pen='r')
    Fourier_Inverse(self)
    # complex_spectrum = np.abs(np.fft.rfft(audio_data))
    # complex_array = new_mag * \
    #     np.exp(1j * np.angle(complex_spectrum))
    # modified_signal = np.fft.irfft(complex_array)

    # # Normalize the signal to the range of int16 (if required)
    # scaled_data = np.int16(
    #     modified_signal * (32767 / np.max(np.abs(modified_signal))))

    # # Save the signal as a .wav file
    # output_filename = "output_audio.wav"
    # wavfile.write(output_filename, self.sample_rate, scaled_data)
    # # self.player.setMedia(QMediaContent(
    # #     QUrl.fromLocalFile(output_filename)))
    # # self.player.play()


def setup_timer(self):
    global plot_iteration, timer
    timer.setInterval(50)  # Update plot every 50 milliseconds
    # timer.timeout.connect(lambda: update_plot(self))
    if ecg == True:
        timer.timeout.connect(lambda: update_plot_Ecg(self))
    else:
        timer.timeout.connect(lambda: update_plot(self))
    timer.start()
    plot_iteration = 0


def update_plot(self):
    global audio_data, timer, plot_iteration, x_values, y_values, y1_values, y1, wav
    if wav == True:
        # Calculate the current position of the media player in milliseconds
        current_position = self.player.position()

        # Calculate the corresponding sample index in the audio data frame
        current_sample_index = int(
            (current_position / 1000) * self.sample_rate)

        # Determine the range of samples to be plotted based on the current position and a window size
        window_size = 2000  # Adjust this window size as needed
        half_window = window_size // 2

        start_sample = max(0, current_sample_index - half_window)
        end_sample = min(len(audio_data), current_sample_index + half_window)

        end_sample_output = min(
            len(self.scaled_data), current_sample_index+half_window)

        # Get the time axis for the audio plot
        time_axis = np.linspace(0, len(audio_data) /
                                self.sample_rate, len(audio_data))
        time_axis_output = np.linspace(
            0, len(self.scaled_data)/self.sample_rate, len(self.scaled_data))

        # Ensure start_sample and end_sample are within bounds
        if start_sample < 0:
            start_sample = 0
        if end_sample > len(audio_data):
            end_sample = len(audio_data)

        if end_sample_output > len(self.scaled_data):
            end_sample_output = len(self.scaled_data)

        # Clear the plot before updating
        self.Input_Graph.clear()
        self.Output_Graph.clear()

        # Plot the audio waveform within the specified range
        if start_sample < end_sample:
            if self.audio_flag == "stereo":
                first_column_input = [row[0] for row in audio_data]
                self.Input_Graph.plot(time_axis[start_sample:end_sample].tolist(
                ), first_column_input[start_sample:end_sample], pen='b')

                # first_column_output = [row[1] for row in self.scaled_data]
                self.Output_Graph.plot(time_axis_output[start_sample:end_sample_output].tolist(
                ), self.scaled_data[start_sample:end_sample_output], pen='g')

            elif self.audio_flag == "mono":
                self.Input_Graph.plot(time_axis[start_sample:end_sample].tolist(
                ), audio_data[start_sample:end_sample], pen='b')

                self.Output_Graph.plot(time_axis_output[start_sample:end_sample_output].tolist(
                ), self.scaled_data[start_sample:end_sample_output], pen='g')

        # Set the X range of the plot to focus on the current window
        if start_sample < end_sample:
            self.Input_Graph.setXRange(
                time_axis[start_sample], time_axis[end_sample])

            self.Output_Graph.setXRange(
                time_axis_output[start_sample], time_axis_output[end_sample_output])

        # Restart the timer for continuous plotting
        if not timer.isActive():
            timer.start()


def update_plot_Ecg(self, channel_index=None):
    global plot_iteration, x_values, y_values, timer, max_data_points, audio_data, Xplotted, Xplotted2, x1_values, y1_values
    # Clear the graphWidget before plotting new data
    if plot_iteration == 0:
        self.Input_Graph.clear()
        self.Output_Graph.clear()

    if plot_iteration < max_data_points:
        # Xplotted += 1
        # Xplotted2 += 1
        # x_range_end = plot_iteration  # Set it to the current iteration
        # self.Input_Graph.setLimits(
        #     yMin=min(y_values[0][:Xplotted]), yMax=max(y_values[0][:Xplotted]))
        # self.Input_Graph.setLimits(xMin=0, xMax=max(
        #     x_values[0][:plot_iteration + 1]))
        # self.Output_Graph.setLimits(
        #     yMin=min(y1_values[0][:Xplotted]), yMax=max(y1_values[0][:Xplotted]))
        # self.Output_Graph.setLimits(
        #     xMin=0, xMax=max(x_values[0][:plot_iteration + 1]))

        # # Clear the graphWidget
        self.Input_Graph.clear()
        self.Output_Graph.clear()
        x_range_end = plot_iteration  # Set it to the current iteration
        # Adjust the range as needed
        x_range_start = max(0, x_range_end - 100)
        # y1_values_reversed = [y[::-1] for y in y1_values]

        # Plot all data arrays up to the current iteration
        for i in range(len(x_values)):
            x = x_values[i][:plot_iteration]
            y = y_values[i][:plot_iteration]
            x1 = x_values[i][:plot_iteration]
            y1 = y1_values[i][:plot_iteration]
            pen = pg.mkPen('g')
            self.Input_Graph.plot(x, y, pen=pen)
            self.Output_Graph.plot(x1, y1, pen=pen)

            self.x_range = [x_range_start, x_range_end]
            self.Input_Graph.setXRange(*self.x_range)
            self.Input_Graph.setXRange(
                x_values[0][x_range_start], x_values[0][x_range_end])
            self.Output_Graph.setXRange(*self.x_range)
            self.Output_Graph.setXRange(
                x_values[0][x_range_start], x_values[0][x_range_end])
        plot_iteration += 1
    else:
        timer.stop()  # Stop the QTimer when finished


def rewind(self):
    global plot_iteration, running, timer, wav, ecg
    # Reset the plot iteration counters to 0
    if wav == True:
        self.player.stop()
        self.player.play()

    elif ecg == True:
        plot_iteration = 0
        if timer.isActive():
            timer.stop()
            timer.start()
        else:
            timer.start()


def start_stop_Input(self):
    global running, timer, Xplotted, Xplotted2, y1_values, wav, ecg
    # self.Input_Graph.setLimits(xMin=0, xMax=max(x_values[0][:Xplotted]))
    # self.Input_Graph.setLimits(
    #     yMin=min(y_values[0][:Xplotted]), yMax=max(y_values[0][:Xplotted]))

    if running:
        if wav == True:
            timer.stop()
            self.player.pause()
            self.PauseButton.setText("Play")
        elif ecg == True:
            timer.stop()
            self.PauseButton.setText("Play")
    else:
        if wav == True:
            timer.start()
            self.player.play()
            self.PauseButton.setText("Pause")
        elif ecg == True:
            timer.start()
            self.PauseButton.setText("Pause")
    running = not running


def update_speed_label(self, value):
    self.label_49.setText(f"Speed:{value}")
    update_graph_speed(self, value)


def update_graph_speed(self, speed):
    global timer
    if ecg == True:
        if speed == 50:
            interval = 50
            timer.setInterval(interval)
        else:
            interval = int(1000 / speed)
            timer.setInterval(interval)
    else:
        if speed == 50:
            interval = 50
            audio_speed = self.player.playbackRate()
        # Adjust the scaling factor as needed
        else:
            # Calculate the interval in milliseconds
            interval = int(1000 / speed)
            audio_speed = speed / 50
        # Set the playback rate of the player
        if self.player:
            self.player.setPlaybackRate(audio_speed)

        if timer.isActive():
            timer.stop()
            # Update the timer interval
            timer.setInterval(interval)
            timer.start()


def Smoothing_Window(self, Rect, Ham, Han, G):
    Smoothing_Window = True
    global gaussian_std, window
    window_size = 1000
    if Rect == True:
        window = np.ones(window_size)
        # x = np.arange(window_size)
        # self.Smoother_Graph.clear()
        # self.Smoother_Graph.plot(x, window, title='Rectangular Smoothing Window', pen='b')
    elif Ham == True:
        window = np.hamming(window_size)
        # x = np.arange(window_size)
        # self.Smoother_Graph.clear()
        # self.Smoother_Graph.plot(x, window, title='Hamming Smoothing Window', pen='b')
    elif Han == True:
        window = np.hanning(window_size)
        # x = np.arange(window_size)
        # self.Smoother_Graph.clear()
        # self.Smoother_Graph.plot(x, window, title='Hanning Smoothing Window', pen='b')
    elif G == True:
        window = np.exp(-(0.5 * ((window_size - 1) / 2 - np.arange(window_size)
                                 ) / (gaussian_std * (window_size - 1) / 2)) ** 2)
    x = np.arange(window_size)
    self.Smoother_Graph.clear()
    self.Smoother_Graph.plot(x, window, pen='b')


def update_gaussian_window(self, value):
    global gaussian_std
    gaussian_std = value / 10
    Smoothing_Window(self, False, False, False, True)
