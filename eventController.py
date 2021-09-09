# own imports
import backgroundIntegration
import customFunctions
import taskpanel
import window

# Qt imports
from PyQt5 import QtWidgets, QtCore, QtGui


class main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.activeWindow = {}
        self.alwaysOnTop = {}

        self.alwaysOnTopWidgetList = customFunctions.LinkedList()

        self.backgroundWallaper = backgroundIntegration.wallpaperManager(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.backgroundWallaper)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.taskpanel = taskpanel.panel(self)
        self.mainWidgetArea = QtWidgets.QFrame(self)

        self.refreshAlwaysOnTopWidgetList()

        self.taskpanel.raise_()
        self.mainWidgetArea.raise_()

        self.test()

    def refreshAlwaysOnTopWidgetList(self):
        if self.taskpanel.setOnTop:
            self.setAlwaysOnTop(self.taskpanel, True)
            self.alwaysOnTopWidgetList.setLast(id(self.taskpanel))

    def raiseWidget(self, widget: QtWidgets.QWidget) -> bool:
        if id(widget) in self.alwaysOnTop:
            self.alwaysOnTopWidgetList.remove(id(widget))
            self.alwaysOnTopWidgetList.append(id(widget))
            return self._raiseWidget()

        else:
            widget.raise_()
            return self._raiseWidget()

    def _raiseWidget(self):
        for onTopWidget in self.alwaysOnTopWidgetList:
            if onTopWidget:
                self.alwaysOnTop[onTopWidget].raise_()
        return True

    def setAlwaysOnTop(self, wid: QtWidgets.QWidget, value: bool) -> bool:
        if (id(wid) in self.alwaysOnTop) and value:
            return True

        if (id(wid) in self.alwaysOnTop) and (not value):
            wid.setParent(self.mainWidgetArea)
            return self.alwaysOnTop.pop(id(wid), None)

        if not (id(wid) in self.alwaysOnTop):
            self.alwaysOnTop[id(wid)] = wid
            return True
        return False

    def loadConfig(self, *args, **kwargs):
        isConfig = customFunctions.loadConfig(*args, **kwargs)
        if issubclass(type(isConfig), Exception):
            # TODO :: handle exceptions in main Frame, info it out Maybe ?
            return
        return isConfig

    def test(self):
        self.window = window.widget(self.mainWidgetArea)
        self.loadApp(self.window)

    def loadApp(self, wid: QtWidgets.QWidget):
        # register wid to active list
        self.activeWindow[id(wid)] = wid
        wid.resize(300, 300)

        wid.show()
        wid.move(30, 30)
        wid.raise_()
        wid.setFocus()

        wid.loadGraphicsEffect()
        wid.updateWallpaper()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super().resizeEvent(a0)
        self.taskpanel.resize(self.size())
        self.mainWidgetArea.resize(self.size())


class tempClass(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, e):
        self.pixmap = QtGui.QPixmap(self.size())
        qp = QtGui.QPainter(self)
        self.pixmap.fill(QtGui.QColor.fromRgb(0, 12, 0))
        qp.drawPixmap(0 , 0, self.pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainApp = main()
    mainApp.resize(100, 100)
    mainApp.show()
    app.exec()