import backgroundIntegration
from PyQt5 import QtWidgets
import customFunctions
import window


class main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.activeWindow = {}

        self.backgroundWallaper = backgroundIntegration.wallpaperManager(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.backgroundWallaper)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.testShell()

    def loadConfig(self, *args, **kwargs):
        isConfig = customFunctions.loadConfig(*args, **kwargs)
        if issubclass(type(isConfig), Exception):
            # TODO :: handle exceptions in main Frame, info it out Maybe ?
            return
        return isConfig

    def testShell(self):
        self.test_widget = window.widget(self)
        self.test_widget.setTitle('main app: runtime')
        self.loadApp(self.test_widget)

    def loadApp(self, wid: QtWidgets.QWidget):
        # register wid to active list
        self.activeWindow[id(wid)] = wid

        wid.resize(500, 500)

        wid.show()
        wid.raise_()
        wid.setFocus()

        wid.loadGraphicsEffect()
        wid.updateWallpaper()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainApp = main()
    mainApp.resize(100, 100)
    mainApp.show()
    app.exec()