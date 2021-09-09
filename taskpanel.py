from PyQt5 import QtWidgets, QtCore, QtGui
from package import taskbar


class panel(QtWidgets.QWidget):
    resizeEventSignal = QtCore.pyqtSignal(QtCore.QSize)

    def __init__(self, parent):
        super().__init__(parent)
        self.setOnTop = True
        self.taskbar = taskbar.taskbar(self)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.resizeEventSignal.emit(self.size())
        super().resizeEvent(a0)
