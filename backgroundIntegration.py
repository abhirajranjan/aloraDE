from PyQt5 import QtGui, QtCore, QtWidgets
import os
import json


class wallpaperException(Exception):
    def __init__(self, message, errorCode):
        self.message = message
        self.errorCode = errorCode

    def __repr__(self):
        return f'W: WallpaperException[{self.errorCode}]: {self.message}.' \
               f'To reset wallpaper config run app -reset-config.' \
               '\n[Info]: setting up default wallpaper'


class wallpaperManager(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pixmap = QtGui.QPixmap()
        self.pixmap.fill(QtGui.QColor.fromRgb(12, 12, 12))
        self.refreshConfig()

    def refreshConfig(self):
        if os.path.lexists(os.path.join(os.getcwd(), 'shell.conf')):
            with open('shell.conf') as file:
                self.config = json.load(file)['Wallpaper']

        self.loadConfig(self.config)

    def loadConfig(self, config):
        if not self.config["wallpaperType"] in self.config['wallpaperStyle']:
            return wallpaperException(f'unknown wallpaperType "{self.config["wallpaperType"]}" selected', 500.19)

        wallpaperStyle = self.config['wallpaperStyle'][self.config['wallpaperType']]

        if self.config['wallpaperType'] == 'ColorType':
            try:
                # TODO :: implement gradient in wallpaper
                # if wallpaperStyle['type'].lower() == 'gradient' and wallpaperStyle['Gradient_QSS']:
                if wallpaperStyle['type'].lower() == 'SolidColor':
                    self.pixmap.fill(QtGui.QColor.fromRgb(*wallpaperStyle['Color']))

            # TODO :: better Exception handling in wallpaper Config
            except Exception as e:
                raise e

        # TODO :: implement multiple photo slideshow in wallpaper
        # if self.config['WallpaperType'] == 'MultipleType':

        elif self.config['wallpaperType'] == "SingleType":
            if (not os.path.lexists(wallpaperStyle["URI"])) or (not os.path.isfile(wallpaperStyle["URI"])):
                return wallpaperException(f'wallpaper image not found at "{wallpaperStyle["URI"]}"', 404)

            # TODO :: implement VODs in wallpaper

            self.pixmap.load(wallpaperStyle['URI'])


    def paintEvent(self, e):
        self.painter = QtGui.QPainter(self)
        self.painter.drawPixmap(self.rect(), self.pixmap)
        self.painter.end()
