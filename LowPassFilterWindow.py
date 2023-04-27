import cv2 as cv
import numpy as np
import sys
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


class LowPassWindow(QWidget):
    @abstractmethod
    def __init__(self):
        super(LowPassWindow, self).__init__()

        self.MainLayout = QVBoxLayout()
        self.Slider = QSlider()
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Slider.setTickPosition(QSlider.TicksBothSides)
        self.Slider.setTickInterval(1)
        self.Slider.setSingleStep(2)
        self.Slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.ApplyButton = QPushButton()

        self.setLayout(self.MainLayout)
        self.MainLayout.addWidget(self.Slider)

        # variable needed by Filters
        self.Image = None
        self.OutImg = None
        self.KernelSize = 1
        self.Noise = 3

    @QtCore.pyqtSlot(int)
    @abstractmethod
    def GetKernelSize(self, value):
        if (value % 2 == 1) and (value > 0):
            self.KernelSize = value
        self.SetImg()

    @QtCore.pyqtSlot(int)
    @abstractmethod
    def GetNoiseLevel(self, value):
        if (value % 2 == 1) and (value > 2):
            self.Noise = value
        print(self.Noise)
        self.SetImg()

    @abstractmethod
    def SetImg(self):
        pass

    @abstractmethod
    def GetImg(self, image):
        self.Image = image


class Filter2D(LowPassWindow):
    def __init__(self):
        super().__init__()
        self.Slider.setRange(1, 15)
        self.kernel = None

    def SetImg(self):
        self.kernel = np.ones((self.KernelSize, self.KernelSize), np.float32) / (self.KernelSize ** 2)
        OutImg = cv.filter2D(self.Image, -1, self.kernel)
        return OutImg


class ImageBlurring(LowPassWindow):
    def __init__(self):
        super().__init__()
        self.Slider.setRange(1, 15)

    def SetImg(self):
        OutImg = cv.blur(self.Image, (self.KernelSize, self.KernelSize))
        return OutImg


class GaussBlurring(LowPassWindow):
    def __init__(self):
        super().__init__()
        self.Slider.setRange(1, 15)

    def SetImg(self):
        OutImg = cv.GaussianBlur(self.Image, (self.KernelSize, self.KernelSize), 0)
        return OutImg


class MedianBlurring(LowPassWindow):
    def __init__(self):
        super().__init__()
        self.Slider.setRange(1, 15)

    def SetImg(self):
        OutImg = cv.medianBlur(self.Image, self.Noise)
        return OutImg


class BilateralFiltering(LowPassWindow):
    def __init__(self):
        super().__init__()
        self.Slider.setRange(1, 15)

    def SetImg(self):
        OutImg = cv.bilateralFilter(self.Image, 9, 75, 75)
        return OutImg
