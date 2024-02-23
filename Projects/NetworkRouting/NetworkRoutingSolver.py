#!/usr/bin/python3


from CS312Graph import *
import time


class NetworkRoutingSolver:
    def __init__( self):
        self.arrayNodes = None
        self.heapNodes = None
        self.hc = 0

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):

        self.dest = destIndex

        # get an appropriate tree to look at
        network = None
        if self.arrayNodes != None:
           network = self.arrayNodes
        elif self.heapNodes != None:
           network = self.pointers

        # set things up to track the edges
        pathEdges = []
        currentNode = network[destIndex]
        cost = currentNode.dist

        while True:

            # check to see if we are at the src node
            if currentNode.prev != None:

                # get the prev node
                nextNode = network[currentNode.prev]

                # get the cost to be here
                pathEdges.append( (currentNode.nodeLoc, nextNode.nodeLoc, '{:.0f}'.format(currentNode.dist - nextNode.dist)) )

                # update the current node
                currentNode = nextNode

            else:
                break

        return {'cost':cost, 'path':pathEdges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        nodesLength = len(self.network.nodes)
        t1 = time.time()
        if use_heap:
            self.djikstrasHeap(srcIndex, nodesLength)            
        else:
            self.djikstrasArray(srcIndex, nodesLength)
        t2 = time.time()
        return (t2-t1)

    def djikstrasArray(self, src, nodesLength):

        # create the new node list for the array
        self.arrayNodes = list(range(nodesLength))

        # add the nodes after giving them a dist and a prev
        for i in range(nodesLength):
      
            # add the new node to our node set
            self.arrayNodes[i] = self.GetNewNode(i, src)

        # go through the nodes and update their distances
        for i in range(nodesLength - 1):
            
            # get the min node and set it as visited
            minGuy = FindMin(self.arrayNodes)
            if minGuy != None:
                node = self.arrayNodes[minGuy]
                node.visited = True
            else:
                break
          
            # search his neighbors and update them as needed
            for edge in node.neighbors:
                if self.arrayNodes[edge.dest.node_id].dist > (node.dist + edge.length):
                    self.arrayNodes[edge.dest.node_id].dist = node.dist + edge.length
                    self.arrayNodes[edge.dest.node_id].prev = node.nodeId

    def djikstrasHeap(self, src, nodesLength):

        # initialize the arrays we need
        self.pointers = list(range(nodesLength))
        self.heapNodes = list(range(nodesLength))
        self.hc = 0

        # add the nodes to the two arrays
        for i in range(nodesLength):
            self.Insert(self.GetNewNode(i, src))
            self.hc += 1

        # update the edges
        for i in range(nodesLength - 1):

            # get the min from the top of the heap
            self.hc -= 1
            node = self.MoveMin()

            for edge in node.neighbors:

                # get the node first
                neighborPlace = self.pointers[edge.dest.node_id]
                if type(neighborPlace) != MyNode:
                    if self.heapNodes[neighborPlace].dist > (node.dist + edge.length):
                        self.heapNodes[neighborPlace].dist = node.dist + edge.length
                        self.heapNodes[neighborPlace].prev = node.nodeId
                        self.UpdateDist(self.heapNodes[neighborPlace])

        return

    
    def GetNewNode(self, i, src):

        # get the node from the network
        oldNode = self.network.nodes[i]

        # create the new node
        if i != src:
            newNode = MyNode(oldNode.node_id, oldNode.loc, oldNode.neighbors, float('inf'), None)
        else: 
            newNode = MyNode(oldNode.node_id, oldNode.loc, oldNode.neighbors, 0, None)

        return newNode
    
    def Insert(self, newNode):
        
        # put the node in and update its pointer
        self.heapNodes[self.hc] = newNode
        self.pointers[newNode.nodeId] = self.hc
        
        # bubble it up
        keepGoing = True
        while keepGoing:
            keepGoing = self.BubbleUp(newNode)

        return
    
    def MoveMin(self):

        # get the node to return
        ret = self.heapNodes[0]

        # switch around the nodes in the heap
        self.heapNodes[0] = self.heapNodes[self.hc]
        self.heapNodes[self.hc] = None

        # switch around the nodes in the pointer array
        self.pointers[self.heapNodes[0].nodeId] = 0
        self.pointers[ret.nodeId] = ret

        # get the node that we are sifting down
        movingNode = self.heapNodes[0]

        keepGoing = True
        while keepGoing:
            keepGoing = self.SiftDown(movingNode)

        return ret
    
    def UpdateDist(self, node):

        # bubble up with the node whose distance was just updated
        keepGoing = True
        while keepGoing:
            keepGoing = self.BubbleUp(node)

        return

    # function to bubble up
    def BubbleUp(self, node):

        # get the node's place in the heap and the other node
        nodePlace = self.pointers[node.nodeId]
        otherNode = self.heapNodes[nodePlace // 2]
        if otherNode == None:
            return False

        # check if our parent has a higher value, if so switch
        if otherNode.dist > node.dist:
            self.Swap(node, nodePlace // 2, otherNode, nodePlace)
            return True
        else: 
            return False

    # function to sift down
    def SiftDown(self, node):

        # get the location of the node and get its children
        nodePlace = self.pointers[node.nodeId]

        # get the children if you can 
        if nodePlace * 2 + 1 < len(self.pointers):
            rightChild = self.heapNodes[nodePlace * 2 + 1]
        else:
            rightChild = None
        if nodePlace * 2 < len(self.pointers):    
            leftChild = self.heapNodes[nodePlace * 2]
        else:
            leftChild = None

        if leftChild != None and rightChild == None:
            rightChild = leftChild
        elif leftChild == None and rightChild != None:
            leftChild = rightChild
        elif leftChild == None and rightChild == None:
            return False

        # see which child has a lower value
        if leftChild.dist < rightChild.dist:

            # see if it is less than that of the node we care about
            if leftChild.dist < node.dist:

                # swap it
                self.Swap(node, nodePlace * 2, leftChild, nodePlace)
                return True

            else:
                return False

        else:
            
            # see if this child has a smaller dist
            if rightChild.dist < node.dist:

                # swap it
                self.Swap(node, nodePlace * 2 + 1, rightChild, nodePlace)
                return True

            else:
                return False
        
    # function to swap two nodes in the heap
    def Swap(self, firstNode, firstSpot, secondNode, secondSpot):

        self.heapNodes[firstSpot] = firstNode
        self.pointers[firstNode.nodeId] = firstSpot
        
        self.heapNodes[secondSpot] = secondNode
        self.pointers[secondNode.nodeId] = secondSpot

        return

# function to find the minimum of the heap array
def FindMin(nodesList):
    
    # set the minimum distance and the node index tracker
    minIndex = None
    minDistance = float('inf')

    # go through the list and update the index and distance as needed
    for i in range(len(nodesList)):
        if nodesList[i].dist < minDistance and not nodesList[i].visited:
            minDistance = nodesList[i].dist
            minIndex = i

    return minIndex


# class to hold the info I need for my node
class MyNode():
    def __init__(self, nodeId, nodeLoc, neighbors, dist, prev):
        self.nodeId = nodeId
        self.nodeLoc = nodeLoc
        self.neighbors = neighbors
        self.dist = dist
        self.prev = prev
        self.visited = False
