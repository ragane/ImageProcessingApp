import sys
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
    QPushButton,
    QSlider,
)


class TransformWindow(QWidget):
    @abstractmethod
    def __init__(self):
        super(TransformWindow, self).__init__()
        