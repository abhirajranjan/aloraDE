from PyQt5 import QtGui, QtWidgets
import os
import exceptions


class wallpaperManager(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pixmap = QtGui.QPixmap()
        self.pixmap.fill(QtGui.QColor.fromRgb(12, 12, 12))
        self.refreshConfig()

    def refreshConfig(self):
        config = self.parent().loadConfig('Wallpaper', ensure=['wallpaperStyle', 'wallpaperType'])
        if not config: return
        self.config = config

        self.loadConfig(self.config)

    def loadConfig(self, config):
        if not config["wallpaperType"] in config['wallpaperStyle']:
            return exceptions.wallpaperException(f'unknown wallpaperType "{config["wallpaperType"]}" selected', 500.19)

        wallpaperStyle = config['wallpaperStyle'][config['wallpaperType']]

        if config['wallpaperType'] == 'ColorType':
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

        elif config['wallpaperType'] == "SingleType":
            if (not os.path.lexists(wallpaperStyle["URI"])) or (not os.path.isfile(wallpaperStyle["URI"])):
                return exceptions.wallpaperException(f'wallpaper image not found at "{wallpaperStyle["URI"]}"', 404)

            # TODO :: implement VODs in wallpaper

            self.pixmap.load(wallpaperStyle['URI'])

    def paintEvent(self, e):
        self.painter = QtGui.QPainter(self)
        self.painter.drawPixmap(self.rect(), self.pixmap)
        self.painter.end()
