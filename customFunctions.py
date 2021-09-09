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


class NodeClass:
    def __init__(self):
        self.value = None
        self.nextNode = None
        self.prevNode = None


class LinkedList:
    def __init__(self):
        self.tail = NodeClass()
        self.last = NodeClass()
        self.head = self.tail
        self.elementCount = 0
        self.last = None

    def __iter__(self):
        currNode = self.tail
        if not self.elementCount:
            return StopIteration()

        while currNode.nextNode:
            yield currNode.value
            currNode = currNode.nextNode

        yield currNode.value

    def __repr__(self):
        return f'{[i for i in self]}' if self.elementCount else ''

    def setLast(self, value):
        node = NodeClass()
        self.last = node
        self.head.nextNode = node
        self.last.value = value
        self.elementCount += 1
        return True

    def removeLast(self):
        if not self.last:
            return True

        del self.last
        self.head.nextNode = None
        self.elementCount -= 1
        return True

    def append(self, value):
        if (not self.elementCount) or (self.last and (self.elementCount == 1)):
            self.head.value = value
            self.elementCount += 1
            return True

        node = NodeClass()
        if self.last:
            node.nextNode = self.last

        self.head.nextNode = node
        self.head = node
        self.head.value = value
        self.elementCount += 1
        return True

    def remove(self, value):
        probably_this_node = self.tail

        if probably_this_node.value == value:
            self.tail = probably_this_node.nextNode
            self.elementCount -= 1
            return True

        if not hasattr(probably_this_node.nextNode, 'value'):
            return False

        while probably_this_node.nextNode.value != value:
            probably_this_node = probably_this_node.nextNode

            if not hasattr(probably_this_node.nextNode, 'value'):
                return False

        temp_node = probably_this_node.nextNode.nextNode

        if probably_this_node.nextNode.nextNode:
            del probably_this_node.nextNode

        probably_this_node.nextNode = temp_node
        self.elementCount -= 1
        return True
