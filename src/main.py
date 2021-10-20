import eventController
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainApp = eventController.main()
    mainApp.resize(100, 100)
    mainApp.show()
    app.exec()