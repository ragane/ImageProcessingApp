import cv2 as cv
import numpy as np
from abc import ABC, abstractmethod
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QComboBox,
    QPushButton,
    QSpinBox,
)


class GeoTransformWindow(QWidget):
    @abstractmethod
    def __init__(self):
        super(GeoTransformWindow, self).__init__()

        self.MainLayout = QVBoxLayout()
        self.SpinBoxLayout = QVBoxLayout()
        self.FirstSpinLayout = QHBoxLayout()
        self.SecondSpinLayout = QHBoxLayout()
        self.ApplyButtonLayout = QVBoxLayout()

        self.FirstSpinBox = QSpinBox()
        self.FirstLabel = QLabel(" ")

        self.SecondSpinBox = QSpinBox()
        self.SecondLabel = QLabel(" ")

        self.ApplyButton = QPushButton("Apply")
        self.setLayout(self.MainLayout)
        self.MainLayout.addLayout(self.SpinBoxLayout)
        self.SpinBoxLayout.addLayout(self.FirstSpinLayout)
        self.SpinBoxLayout.addLayout(self.SecondSpinLayout)

        self.FirstSpinLayout.addWidget(self.FirstLabel)
        self.FirstSpinLayout.addWidget(self.FirstSpinBox)

        self.SecondSpinLayout.addWidget(self.SecondLabel)
        self.SecondSpinLayout.addWidget(self.SecondSpinBox)

        self.ThirdLayout = QHBoxLayout()
        self.InterpolationBox = QComboBox()
        self.ThirdLabel = QLabel("Interpolation method: ")
        self.MainLayout.addLayout(self.ThirdLayout)
        self.ThirdLayout.addWidget(self.ThirdLabel)
        self.ThirdLayout.addWidget(self.InterpolationBox)
        self.InterpolationList = ["Inter Linear", "Inter Area", "Inter Cubic"]
        self.InterpolationBox.addItems(self.InterpolationList)

        self.MainLayout.addWidget(self.ApplyButton)

        self.FirstValue = 1
        self.SecondValue = 1
        self.Image = None
        self.rows, self.cols = 0, 0
        self.TransformMatrix = np.float32([[1, 0, 0], [0, 1, 0]])

    @abstractmethod
    def GetImg(self, image):
        self.Image = image
        self.rows, self.cols, _channel = self.Image.shape
        self.FirstSpinBox.setRange(1, self.cols)
        self.SecondSpinBox.setRange(1, self.rows)

    @QtCore.pyqtSlot(int)
    @abstractmethod
    def GetFirstValue(self, value):
        self.FirstValue = value

    @QtCore.pyqtSlot(int)
    @abstractmethod
    def GetSecondValue(self, value):
        self.SecondValue = value

    @QtCore.pyqtSlot(int)
    @abstractmethod
    def SetValue(self):
        pass


class Scaling(GeoTransformWindow):
    def __init__(self):
        super().__init__()

        self.InterpolationValue = None

        self.FirstLabel.setText("Fx value: ")
        self.FirstSpinBox.setRange(1, 200)

        self.SecondLabel.setText("Fy value: ")
        self.SecondSpinBox.setRange(1, 200)

        self.InterpolationBox.activated.connect(self.GetInterpolationValue)

    def GetInterpolationValue(self, index):

        ctext = self.InterpolationBox.itemText(index)
        if ctext == "Inter Area":
            self.InterpolationValue = cv.INTER_AREA
        elif ctext == "Inter Cubic":
            self.InterpolationValue = cv.INTER_CUBIC
        elif ctext == "Inter Linear":
            self.InterpolationValue = cv.INTER_LINEAR
        return self.InterpolationValue

    def SetValue(self):

        image = cv.resize(self.Image, None, fx = self.FirstValue, fy = self.SecondValue,
                          interpolation = self.InterpolationValue)
        return image


class Translation(GeoTransformWindow):
    def __init__(self):
        super().__init__()
        self.FirstLabel.setText("Tx value: ")
        self.SecondLabel.setText("Ty value: ")
        self.InterpolationBox.setVisible(0)
        self.ThirdLabel.setVisible(0)

    def SetValue(self):
        self.TransformMatrix = np.float32([[1, 0, self.FirstValue], [0, 1, self.SecondValue]])
        image = cv.warpAffine(self.Image, self.TransformMatrix, (self.cols, self.rows))
        return image


class Rotation(GeoTransformWindow):
    def __init__(self):
        super().__init__()
        self.FirstLabel.setText("Angle of rotation: ")
        self.FirstSpinBox.setRange(0, 360)
        self.SecondLabel.setVisible(0)
        self.SecondSpinBox.setVisible(0)
        self.InterpolationBox.setVisible(0)
        self.ThirdLabel.setVisible(0)

    def SetValue(self):
        self.TransformMatrix = cv.getRotationMatrix2D(((self.cols / 2), (self.rows / 2)), self.FirstValue, 1)
        image = cv.warpAffine(self.Image, self.TransformMatrix, (self.cols, self.rows))
        return image
