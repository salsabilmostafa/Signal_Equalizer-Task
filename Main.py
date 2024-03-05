
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import uic
import UI
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import sys
import pyqtgraph as pg
from mplwidget import MplWidget
from PyQt5.QtMultimedia import QMediaPlayer


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("UI.ui", self)
        self.mplWidget = MplWidget()  # Create an instance of MplWidget
        self.gridLayout_4.addWidget(self.mplWidget)  # Add it to the layout
        self.mplWidget_out = MplWidget()  # Create an instance of MplWidget
        self.gridLayout_5.addWidget(self.mplWidget_out)  # Add it to the layout
        self.player = QMediaPlayer()
        UI.initConnectors(self)
        self.show()

    def toggle_spectrogram_widget_Hide(self, checked):
        if checked:
            # Hide the spectrogram widget
            self.mplWidget_out.hide()
            self.mplWidget.hide()

    def toggle_spectrogram_widget_Show(self, checked):
        if checked:
            # Hide the spectrogram widget
            self.mplWidget_out.show()
            self.mplWidget.show()

    def toggle_spectrogram(self):
        if self.mplWidget.isHidden():
            # self.gridLayout_4.show()
            self.frame.setGeometry(QtCore.QRect(0, 12, 1082, 301))
            self.Input_Graph.setGeometry(QtCore.QRect(10, 10, 1000, 300))

        if self.mplWidget_out.isHidden():
            # self.gridLayout_4.hide()
            self.frame_3.setGeometry(QtCore.QRect(12, 307, 1082, 301))
            self.Output_Graph.setGeometry(QtCore.QRect(10, 10, 1000, 300))

        if self.mplWidget.isVisible():
            # self.gridLayout_4.show()
            self.frame.setGeometry(QtCore.QRect(0, 12, 541, 301))
            self.Input_Graph.setGeometry(QtCore.QRect(10, 10, 521, 281))

        if self.mplWidget_out.isVisible():
            # self.gridLayout_4.hide()
            self.frame_3.setGeometry(QtCore.QRect(12, 307, 541, 291))
            self.Output_Graph.setGeometry(QtCore.QRect(10, 10, 521, 271))


app = QApplication(sys.argv)
UIwindow = MainWindow()
app.exec_()
