import sys, imutils
import cv2 as cv
import numpy as np

from abc import ABC, abstractmethod
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QSlider,
    QRadioButton,
)


class HighPassWindow(QWidget):
    @abstractmethod
    def __init__(self):
        super(HighPassWindow, self).__init__()

        self.MainLayout = QVBoxLayout()
        self.Layout_1 = QVBoxLayout()
        self.Layout_2 = QVBoxLayout()

        self.Slider_1 = QSlider()
        self.Slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Slider_1.setTickPosition(QSlider.TicksBothSides)
        self.Slider_1.setTickInterval(1)
        self.Slider_1.setSingleStep(1)
        self.Slider_1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.RadioButton_1 = QRadioButton()

        self.Slider_2 = QSlider()
        self.Slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Slider_2.setTickPosition(QSlider.TicksBothSides)
        self.Slider_2.setTickInterval(1)
        self.Slider_2.setSingleStep(1)
        self.Slider_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.RadioButton_2 = QRadioButton()

        self.setLayout(self.MainLayout)
        self.MainLayout.addLayout(self.Layout_1)
        self.MainLayout.addLayout(self.Layout_2)

        # Values for all classes
        self.Image = None
        self.imageOut = None
        self.KernelSize = 1

        self.valueX = 0
        self.valueY = 0
        self.imageX = None
        self.imageY = None

    @abstractmethod
    def getImg(self, image):
        self.Image = image

    @QtCore.pyqtSlot(int)
    @abstractmethod
    def getValue(self, value):
        if value % 2 == 1:
            self.KernelSize = value

    def SetFilter(self):
        pass


class SobelFilter(HighPassWindow):
    def __init__(self):
        super().__init__()
        self.Layout_1.addWidget(self.RadioButton_1)
        self.Layout_1.addWidget(self.RadioButton_2)
        self.Layout_1.addWidget(self.Slider_1)
        self.RadioButton_1.setText("Sobel Filter along X-axis")
        self.RadioButton_2.setText("Sobel Filter along Y-axis")
        self.Slider_1.setRange(1, 32)

    def SetFilter(self):
        if self.RadioButton_1.isChecked():
            self.imageX = cv.Sobel(self.Image, -cv.CV_64F, 1, 0, ksize = self.KernelSize)
            image = imutils.resize(self.imageX, 600, 500)
        elif self.RadioButton_2.isChecked():
            self.imageY = cv.Sobel(self.Image, -cv.CV_64F, 0, 1, ksize = self.KernelSize)
            image = imutils.resize(self.imageY, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image


class LaplacianFilter(HighPassWindow):
    def __init__(self):
        super().__init__()
        self.Label = QLabel()
        self.Layout_1.addWidget(self.Label)
        self.Layout_1.addWidget(self.Slider_1)
        self.Label.setText("Set size of kernel: ")
        self.Slider_1.setRange(1, 28)

    def SetFilter(self):
        self.imageOut = cv.Laplacian(self.Image, -cv.CV_64F, ksize = self.KernelSize)
        image = imutils.resize(self.imageOut, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image


class ScharrFilter(HighPassWindow):
    def __init__(self):
        super().__init__()
        self.Layout_1.addWidget(self.RadioButton_1)
        self.Layout_1.addWidget(self.RadioButton_2)
        self.RadioButton_1.setText("Scharr Filtering along X-axis")
        self.RadioButton_2.setText("Scharr Filtering along Y-axis")
        self.KernelSize = cv.FILTER_SCHARR

    def getAxis(self):
        if self.RadioButton_1.isChecked():
            self.imageX = cv.Scharr(self.Image, -cv.CV_64F, 1, 0, self.KernelSize)
            image = self.imageX
        elif self.RadioButton_2.isChecked():
            self.imageY = cv.Scharr(self.Image, -cv.CV_64F, 0, 1, self.KernelSize)
            image = self.imageY
        image = imutils.resize(image, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image


class CannyFilter(HighPassWindow):
    def __init__(self):
        super().__init__()
        self.Label_1 = QLabel()
        self.Label_2 = QLabel()
        self.Layout_1.addWidget(self.Label_1)
        self.Layout_1.addWidget(self.Slider_1)
        self.Label_1.setText("First threshold for the hysteresis procedure:")
        self.Layout_2.addWidget(self.Label_2)
        self.Layout_2.addWidget(self.Slider_2)
        self.Label_2.setText("Second threshold for the hysteresis procedure:")
        self.Slider_1.setRange(1, 300)
        self.Slider_2.setRange(1, 300)

    @QtCore.pyqtSlot(int)
    def FirstGetValue(self, value):
        self.valueX = value
        print("Value is: ", self.valueX)

    @QtCore.pyqtSlot(int)
    def SecondGetValue(self, value):
        self.valueY = value
        print("Value is: ", self.valueY)

    def SetFilter(self):
        self.imageOut = cv.Canny(self.Image, self.valueX, self.valueY)
        image = imutils.resize(self.imageOut, 600, 500)
        return image
