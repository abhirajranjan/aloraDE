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

        self.taskpanel.setObjectName('taskbar')

        self.refreshAlwaysOnTopWidgetList()

        self.mainWidgetArea.raise_()

        self.test()

    def refreshAlwaysOnTopWidgetList(self):
        if self.taskpanel.setOnTop:
            self.alwaysOnTop[id(self.taskpanel)] = self.taskpanel
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
            self.alwaysOnTopWidgetList.remove(id(wid))
            return self.alwaysOnTop.pop(id(wid), None)

        if not (id(wid) in self.alwaysOnTop):
            self.alwaysOnTopWidgetList.append(id(wid))
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
        self.window1 = window.widget(self.mainWidgetArea)
        self.window2 = window.widget(self.mainWidgetArea)
        self.window3 = window.widget(self.mainWidgetArea)

        self.window1.setObjectName('widget1')
        self.window2.setObjectName('widget2')
        self.window3.setObjectName('widget3')

        self.window1.setTitle('window1')
        self.window2.setTitle('window2')
        self.window3.setTitle('window3')

        self.setAlwaysOnTop(self.window2, True)

        self.loadApp(self.window1)
        self.loadApp(self.window2)
        self.loadApp(self.window3)

    def loadApp(self, wid: QtWidgets.QWidget):
        # register wid to active list
        self.activeWindow[id(wid)] = wid
        wid.resize(300, 300)

        wid.show()
        wid.move(30, 30)
        # wid.raise_()
        # wid.setFocus()

        wid.loadGraphicsEffect()
        wid.updateWallpaper()

    def grabByArea(self, widget, areas):
        returnData = []
        for area in areas:
            returnData.append(self.grab(area))
        return returnData

    def grabBackground(self, widget, areas={}):
        temp = {}
        if widget in self.alwaysOnTop:
            return self.grabByArea(widget, areas=areas)

        for alwaysOnTopWidgetID in self.alwaysOnTop:
            # TODO :: better method to hide sp widget probably using sets or updating blur algo
            if self.alwaysOnTop[alwaysOnTopWidgetID]:
                if self.alwaysOnTop[alwaysOnTopWidgetID].isVisible():
                    temp[alwaysOnTopWidgetID] = True
                    self.alwaysOnTop[alwaysOnTopWidgetID].hide()

        to_return = self.grabByArea(widget, areas=areas)

        for alwaysOnTopWidgetID in temp:
            self.alwaysOnTop[alwaysOnTopWidgetID].show()

        return to_return

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super().resizeEvent(a0)
        self.taskpanel.resizeEventSignal.emit(self.size())
        self.mainWidgetArea.resize(self.size())