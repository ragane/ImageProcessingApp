import cv2 as cv
import numpy as np
import sys
from abc import ABC, abstractmethod


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSlider,
)


class AdditionalWindow(QWidget):
    @abstractmethod
    def __init__(self):
        super(AdditionalWindow, self).__init__()

        self.MainLayout = QVBoxLayout()
        self.FirstLayout = QVBoxLayout()
        self.SecondLayout = QVBoxLayout()
        self.ThirdLayout = QVBoxLayout()

        self.FirstSlider = QSlider()
        self.FirstSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FirstSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.FirstSlider.setTickPosition(QSlider.TicksBothSides)
        self.FirstSlider.setTickInterval(10)
        self.FirstSlider.setSingleStep(1)
        self.FirstSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.SecondSlider = QSlider()
        self.SecondSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SecondSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SecondSlider.setTickPosition(QSlider.TicksBothSides)
        self.SecondSlider.setTickInterval(10)
        self.SecondSlider.setSingleStep(1)
        self.SecondSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.ThirdSlider = QSlider()
        self.ThirdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ThirdSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ThirdSlider.setTickPosition(QSlider.TicksBothSides)
        self.ThirdSlider.setTickInterval(10)
        self.ThirdSlider.setSingleStep(1)
        self.ThirdSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.FirstLabel = QLabel(" ")
        self.SecondLabel = QLabel(" ")
        self.ThirdLabel = QLabel(" ")

        self.setLayout(self.MainLayout)
        self.MainLayout.addLayout(self.FirstLayout)
        self.MainLayout.addLayout(self.SecondLayout)
        self.MainLayout.addLayout(self.ThirdLayout)

        self.FirstLayout.addWidget(self.FirstLabel)
        self.FirstLayout.addWidget(self.FirstSlider)
        self.SecondLayout.addWidget(self.SecondLabel)
        self.SecondLayout.addWidget(self.SecondSlider)
        self.ThirdLayout.addWidget(self.ThirdLabel)
        self.ThirdLayout.addWidget(self.ThirdSlider)

        self.Value = 0
        self.ChosenChannel = 0

    @abstractmethod
    def GetImg(self, image):
        self.Image = image

    @QtCore.pyqtSlot(int)
    @abstractmethod
    def FirstGetValue(self, value):
        self.Value = value
        self.ChosenChannel = 0
        print("Value is: ", self.Value, " +++++ ", self.ChosenChannel)
        self.SetValue()

    @abstractmethod
    @QtCore.pyqtSlot(int)
    def SecondGetValue(self, value):
        self.Value = value
        self.ChosenChannel = 1
        print("Value is: ", self.Value, " +++++ ", self.ChosenChannel)
        self.SetValue()

    @abstractmethod
    @QtCore.pyqtSlot(int)
    def ThirdGetValue(self, value):
        self.Value = value
        self.ChosenChannel = 2
        print("Value is: ", self.Value, "+++++", self.ChosenChannel)
        self.SetValue()

    @abstractmethod
    @QtCore.pyqtSlot(int)
    def SetValue(self):

        firstChannel, secondChannel, thirdChannel = cv.split(self.Image)
        if self.ChosenChannel == 0:
            lim = 255 - self.Value
            firstChannel[firstChannel > 255] = 255
            firstChannel[firstChannel <= lim] += self.Value

        elif self.ChosenChannel == 1:
            lim = 255 - self.Value
            secondChannel[secondChannel > 255] = 255
            secondChannel[secondChannel <= lim] += self.Value

        else:
            lim = 255 - self.Value
            thirdChannel[thirdChannel > 255] = 255
            thirdChannel[thirdChannel <= lim] += self.Value

        image = cv.merge((firstChannel, secondChannel, thirdChannel))
        return image


class BGR_window(AdditionalWindow):
    def __init__(self):
        super().__init__()
        self.FirstLabel.setText("B value: ")
        self.FirstSlider.setRange(0, 255)

        self.SecondLabel.setText("G value: ")
        self.SecondSlider.setRange(0, 255)

        self.ThirdLabel.setText("R value: ")
        self.ThirdSlider.setRange(0, 255)


class RGB_window(AdditionalWindow):

    def __init__(self):
        super().__init__()

        self.FirstLabel.setText("R value: ")
        self.FirstSlider.setRange(0, 255)
        self.SecondLabel.setText("G value: ")
        self.SecondSlider.setRange(0, 255)
        self.ThirdLabel.setText("B value: ")
        self.ThirdSlider.setRange(0, 255)


class HSV_window(AdditionalWindow):

    def __init__(self):
        super().__init__()

        self.FirstLabel.setText("H value: ")
        self.FirstSlider.setRange(0, 179)
        self.SecondLabel.setText("S value: ")
        self.SecondSlider.setRange(0, 255)
        self.ThirdLabel.setText("V value: ")
        self.ThirdSlider.setRange(0, 255)
