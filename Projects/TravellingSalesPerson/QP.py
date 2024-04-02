# the class to hold the priority queue and its functions 
# the items stored in the priority queue must have three fields:
#   id (a value to identify the item)
#   value (the value to compare in moving around the items in the heap)
#   spot (for the heap to manipulate in moving the nodes)

class PQ:
    
    def __init__(self):
        self.heap = []
        self.count = 0
        self.max = 0

    def Insert(self, item):
        
        # insert the item in the heap and update its spot
        item.spot = self.count
        self.heap.insert(self.count, item)


        # up the count and update the max if needed
        self.count += 1
        if self.count > self.max:
            self.max = self.count

        # bubble the item to where it should go in the heap
        keepGoing = True
        while keepGoing:
            keepGoing = self.BubbleUp(item)

        return

    def Delete(self):

        # get the item to return 
        ret = self.heap[0]

        # update the count
        self.count -= 1

        # move the item at the end of the heap to the top
        self.heap[0] = self.heap[self.count]
        self.heap[0].spot = 0
        del self.heap[self.count]

        # sift that new root down
        if not self.IsEmpty():
            newRoot = self.heap[0]
            keepGoing = True
            while keepGoing:
                keepGoing = self.SiftDown(newRoot)

        return ret
        
    def BubbleUp(self, item):

        # get the parent item
        parent = self.heap[abs((item.spot - 1)) // 2]

        # swap places if the parent has a higher value
        if parent.value > item.value:
            self.Swap(item, abs((item.spot - 1)) // 2, parent, item.spot)
            return True
        else:
            return False

        return

    def SiftDown(self, item):

        # get the children
        rightChild = None if item.spot * 2 + 2 > self.count - 1 else self.heap[item.spot * 2 + 2]
        leftChild = None if item.spot * 2 + 1 > self.count - 1 else self.heap[item.spot * 2 + 1]

        # see which child to replace, if any
        if rightChild != None and leftChild != None:
            
            # wap with the appropriate child
            if leftChild.value <= rightChild.value and leftChild.value < item.value:
                self.Swap(item, item.spot * 2 + 1, leftChild, item.spot)
                return True
            elif rightChild.value < item.value:
                self.Swap(item, item.spot * 2 + 2, rightChild, item.spot)
                return True
            else:
                return False
                
        elif rightChild != None:

            # see if we are less than the parent
            if rightChild.value < item.value:
                self.Swap(item, item.spot * 2 + 2, rightChild, item.spot)
                return True
            else:
                return False
            
        elif leftChild != None:
            
            # see if we are less than the parent
            if leftChild.value < item.value:
                self.Swap(item, item.spot * 2 + 1, leftChild, item.spot)
                return True
            else:
                return False

        else:
            return False

        return

    def Swap(self, item1, spot1, item2, spot2):

        self.heap[spot1] = item1
        item1.spot = spot1
        self.heap[spot2] = item2
        item2.spot = spot2

        return

    def ToString(self):

        # start the string
        str = ""

        # add the headers
        str += "\t\tID\t\tValue\t\tSpot\n"
        str += "\t===================================================="

        # loop each value in the queue from the top and add it
        for item in self.heap:
             str += "\n\t\t {}\t\t  {}\t\t  {}".format(item.id, item.value, item.spot)
            
        str += "\n\n\tCount: {}".format(self.count)

        return str

    def ToTree(self):

        # start the string and list of values for i
        str = ""
        newLine = [0, 2, 6, 14, 30, 62, 126]

        for i in range(self.count):
            str += "\t{}".format(self.heap[i].value)
            if i in newLine:
                str += "\n"

        return str

    def IsEmpty(self):

        if len(self.heap) == 0:
            return True
        else:
            return False
           
