import backgroundIntegration
from PyQt5 import QtWidgets, QtCore, QtGui
import customFunctions
import taskpanel


class main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.activeWindow = {}
        self.alwaysOnTop = {}

        self.backgroundWallaper = backgroundIntegration.wallpaperManager(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.backgroundWallaper)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.taskpanel = taskpanel.panel(self)
        self.mainWidgetArea = QtWidgets.QFrame(self)
        self.alwaysOnTopArea = QtWidgets.QFrame(self)

        self.mainWidgetArea.raise_()
        self.taskpanel.raise_()
        self.alwaysOnTopArea.raise_()

    def setAlwaysOnTop(self, wid: QtWidgets.QWidget, value: bool) -> bool:
        if (id(wid) in self.alwaysOnTop) and value:
            return True

        if (id(wid) in self.alwaysOnTop) and (not value):
            wid.setParent(self.mainWidgetArea)
            return self.alwaysOnTop.pop(id(wid), None)

        if not (id(wid) in self.alwaysOnTop):
            wid.setParent(self.alwaysOnTopArea)
            self.alwaysOnTop[id(wid)] = wid
            return True
        return False

    def loadConfig(self, *args, **kwargs):
        isConfig = customFunctions.loadConfig(*args, **kwargs)
        if issubclass(type(isConfig), Exception):
            # TODO :: handle exceptions in main Frame, info it out Maybe ?
            return
        return isConfig

    def loadApp(self, wid: QtWidgets.QWidget):
        # register wid to active list
        self.activeWindow[id(wid)] = wid
        wid.resize(500, 500)

        wid.show()
        wid.raise_()
        wid.setFocus()

        wid.loadGraphicsEffect()
        wid.updateWallpaper()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super().resizeEvent(a0)
        self.alwaysOnTopArea.resize(self.size())
        self.taskpanel.resize(self.size())
        self.mainWidgetArea.resize(self.size())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainApp = main()
    mainApp.resize(100, 100)
    mainApp.show()
    app.exec()