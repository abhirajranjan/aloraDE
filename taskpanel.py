from PyQt5 import QtWidgets

class panel(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.loadConfig()
        self.getBar()

    def loadConfig(self):
        isConfig = self.parent().loadConfig('taskbar', ensure=['WidgetMainFile', 'main', 'pos'])

        if isConfig:
            self.config = isConfig

    def getBar(self):
        # temp bar, without loading config
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.pos = 'bottom'

        self.frame = QtWidgets.QFrame(self)
        self.layout.addWidget(self.frame)