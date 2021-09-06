import os
import json
import exceptions


def loadConfig(key, ensure=[]):
    if not os.path.lexists('shell.conf'):
        return exceptions.ConfigFileNotFoundError()

    try:
        with open('shell.conf') as configFile:
            config = json.load(configFile)
    except Exception as e:
        return e

    if not key:
        return config

    if key in config:
        requiredDict = config[key]
        if ensure:
            if not all(map(lambda x: x in requiredDict, ensure)):
                return exceptions.KeyNotFoundError(key, ensureKeys=ensure)
        return requiredDict
    else:
        return exceptions.KeyNotFoundError(key)
