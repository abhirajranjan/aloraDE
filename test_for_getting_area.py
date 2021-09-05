from PyQt5 import QtWidgets, QtGui, QtCore
import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck, Gdk

#linux
class Container(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.embed('xterm')

    def embed(self, command, *args):
        #proc = QtCore.QProcess()
        #proc.setProgram(command)
        #proc.setArguments(args)

        #started, procId = proc.startDetached(command, ['/bin/bash'], '.')
        #if not started:
        #    QtWidgets.QMessageBox.critical(self, f'command "{command}" not started')
        #    return

        self.widget = QtWidgets.QWidget(self)
        id = self.widget.winId()

        window = QtGui.QWindow.fromWinId(id)
        container = QtWidgets.QWidget.createWindowContainer(window, self)
        self.addTab(container, command)
        self.setWindowTitle('zero')

        '''attempts = 0
        while attempts < 10:
            screen = Wnck.Screen.get_default()
            screen.force_update()

            while Gdk.events_pending():
                Gdk.event_get()

            for w in screen.get_windows():
                if w.get_pid() == procId:
                    window = QtGui.QWindow.fromWinId(w.get_xid())
                    container = QtWidgets.QWidget.createWindowContainer(window, self)
                    self.addTab(container, command)
                    self.setWindowTitle('zero')
                    return

            attempts += 1'''
        QtWidgets.QMessageBox.critical(self, 'Window not found', 'Process started but window not found')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainWindow = Container()
    mainWindow.show()
    app.exec()
