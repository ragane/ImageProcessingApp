import sys
import cv2 as cv
import numpy as np
import imutils

from abc import ABC, abstractmethod
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSlider,
)


class TransformWindow(QWidget):
    @abstractmethod
    def __init__(self):
        super(TransformWindow, self).__init__()

        self.MainLayout = QVBoxLayout()

        self.KernelSlider = QSlider()
        self.IterationSlider = QSlider()
        self.KernelLabel = QLabel()
        self.IterationLabel = QLabel()
        self.ApplyButton = QPushButton()

        Sliders = [self.KernelSlider, self.IterationSlider]
        for i in Sliders:
            i.setOrientation(QtCore.Qt.Horizontal)
            i.setFocusPolicy(QtCore.Qt.StrongFocus)
            i.setTickPosition(QSlider.TicksBothSides)

        self.setLayout(self.MainLayout)
        self.MainLayout.addWidget(self.KernelSlider)
        self.MainLayout.addWidget(self.IterationSlider)
        self.MainLayout.addWidget(self.ApplyButton)
        self.ApplyButton.setText("Apply settings")
        self.Image = None
        self.KernelSize = 1
        self.Kernel = None
        self.Iterations = 1
        self.imageOut = None

    @abstractmethod
    def getImage(self, image):
        self.Image = image

    def getKernelSize(self, value):
        if value % 2 == 1:
            self.KernelSize = value
        self.Kernel = np.ones((self.KernelSize, self.KernelSize), np.uint8)

    def getIteration(self, value):
        self.Iterations = value

    def SetValue(self):
        pass


class ErosionTransform(TransformWindow):
    def __init__(self):
        super().__init__()

        self.KernelSlider.setRange(1, 10)
        self.IterationSlider.setRange(1, 10)

    def SetValue(self):
        self.imageOut = cv.erode(self.Image, self.Kernel, iterations = self.Iterations)
        image = imutils.resize(self.imageOut, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image


class DilationTransform(TransformWindow):
    def __init__(self):
        super().__init__()
        self.KernelSlider.setRange(1, 10)
        self.IterationSlider.setRange(1, 10)

    def SetValue(self):
        self.imageOut = cv.dilate(self.Image, self.Kernel, iterations = self.Iterations)
        image = imutils.resize(self.imageOut, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image


class OpeningTransform(TransformWindow):
    def __init__(self):
        super().__init__()
        self.KernelSlider.setRange(1, 10)

    def SetValue(self):
        self.imageOut = cv.morphologyEx(self.Image, cv.MORPH_OPEN, self.Kernel)
        image = imutils.resize(self.imageOut, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image


class ClosingTransform(TransformWindow):
    def __init__(self):
        super().__init__()
        self.KernelSlider.setRange(1, 10)

    def SetValue(self):
        self.imageOut = cv.morphologyEx(self.Image, cv.MORPH_CLOSE, self.Kernel)
        image = imutils.resize(self.imageOut, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image


class GradientTransform(TransformWindow):
    def __init__(self):
        super().__init__()

        self.KernelSlider.setRange(1, 10)
        self.IterationSlider.setRange(1, 10)

    def SetValue(self):
        self.imageOut = cv.morphologyEx(self.Image, cv.MORPH_GRADIENT, self.Kernel)
        image = imutils.resize(self.imageOut, 600, 500)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image