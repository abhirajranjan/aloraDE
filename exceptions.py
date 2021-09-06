class baseException(Exception):
    def __repr__(self):
        return f'{self.condition.strip()} [{self.code}]: {self.message}'


class ConfigFileNotFoundError(baseException):
    def __init__(self):
        self.condition = 'C'
        self.message = 'Config File \'shell.conf\' not found'
        self.code = 404


class KeyNotFoundError(baseException):
    def __init__(self, key, ensureKeys=[]):
        self.condition = 'C'
        if not ensureKeys:
            self.message = f'Config file does not contain \'{key}\' key.'
        else:
            self.message = f'Config file does not contain subkey {ensureKeys} in \'{key}\''
        self.code = 500.14


class wallpaperException(Exception):
    def __init__(self, message, errorCode):
        self.message = message
        self.errorCode = errorCode

    def __repr__(self):
        return f'W: WallpaperException[{self.errorCode}]: {self.message}.' \
               f'To reset wallpaper config run app -reset-config.' \
               '\n[Info]: setting up default wallpaper'
