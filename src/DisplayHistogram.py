from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Histogram(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas, stretch = 1)
        vertical_layout.addWidget(self.toolbar)
        self.canvas.sumbu1 = self.canvas.figure.add_subplot(111)

        self.canvas.figure.set_facecolor("xkcd:wheat")
        self.setLayout(vertical_layout)