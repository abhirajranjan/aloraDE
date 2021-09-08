from PyQt5 import QtWidgets, QtGui, QtCore


class taskbar(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent().resizeEventSignal.connect(self.refresh)

    @QtCore.pyqtSlot(QtCore.QSize)
    def refresh(self, size):
        self.resize(size.width(), 100)
        self.move(0, 0)

    def paintEvent(self, e):
        self.pixmap = QtGui.QPixmap(self.size())
        qp = QtGui.QPainter(self)
        self.pixmap.fill(QtGui.QColor.fromRgb(0, 0, 0))
        qp.drawPixmap(0, 0, self.pixmap)