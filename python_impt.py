from PyQt5 import QtGui, QtCore, QtWidgets

QtGui.QRegion()

class Region:
    def __init__(self, rects):
        toremove = []
        for i in range(1, len(rects)):
            # what if all X-points of i are inside i-1 ?
            if (rects[i-1][0] <= rects[i][0], rects[i][0] + rects[i][2] <= rects[i-1][0] + rects[i-1][2]) == (True, True):

                # what if all Y-points of i are inside i-1 ?
                if (rects[i-1][1] <= rects[i][1], rects[i][1] + rects[i][3] <= rects[i-1][1] + rects[i-1][3]) == (True, True):
                    toremove.append(i)

                # what if location point of i is in area i-1 bt height  Y-point is outside i-1 ?
                elif (rects[i-1][1] <= rects[i][1], rects[i][1] + rects[i][3] <= rects[i-1][1] + rects[i-1][3]) == (True, False):
                    rects[i][3] -= rects[i-1][1] + rects[i-1][3] - rects[i][1]
                    rects[i][1]  = rects[i-1][1] + rects[i-1][3]

                # what if location point of i is not in area i-1 bt height Y-point is inside i-1 ?
                elif (rects[i-1][1] <= rects[i][1], rects[i][1] + rects[i][3] <= rects[i-1][1] + rects[i-1][3]) == (False, True):
                    rects[i][3] -= rects[i][1] + rects[i][3] - rects[i-1][1]

                # what if all Y-points of i doesnt lie inside i-1 ?
                elif (rects[i-1][1] <= rects[i][1], rects[i][1] + rects[i][3] <= rects[i-1][1] + rects[i-1][3]) == (False, False):
                    if not (rects[i][1] >= rects[i-1][1] + rects[i-1][3] or rects[i][1] + rects[i][3] <= rects[i-1][1]):
                        toremove.append(i)
                        upperRect =  lowerRect  = rects[i]

                        upperRect[3] -= rects[i][1] + rects[i][3] - rects[i-1][1]

                        lowerRect[3] -= rects[i-1][1] + rects[i-1][3] - rects[i][1]
                        lowerRect[1]  = rects[i-1][1] + rects[i-1][3]

                        rects.append(lowerRect)
                        rects.append(upperRect)

        self.rects = rects


    def union(self, anotherRegion):
        if self.hasMixedSelection:
            if anotherRegion.hasMixedSelection:
                for i in anotherRegion.rects:


class widgetGetter:
    def __init__(self):
        self.windows = []

    def mergeSelection(self, array):
        if len(array) == 1:
            return array

        if len(array) == 2:
            if array[1].union(array[0]) == array[1]:
                return array[1]
            if array[0].union(array[1]) == array[0]:
                return array[0]
            if

        return self.mergeSort(array[:len(array)//2]) + \
               self.mergeSort(array[len(array)//2:])



    def getRegion(self, x, y, height, width):

