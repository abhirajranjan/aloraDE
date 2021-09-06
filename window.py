from PyQt5 import QtCore, QtGui, QtWidgets
import shell


class widget(shell.windowShell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.mainFrame.layout = QtWidgets.QVBoxLayout(self.mainFrame)

        self.mainFrame.upperFrame = QtWidgets.QFrame(self.mainFrame)
        self.mainFrame.lowerFrame = QtWidgets.QFrame(self.mainFrame)

        self.mainFrame.upperFrame.layout = QtWidgets.QVBoxLayout(self.mainFrame.upperFrame)
        self.mainFrame.lowerFrame.layout = QtWidgets.QHBoxLayout(self.mainFrame.lowerFrame)

        self.mainFrame.upperFrame.btn = QtWidgets.QPushButton(self)
        self.mainFrame.upperFrame.btn.setText('Shoot')

        self.mainFrame.lowerFrame.moveLeftBtn = QtWidgets.QPushButton(self.mainFrame.lowerFrame)
        self.mainFrame.lowerFrame.moveLeftBtn.setObjectName('moveLeftBtn')

        self.mainFrame.lowerFrame.moveRightBtn = QtWidgets.QPushButton(self.mainFrame.lowerFrame)
        self.mainFrame.lowerFrame.moveRightBtn.setObjectName('moveRightBtn')

        self.mainFrame.lowerFrame.layout.addWidget(self.mainFrame.lowerFrame.moveLeftBtn)
        self.mainFrame.lowerFrame.layout.addWidget(self.mainFrame.lowerFrame.moveRightBtn)

        self.mainFrame.upperFrame.layout.addWidget(self.mainFrame.upperFrame.btn)

        self.mainFrame.layout.addWidget(self.mainFrame.upperFrame)
        self.mainFrame.layout.addWidget(self.mainFrame.lowerFrame)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.raise_()
        super().mousePressEvent(a0)
