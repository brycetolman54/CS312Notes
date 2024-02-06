from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
    from PyQt5.QtCore import QLineF, QPointF, QObject
elif PYQT_VER == 'PYQT4':
    from PyQt4.QtCore import QLineF, QPointF, QObject
elif PYQT_VER == 'PYQT6':
    from PyQt6.QtCore import QLineF, QPointF, QObject
else:
    raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))



import time

# Some global color constants that might be useful
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

# Global variable that controls the speed of the recursion automation, in seconds
PAUSE = 2

#
# This is the class you have to complete.
#
class ConvexHullSolver(QObject):

# Class constructor
    def __init__( self):
        super().__init__()
        self.pause = True

# Some helper methods that make calls to the GUI, allowing us to send updates
# to be displayed.

    def showTangent(self, line, color):
        self.view.addLines(line,color)
        if self.pause:
            time.sleep(PAUSE)

    def eraseTangent(self, line):
        self.view.clearLines(line)

    def blinkTangent(self,line,color):
        self.showTangent(line,color)
        self.eraseTangent(line)

    def showHull(self, polygon, color):
        self.view.addLines(polygon,color)
        if self.pause:
            time.sleep(PAUSE)

    def eraseHull(self,polygon):
        self.view.clearLines(polygon)

    def showText(self,text):
        self.view.displayStatusText(text)


# This is the method that gets called by the GUI and actually executes
# the finding of the hull
    def compute_hull( self, points, pause, view):
        self.pause = pause
        self.view = view
        assert( type(points) == list and type(points[0]) == QPointF )

        t1 = time.time()
        points = self.MergeSort(points)
        t2 = time.time()

        t3 = time.time()
        hull = self.ConvexHull(points)
        t4 = time.time()

        # when passing lines to the display, pass a list of QLineF objects.  Each QLineF
        # object can be created with two QPointF objects corresponding to the endpoints
        
        # build the polygon
        hullPoints = hull.points
        lengthHull = len(hullPoints)
        polygon = list(range(lengthHull))

        for i in range(lengthHull):
            polygon[i] = QLineF(hullPoints[i], hullPoints[(i + 1) % lengthHull])

        self.showHull(polygon,RED)
        self.showText('Time Elapsed (Convex Hull): {:3.3f} sec'.format(t4-t3))

    # Functions to do the Sorting of the points
    def MergeSort(self, points):

        # see if we are down to one value; if not, we can recursively call down and split the list in half
        length = len(points)        
        if length == 1:
            return points
        else:
            return self.Merge(self.MergeSort(points[:(length // 2)]), self.MergeSort(points[(length // 2):]))

    def Merge(self, points1, points2):

        # see if either array is empty
        if points1 == None or len(points1) == 0:
            return points2
        elif points2 == None or len(points2) == 0:
            return points1
        
        # make a new array of the proper size and fill it in iteratively
        length1 = len(points1)
        length2 = len(points2)
        newArray = list(range(length1 + length2))

        # these will be the indicies we access in the arrays we have to compare them
        i = 0
        j = 0
        
        # loop through until the whole array is built, one by one by the lowest value of the two arrays
        for k in range(0, length1 + length2):
            if i == length1:
                for l in range(0, length2 - j):
                    newArray[l + k] = points2[l + j]
                break
            elif j == length2:
                for l in range(0, length1 - i):
                    newArray[l + k] = points1[l + i]
                break
            elif points1[i].x() <= points2[j].x():
                newArray[k] = points1[i]
                i += 1
            else:
                newArray[k] = points2[j]
                j += 1

        return newArray

    # Functions to do the Hull Splitting and Merge
    def ConvexHull(self, points):
        
        length = len(points)

        # check for the base case and create the first hulls
        if length <= 3:
            
            # deal with it if only two points
            if length < 3: 

                # create the new array, add to it the two points and the right most position's index
                newHull = Hull(points, 1)

            # deal with it if there are three points, do the same as above but compare slopes to order the other two points that are not the left most
            else:

                if GetSlope(points[0], points[1]) >= GetSlope(points[0], points[2]):
                    newHull = Hull(points, 2)
                else: 
                    newHull = Hull([points[0], points[2], points[1]], 1)

            return newHull

        # or split the array further until we get to the base case
        else:
            return self.MergeHull(self.ConvexHull(points[:(length // 2)]), self.ConvexHull(points[(length // 2):]))

    def MergeHull(self, leftPoints, rightPoints):
        
        # get the hulls
        leftHull = leftPoints.points
        rightHull = rightPoints.points

        # get the hull lengths for later use
        leftMod = len(leftHull)
        rightMod = len(rightHull)

    # UPPER TANGENT FIRST

        # get values with which to iterate over points to find the tangent lines, rightmost on left hull and leftmost on right hull 
        leftFirstPoint = leftPoints.rightMost
        rightFirstPoint = 0

        # initialize the variables for the while loop to make sure it stops when we are no longer moving the tangent line
        goodLeft = False
        goodRight = False

        while not goodLeft or not goodRight:

            # restart the booleans
            goodLeft = True
            goodRight = True

            # move the left side first, then the right
            while True:
                newLeftPoint = (leftFirstPoint - 1) % leftMod
                if GetSlope(leftHull[newLeftPoint], rightHull[rightFirstPoint]) <= GetSlope(leftHull[leftFirstPoint], rightHull[rightFirstPoint]):
                    leftFirstPoint = newLeftPoint
                    goodLeft = False
                else: 
                    break
            while True:
                newRightPoint = (rightFirstPoint + 1) % rightMod
                if GetSlope(rightHull[newRightPoint], leftHull[leftFirstPoint]) >= GetSlope(rightHull[rightFirstPoint], leftHull[leftFirstPoint]):
                    rightFirstPoint = newRightPoint
                    goodRight = False
                else:
                    break

    # NOW LOWER TANGENT
                
        goodLeft = False
        goodRight = False 

        # get values with which to iterate over points to find the tangent lines, rightmost on left hull and leftmost on right hull
        leftLastPoint = leftPoints.rightMost
        rightLastPoint = 0

        while not goodLeft or not goodRight:

            # restart the booleans
            goodLeft = True
            goodRight = True

            # move the left side first, then the right
            while True:
                newLeftPoint = (leftLastPoint + 1) % leftMod
                if GetSlope(leftHull[newLeftPoint], rightHull[rightLastPoint]) >= GetSlope(leftHull[leftLastPoint], rightHull[rightLastPoint]):
                    leftLastPoint = newLeftPoint
                    goodLeft = False
                else: 
                    break
            while True:
                newRightPoint = (rightLastPoint - 1) % rightMod
                if GetSlope(rightHull[newRightPoint], leftHull[leftLastPoint]) <= GetSlope(rightHull[rightLastPoint], leftHull[leftLastPoint]):
                    rightLastPoint = newRightPoint
                    goodRight = False
                else:
                    break
                
        # construct the new array to return after getting the sub arrays we need 
        firstPartLeftHull = leftHull[:leftFirstPoint + 1]
        l1 = len(firstPartLeftHull)
        if leftLastPoint == 0:
            secondPartLeftHull = []
        else:
            secondPartLeftHull = leftHull[leftLastPoint:]
        l3 = len(secondPartLeftHull)
        if rightLastPoint == 0:
            middlePartRightHull = rightHull[rightFirstPoint:] + [rightHull[0]]
        else:
            middlePartRightHull = rightHull[rightFirstPoint:rightLastPoint + 1]
        l2 = len(middlePartRightHull)
        newHull = list(range(l1 + l2 + l3))

        for i in range(0, l1):
            newHull[i] = firstPartLeftHull[i]
        for i in range(0, l2):
            newHull[i + l1] = middlePartRightHull[i]
        for i in range(0, l3):
            newHull[i + l1 + l2] = secondPartLeftHull[i]

        return Hull(newHull, rightPoints.rightMost + l1 - rightFirstPoint)


# define the class to hold the hull
class Hull():
    def __init__(self, points, rightMost):
        self.points = points
        self.rightMost = rightMost

# Helper Function to get slopes
def GetSlope(point1, point2):
    dy = point2.y() - point1.y()
    dx = point2.x() - point1.x()
    
    return dy/dx
 
