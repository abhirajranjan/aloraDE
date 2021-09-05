from PyQt5 import QtCore, QtGui, QtWidgets
import shell
import backgroundIntegration

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
        self.mainFrame.upperFrame.btn.clicked.connect(self.updateWallpaper)

        self.mainFrame.lowerFrame.moveLeftBtn = QtWidgets.QPushButton(self.mainFrame.lowerFrame)
        self.mainFrame.lowerFrame.moveLeftBtn.setObjectName('moveLeftBtn')

        self.mainFrame.lowerFrame.moveRightBtn = QtWidgets.QPushButton(self.mainFrame.lowerFrame)
        self.mainFrame.lowerFrame.moveRightBtn.setObjectName('moveRightBtn')

        self.mainFrame.lowerFrame.moveLeftBtn.clicked.connect(self.moveWidget)
        self.mainFrame.lowerFrame.moveRightBtn.clicked.connect(self.moveWidget)

        self.mainFrame.lowerFrame.layout.addWidget(self.mainFrame.lowerFrame.moveLeftBtn)
        self.mainFrame.lowerFrame.layout.addWidget(self.mainFrame.lowerFrame.moveRightBtn)

        self.mainFrame.upperFrame.layout.addWidget(self.mainFrame.upperFrame.btn)

        self.mainFrame.layout.addWidget(self.mainFrame.upperFrame)
        self.mainFrame.layout.addWidget(self.mainFrame.lowerFrame)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.raise_()
        super().mousePressEvent(a0)


class main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.wid = widget(self)
        self.newwid = widget(self)
        self.cwindow = backgroundIntegration.wallpaperManager(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.cwindow)

        self.layout.setContentsMargins(0, 0, 0, 0)

        self.wid.raise_()
        self.newwid.raise_()

        self.newwid.resize(300, 300)
        self.newwid.move(100, 100)

        self.wid.resize(300, 300)
        self.wid.move(100, 100)

        self.resize(500, 500)
        self.wid.loadGraphicsEffect()
        self.wid.updateWallpaper()
        self.newwid.loadGraphicsEffect()
        self.newwid.updateWallpaper()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = main()
    main.show()
    app.exec()
