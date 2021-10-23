from PyQt5 import QtWidgets, QtCore, QtGui
from package import taskbar


class panel(QtWidgets.QWidget):
    resizeEventSignal = QtCore.pyqtSignal(QtCore.QSize)

    def __init__(self, parent):
        super().__init__(parent)
        self.setOnTop = True
        self.taskbar = taskbar.taskbar(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0 ,0)
        self.layout.addWidget(self.taskbar)

    def updateWallpaper(self):
        ...