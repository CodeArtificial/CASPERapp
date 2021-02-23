# Each widget used for matlab potting needs its own file to be promoted to it within
# the Qt editor. This file is for the line graph of repeats vs. seeds. This just initializes
# the widget to be a matplotlib plot
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from matplotlib.figure import Figure

class pop_analysis_repeats_graph(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvasQTAgg(Figure(figsize=(4,2)))

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.figure.set_visible(False)
        self.setLayout(vertical_layout)
        self.canvas.figure.tight_layout()
