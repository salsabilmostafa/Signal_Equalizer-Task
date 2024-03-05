
from pyqtgraph import PlotWidget

from PyQt5 import QtCore, QtGui, QtWidgets
import Functions


def initConnectors(self):
    # Frame items
    self.Input_Graph = self.findChild(PlotWidget, "Input_Graph")
    self.Output_Graph = self.findChild(PlotWidget, "Output_Graph")
    self.Frequency_Graph = self.findChild(PlotWidget, "Frequency_Graph")
    self.LoadButton = self.findChild(QtWidgets.QPushButton, "LoadButton")
    self.PauseButton = self.findChild(QtWidgets.QPushButton, "PauseButton")
    self.ResetButton = self.findChild(QtWidgets.QPushButton, "ResetButton")
    self.ZoomIn_Button = self.findChild(QtWidgets.QPushButton, "ZoomIn_Button")
    self.ZoomOut_Button = self.findChild(
        QtWidgets.QPushButton, "ZoomOut_Button")
    self.Speed_Slider = self.findChild(QtWidgets.QSlider, "Speed_Slider")
    self.label_49 = self.findChild(QtWidgets.QLabel, "label_49")
    self.Input_RadioBtn = self.findChild(
        QtWidgets.QRadioButton, "Input_RadioBtn")
    self.Output_RadioBtn = self.findChild(
        QtWidgets.QRadioButton, "Output_RadioBtn")
    self.Hide_Spect = self.findChild(QtWidgets.QRadioButton, "Hide_Spect")
    self.Show_Spect = self.findChild(QtWidgets.QRadioButton, "Show_Spect")
    # tab_widget objects
    self.tabWidget = self.findChild(QtWidgets.QTabWidget, "tabWidget")
    # Uniform_Range tab
    self.Uniform_Sliders = [self.Range1_Slider, self.Range2_Slider, self.Range3_Slider, self.Range4_Slider,
                            self.Range5_Slider, self.Range6_Slider, self.Range7_Slider, self.Range8_Slider, self.Range9_Slider, self.Range10_Slider]
    self.Range1_Slider = self.findChild(QtWidgets.QSlider, "Range1_Slider")
    self.Range2_Slider = self.findChild(QtWidgets.QSlider, "Range2_Slider")
    self.Range3_Slider = self.findChild(QtWidgets.QSlider, "Range3_Slider")
    self.Range4_Slider = self.findChild(QtWidgets.QSlider, "Range4_Slider")
    self.Range5_Slider = self.findChild(QtWidgets.QSlider, "Range5_Slider")
    self.Range6_Slider = self.findChild(QtWidgets.QSlider, "Range6_Slider")
    self.Range7_Slider = self.findChild(QtWidgets.QSlider, "Range7_Slider")
    self.Range8_Slider = self.findChild(QtWidgets.QSlider, "Range8_Slider")
    self.Range9_Slider = self.findChild(QtWidgets.QSlider, "Range9_Slider")
    self.Range10_Slider = self.findChild(QtWidgets.QSlider, "Range10_Slider")
    # Music tab
    self.Musical_Sliders = [self.Musical_slider_1, self.Musical_slider_2,
                            self.Musical_slider_3, self.Musical_slider_4]
    self.Musical_slider_1 = self.findChild(
        QtWidgets.QSlider, "Musical_slider_1")
    self.Musical_slider_2 = self.findChild(
        QtWidgets.QSlider, "Musical_slider_2")
    self.Musical_slider_3 = self.findChild(
        QtWidgets.QSlider, "Musical_slider_3")
    self.Musical_slider_4 = self.findChild(
        QtWidgets.QSlider, "Musical_slider_4")
    # Animal_sound tab
    self.Animal_Sliders = [self.Animal_slider_1, self.Animal_slider_2,
                           self.Animal_slider_3, self.Animal_slider_4]
    self.Animal_slider_1 = self.findChild(QtWidgets.QSlider, "Animal_slider_1")
    self.Animal_slider_2 = self.findChild(QtWidgets.QSlider, "Animal_slider_2")
    self.Animal_slider_3 = self.findChild(QtWidgets.QSlider, "Animal_slider_3")
    self.Animal_slider_4 = self.findChild(QtWidgets.QSlider, "Animal_slider_4")
    # ECG tab
    self.ECG_Sliders = [self.ECG_slider_1, self.ECG_slider_2,
                        self.ECG_slider_3, self.ECG_slider_4]
    self.ECG_slider_1 = self.findChild(QtWidgets.QSlider, "ECG_slider_1")
    self.ECG_slider_2 = self.findChild(QtWidgets.QSlider, "ECG_slider_2")
    self.ECG_slider_3 = self.findChild(QtWidgets.QSlider, "ECG_slider_3")
    self.ECG_slider_4 = self.findChild(QtWidgets.QSlider, "ECG_slider_4")
    # Smoother items
    self.Smoother_Graph = self.findChild(PlotWidget, "Smoother_Graph")
    self.Rectangle_Smoothing = self.findChild(
        QtWidgets.QRadioButton, "Rectangle_Smoothing")
    self.Hamming_Smoothing = self.findChild(
        QtWidgets.QRadioButton, "Hamming_Smoothing")
    self.Hanning_Smoothing = self.findChild(
        QtWidgets.QRadioButton, "Hanning_Smoothing")
    self.Gaussian_Smoothing = self.findChild(
        QtWidgets.QRadioButton, "Gaussian_Smoothing")
    self.Smoother_vertical_slider = self.findChild(
        QtWidgets.QSlider, "Smoother_vertical_slider")
    self.Smoother_horizontal_slider = self.findChild(
        QtWidgets.QSlider, "Smoother_horizontal_slider")

    # tabWidget
    self.tabWidget.currentChanged.connect(
        lambda index: Functions.update_current_tab_index(self, index))

    # Button Actions
    self.ZoomIn_Button.clicked.connect(lambda: Functions.zoom_in(self))
    self.ZoomOut_Button.clicked.connect(lambda: Functions. zoom_out(self))
    self.LoadButton.clicked.connect(lambda: Functions.browsefiles(self))
    self.PauseButton.clicked.connect(lambda: Functions.start_stop_Input(self))
    self.ResetButton.clicked.connect(lambda: Functions.rewind(self))
    self.Input_RadioBtn.clicked.connect(lambda: Functions.play_audio(self))
    self.Output_RadioBtn.clicked.connect(lambda: Functions.play_audio(self))

    self.Rectangle_Smoothing.clicked.connect(
        lambda: Functions.Smoothing_Window(self, True, False, False, False))
    self.Hamming_Smoothing.clicked.connect(
        lambda: Functions.Smoothing_Window(self, False, True, False, False))
    self.Hanning_Smoothing.clicked.connect(
        lambda: Functions.Smoothing_Window(self, False, False, True, False))
    self.Gaussian_Smoothing.clicked.connect(
        lambda: Functions.Smoothing_Window(self, False, False, False, True))
    self.Smoother_vertical_slider.valueChanged.connect(
        lambda value: Functions.update_gaussian_window(self, value))

    self.Hide_Spect.toggled.connect(self.toggle_spectrogram_widget_Hide)
    self.Hide_Spect.toggled.connect(self.toggle_spectrogram)
    self.Show_Spect.toggled.connect(self.toggle_spectrogram_widget_Show)
    self.Show_Spect.toggled.connect(self.toggle_spectrogram)

    self.Speed_Slider.setValue(50)
    self.Speed_Slider.setMaximum(100)
    self.Speed_Slider.setMinimum(1)
    self.Speed_Slider.setSingleStep(1)
    self.Speed_Slider.valueChanged.connect(
        lambda value: Functions.update_speed_label(self, value))

    self.Range1_Slider.setValue(50)
    self.Range1_Slider.setMaximum(100)
    self.Range1_Slider.setMinimum(0)
    self.Range1_Slider.setSingleStep(5)
    self.Range1_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range2_Slider.setValue(50)
    self.Range2_Slider.setMaximum(100)
    self.Range2_Slider.setMinimum(0)
    self.Range2_Slider.setSingleStep(5)
    self.Range2_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range3_Slider.setValue(50)
    self.Range3_Slider.setMaximum(100)
    self.Range3_Slider.setMinimum(0)
    self.Range3_Slider.setSingleStep(5)
    self.Range3_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range4_Slider.setValue(50)
    self.Range4_Slider.setMaximum(100)
    self.Range4_Slider.setMinimum(0)
    self.Range4_Slider.setSingleStep(5)
    self.Range4_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range5_Slider.setValue(50)
    self.Range5_Slider.setMaximum(100)
    self.Range5_Slider.setMinimum(0)
    self.Range5_Slider.setSingleStep(5)
    self.Range5_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range6_Slider.setValue(50)
    self.Range6_Slider.setMaximum(100)
    self.Range6_Slider.setMinimum(0)
    self.Range6_Slider.setSingleStep(5)
    self.Range6_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range7_Slider.setValue(50)
    self.Range7_Slider.setMaximum(100)
    self.Range7_Slider.setMinimum(0)
    self.Range7_Slider.setSingleStep(5)
    self.Range7_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range8_Slider.setValue(50)
    self.Range8_Slider.setMaximum(100)
    self.Range8_Slider.setMinimum(0)
    self.Range8_Slider.setSingleStep(5)
    self.Range8_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range9_Slider.setValue(50)
    self.Range9_Slider.setMaximum(100)
    self.Range9_Slider.setMinimum(0)
    self.Range9_Slider.setSingleStep(5)
    self.Range9_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Range10_Slider.setValue(50)
    self.Range10_Slider.setMaximum(100)
    self.Range10_Slider.setMinimum(0)
    self.Range10_Slider.setSingleStep(5)
    self.Range10_Slider.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Animal_slider_1.setValue(50)
    self.Animal_slider_1.setMaximum(100)
    self.Animal_slider_1.setMinimum(0)
    self.Animal_slider_1.setSingleStep(5)
    self.Animal_slider_1.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Animal_slider_2.setValue(50)
    self.Animal_slider_2.setMaximum(100)
    self.Animal_slider_2.setMinimum(0)
    self.Animal_slider_2.setSingleStep(5)
    self.Animal_slider_2.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Animal_slider_3.setValue(50)
    self.Animal_slider_3.setMaximum(100)
    self.Animal_slider_3.setMinimum(0)
    self.Animal_slider_3.setSingleStep(5)
    self.Animal_slider_3.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Animal_slider_4.setValue(50)
    self.Animal_slider_4.setMaximum(100)
    self.Animal_slider_4.setMinimum(0)
    self.Animal_slider_4.setSingleStep(5)
    self.Animal_slider_4.valueChanged.connect(lambda: Functions.Equalise(self))

    self.Musical_slider_1.setValue(50)
    self.Musical_slider_1.setMaximum(100)
    self.Musical_slider_1.setMinimum(0)
    self.Musical_slider_1.setSingleStep(5)
    self.Musical_slider_1.valueChanged.connect(
        lambda: Functions.Equalise(self))

    self.Musical_slider_2.setValue(50)
    self.Musical_slider_2.setMaximum(100)
    self.Musical_slider_2.setMinimum(0)
    self.Musical_slider_2.setSingleStep(5)
    self.Musical_slider_2.valueChanged.connect(
        lambda: Functions.Equalise(self))

    self.Musical_slider_3.setValue(50)
    self.Musical_slider_3.setMaximum(100)
    self.Musical_slider_3.setMinimum(0)
    self.Musical_slider_3.setSingleStep(5)
    self.Musical_slider_3.valueChanged.connect(
        lambda: Functions.Equalise(self))

    self.Musical_slider_4.setValue(50)
    self.Musical_slider_4.setMaximum(100)
    self.Musical_slider_4.setMinimum(0)
    self.Musical_slider_4.setSingleStep(5)
    self.Musical_slider_4.valueChanged.connect(
        lambda: Functions.Equalise(self))

    self.ECG_slider_1.setValue(50)
    self.ECG_slider_1.setMaximum(100)
    self.ECG_slider_1.setMinimum(0)
    self.ECG_slider_1.setSingleStep(5)
    self.ECG_slider_1.valueChanged.connect(
        lambda: Functions.Equalise(self))

    self.ECG_slider_2.setValue(50)
    self.ECG_slider_2.setMaximum(100)
    self.ECG_slider_2.setMinimum(0)
    self.ECG_slider_2.setSingleStep(5)
    self.ECG_slider_2.valueChanged.connect(
        lambda: Functions.Equalise(self))

    self.ECG_slider_3.setValue(50)
    self.ECG_slider_3.setMaximum(100)
    self.ECG_slider_3.setMinimum(0)
    self.ECG_slider_3.setSingleStep(5)
    self.ECG_slider_3.valueChanged.connect(
        lambda: Functions.Equalise(self))

    self.ECG_slider_4.setValue(50)
    self.ECG_slider_4.setMaximum(100)
    self.ECG_slider_4.setMinimum(0)
    self.ECG_slider_4.setSingleStep(5)
    self.ECG_slider_4.valueChanged.connect(
        lambda: Functions.Equalise(self))
