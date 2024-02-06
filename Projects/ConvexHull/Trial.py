from PyQt6.QtCore import QLineF, QPointF, QObject
import random
import sys


# Functions to do the Sorting of the points
def MergeSort(points):

    # see if we are down to one value; if not, we can recursively call down and split the list in half
    length = len(points)        
    if length == 1:
        return points
    else:
        return Merge(MergeSort(points[:(length // 2)]), MergeSort(points[(length // 2):]))

def Merge(points1, points2):

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

# define the class to hold the hull
class Hull():
    def __init__(self, points, rightMost):
        self.points = points
        self.rightMost = rightMost

# Functions to do the Hull Splitting and Merge
def ConvexHull(points):
    
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
        return MergeHull(ConvexHull(points[:(length // 2)]), ConvexHull(points[(length // 2):]))

def MergeHull(leftPoints, rightPoints):
    
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

    while not goodLeft and not goodRight:

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

    while not goodLeft and not goodRight:

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
    secondPartLeftHull = leftHull[leftLastPoint:-1]
    l3 = len(secondPartLeftHull)
    middlePartRightHull = rightHull[rightFirstPoint:rightLastPoint + 1]
    l2 = len(middlePartRightHull)
    newHull = list(range(l1 + l2 + l3))

    for i in range(0, l1):
        newHull[i] = firstPartLeftHull[i]
    for i in range(0, l2):
        newHull[i + l1] = middlePartRightHull[i]
    for i in range(0, l3):
        newHull[i + l1 + l2] = secondPartLeftHull[i]

    return Hull(newHull, rightPoints.rightMost + l1 - 1)

# Helper Functions
def GetSlope(point1, point2):
    dy = point2.y() - point1.y()
    dx = point2.x() - point1.x()
    
    return dy/dx

def Print(pointList):
    for point in pointList:
        if(type(point) == int):
            print(f"int value: {point}")
        else:
            print(f"x: {int(point.x())}\t\ty: {int(point.y())}")


# run it
if __name__ == '__main__':
    if len(sys.argv) == 2: 
        ptlist = []
        unique_xvals = {}
        max_r = 0.98
        while len(ptlist) < int(sys.argv[1]):
            xval = random.uniform(-1.0,1.0)
            yval = random.uniform(-1.0,1.0)
            if xval**2 + yval**2 <= max_r**2:
                x = int(xval * 100)
                y = int(yval * 100)
                if not x in unique_xvals:
                    ptlist.append(QPointF(x,y))
                    unique_xvals[x] = 1

        points = MergeSort(ptlist)
        Print(points)
        print("\n")
        hull = ConvexHull(points)
        Print(hull.points)
    else:
        print("Usage: python Trial.py <# points>")