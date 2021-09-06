from PyQt5 import QtWidgets, QtGui, QtCore

class titleBarButton(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.normal = ''
        self.active = ''
        self.hover = ''
        self.resize(32, 32)
        self.func = None

    # TODO :: SVG support in titlebar button icons
    def enterEvent(self, a0: QtCore.QEvent) -> None:
        if self.hover:
            pixmap = QtGui.QPixmap()
            pixmap.load(self.hover)
            self.setPixmap(pixmap)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        if self.normal:
            pixmap = QtGui.QPixmap()
            pixmap.load(self.normal)
            self.setPixmap(pixmap)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.active:
            pixmap = QtGui.QPixmap()
            pixmap.load(self.active)
            self.setPixmap(pixmap)

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.hover:
            pixmap = QtGui.QPixmap()
            pixmap.load(self.hover)
            self.setPixmap(pixmap)

        # TODO :: maybe user pressed by mistake and move away cursor while btn being pressed
        if self.func:
            self.func()

class titleBar(QtWidgets.QWidget):
    minimizing = QtCore.pyqtSignal()
    maximizing = QtCore.pyqtSignal()
    closing = QtCore.pyqtSignal()
    shading = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QHBoxLayout(self)

        self.leftFrame = QtWidgets.QFrame(self)
        self.centralFrame = QtWidgets.QFrame(self)
        self.rightFrame = QtWidgets.QFrame(self)

        self.horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalSpacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(4)

        self.layout.addWidget(self.leftFrame)
        self.layout.addItem(self.horizontalSpacer)
        self.layout.addWidget(self.centralFrame)
        self.layout.addItem(self.horizontalSpacer1)
        self.layout.addWidget(self.rightFrame)

        self.leftFrame.layout = QtWidgets.QHBoxLayout(self.leftFrame)
        self.centralFrame.layout = QtWidgets.QHBoxLayout(self.centralFrame)
        self.rightFrame.layout = QtWidgets.QHBoxLayout(self.rightFrame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.leftFrame.setSizePolicy(sizePolicy)
        self.rightFrame.setSizePolicy(sizePolicy)
        self.setSizePolicy(sizePolicy)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.centralFrame.setSizePolicy(sizePolicy)

        self.icon = None
        self.refreshUI()

    def setTitle(self, title: str):
        if hasattr(self, "title"):
            self.title.setText(title)

    def refreshUI(self):
        self.loadConfig()

        size = self.config.get('style', dict()).get('general', dict()).get('icon-size', 18)

        for config_name, ref_name in {'leftFrame_color': self.leftFrame,
                                      'centralFrame_color': self.centralFrame,
                                      'rightFrame_color': self.rightFrame}.items():

            color = self.config.get('style', dict()).get('general', dict()).get(config_name, [0, 0, 0, 0])

            ref_name.setStyleSheet(f'background-color: rgba{tuple(color)}')

        for i in self.config['items']:
            if i == 'leftFrame':
                place = self.leftFrame
            elif i == 'centralFrame':
                place = self.centralFrame
            elif i == 'rightFrame':
                place = self.rightFrame
            else:
                # TODO :: titlebar Config Exceptions
                continue

            for item in self.config['items'][i]:
                if item == 'icon':
                    self.icon = QtWidgets.QLabel(self)
                    self.icon.setObjectName('icon')

                    place.layout.addWidget(self.icon)

                    pixmap = QtGui.QPixmap()
                    pixmap.load(self.config.get('style', dict()).get('icon', dict()).get('url', ''))
                    self.icon.setPixmap(pixmap)
                    self.icon.setScaledContents(True)

                    self.icon.setMaximumSize(size, size)
                    self.icon.setMinimumSize(size, size)

                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)

                    self.icon.setSizePolicy(sizePolicy)

                    self.icon.setStyleSheet('background: transparent;')

                elif item == 'title':
                    self.title = QtWidgets.QLabel(self)
                    self.title.setObjectName('title')

                    place.layout.addWidget(self.title)

                    font = QtGui.QFont(self.config.get('style', dict()).get('title', dict()).get('font', 'monospace'),
                                       self.config.get('style', dict()).get('title', dict()).get('size', 8))
                    self.title.setFont(font)

                    self.title.setStyleSheet('background: transparent;')

                elif item == 'shade':
                    self.shade = titleBarButton(self)
                    self.shade.setObjectName('shade')
                    place.layout.addWidget(self.shade)
                    self.shade.normal = self.config.get('style', dict()).get('shade', dict()).get('normal',
                                                                                                    '')
                    self.shade.active = self.config.get('style', dict()).get('shade', dict()).get('clicked',
                                                                                                    '')
                    self.shade.hover = self.config.get('style', dict()).get('shade', dict()).get('hover',
                                                                                                   '')
                    self.shade.func = self.shading.emit()

                    self.shade.setScaledContents(True)

                    self.shade.setMaximumSize(size, size)
                    self.shade.setMinimumSize(size, size)

                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)

                    self.shade.setSizePolicy(sizePolicy)

                    self.shade.setStyleSheet('background: transparent;')

                elif item == 'minimize':
                    self.minimize = titleBarButton(self)
                    self.minimize.setObjectName('minimize')

                    place.layout.addWidget(self.minimize)

                    self.minimize.normal = self.config.get('style', dict()).get('minimize', dict()).get('normal',
                                                                                                        '')
                    self.minimize.active = self.config.get('style', dict()).get('minimize', dict()).get('clicked',
                                                                                                        '')
                    self.minimize.hover = self.config.get('style', dict()).get('minimize', dict()).get('hover',
                                                                                          '')
                    self.minimize.func = self.minimizing.emit

                    self.minimize.setScaledContents(True)

                    self.minimize.setMaximumSize(size, size)
                    self.minimize.setMinimumSize(size, size)

                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)

                    self.minimize.setSizePolicy(sizePolicy)

                    self.minimize.setStyleSheet('background: transparent;')

                elif item == 'maximize':
                    self.maximize = titleBarButton(self)
                    self.maximize.setObjectName('maximize')

                    place.layout.addWidget(self.maximize)

                    self.maximize.normal = self.config.get('style', dict()).get('maximize', dict()).get('normal',
                                                                                                        '')
                    self.maximize.active = self.config.get('style', dict()).get('maximize', dict()).get('clicked',
                                                                                                        '')
                    self.maximize.hover = self.config.get('style', dict()).get('maximize', dict()).get('hover',
                                                                                                       '')
                    self.maximize.func = self.maximizing.emit

                    self.maximize.setScaledContents(True)

                    self.maximize.setMaximumSize(size, size)
                    self.maximize.setMinimumSize(size, size)

                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)

                    self.maximize.setSizePolicy(sizePolicy)

                    self.maximize.setStyleSheet('background: transparent;')

                elif item == 'close':
                    self.close = titleBarButton(self)
                    self.close.setObjectName('close')

                    place.layout.addWidget(self.close)
                    self.close.normal = self.config.get('style', dict()).get('close', dict()).get('normal',
                                                                                                        '')
                    self.close.active = self.config.get('style', dict()).get('close', dict()).get('clicked',
                                                                                                        '')
                    self.close.hover = self.config.get('style', dict()).get('close', dict()).get('hover',
                                                                                                       '')
                    self.close.func = self.closing.emit

                    self.close.setScaledContents(True)

                    self.close.setMaximumSize(size, size)
                    self.close.setMinimumSize(size, size)

                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)

                    self.close.setSizePolicy(sizePolicy)

                    self.close.setStyleSheet('background: transparent;')

        super().update()

    def loadConfig(self):
        config = self.window().loadConfig('titlebar', ensure=['items', 'style'])
        if config:
            self.config = config


class windowShell(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wallpaperCover = QtWidgets.QFrame(self)
        self.wallpaperCover.layout = QtWidgets.QHBoxLayout(self.wallpaperCover)
        self.wallpaper = QtWidgets.QLabel(self)
        self.wallpaper.pixmap = QtGui.QPixmap(self.size())

        self.wallpaperCover.layout.setContentsMargins(0, 0, 0, 0)
        self.wallpaperCover.layout.addWidget(self.wallpaper)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.wallpaperCover)

        self.tb = titleBar(self)

        self.centralFrame = QtWidgets.QFrame(self)
        self.centralFrame.layout = QtWidgets.QVBoxLayout(self.centralFrame)

        self.mainFrame = QtWidgets.QFrame(self.centralFrame)

        self.horizontalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                      QtWidgets.QSizePolicy.Expanding)

        self.centralFrame.layout.setContentsMargins(0, 0, 0, 0)
        self.centralFrame.layout.setSpacing(0)

        self.centralFrame.layout.addWidget(self.tb)
        self.centralFrame.layout.addItem(self.horizontalSpacer)
        self.centralFrame.layout.addWidget(self.mainFrame)

        self.loadGraphicsEffect()
        self.readConf()

    def readConf(self):
        config = self.window().loadConfig('shell', ensure=['general'])
        if not config: return
        self.config = config

        if self.config['general']['offset']:
            self.layout.setContentsMargins(*self.config['general']['offset'])

    def setTitle(self, title: str):
        self.tb.setTitle(title)

    @QtCore.pyqtSlot()
    def loadGraphicsEffect(self):
        self.dropShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.dropShadow.setBlurRadius(50)
        self.dropShadow.setColor(QtGui.QColor(40, 40, 40, 225))
        self.dropShadow.setOffset(0, 10)

        self.blur = QtWidgets.QGraphicsBlurEffect()
        self.blur.setBlurRadius(8)

        self.wallpaper.setGraphicsEffect(self.blur)

        self.wallpaperCover.setStyleSheet('background-color:rgba(3, 3, 3, 100)')

    @QtCore.pyqtSlot()
    def unloadGraphicsEffect(self):
        self.wallpaper.setGraphicsEffect(None)

        self.wallpaper.pixmap = QtGui.QPixmap(self.size())
        self.wallpaper.pixmap.fill(QtCore.Qt.transparent)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super().resizeEvent(a0)
        self.centralFrame.resize(self.size())

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.oldPos = a0.globalPos()
        self.setFocus()
        self.updateWallpaper()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        delta = QtCore.QPoint(a0.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = a0.globalPos()
        self.loadGraphicsEffect()
        self.updateWallpaper()

    ## blur
    # general approch
    def applyEffectToImage(self, pixmap: QtGui.QPixmap, effect: QtWidgets.QGraphicsEffect, extend: int = 0):
        if pixmap.isNull(): return QtGui.QPixmap()
        if not effect: return pixmap
        scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem()
        item.setPixmap(pixmap)
        item.setGraphicsEffect(effect)
        scene.addItem(item)

        res = QtGui.QPixmap(QtCore.QSize(pixmap.width() + extend * 2, pixmap.height() + extend * 2))
        res.fill(QtCore.Qt.transparent)

        ptr = QtGui.QPainter(res)
        scene.render(ptr, QtCore.QRectF(), QtCore.QRectF(-extend, -extend, pixmap.width() + extend * 2, \
                                                         pixmap.height() + extend * 2))
        return res

    @QtCore.pyqtSlot()
    def updateWallpaper(self):
        self.hide()
        self.blockSignals(True)
        self.wallpaper.pixmap = self.parent().grab(QtCore.QRect(self.x(), self.y(), self.width(), self.height()))
        self.wallpaper.setPixmap(self.wallpaper.pixmap)
        self.blockSignals(False)
        self.show()
