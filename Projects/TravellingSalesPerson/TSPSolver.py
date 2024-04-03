#!/usr/bin/python3

from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
    from PyQt5.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT4':
    from PyQt4.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT6':
    from PyQt6.QtCore import QLineF, QPointF
else:
    raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))


import time
import numpy as np
from TSPClasses import *
import heapq
import itertools
from State import *
from QP import *
import copy

class TSPSolver:
    def __init__( self, gui_view ):
        self._scenario = None

    def setupWithScenario( self, scenario ):
        self._scenario = scenario


    ''' <summary>
        This is the entry point for the default solver
        which just finds a valid random tour.  Note this could be used to find your
        initial BSSF.
        </summary>
        <returns>results dictionary for GUI that contains three ints: cost of solution,
        time spent to find solution, number of permutations tried during search, the
        solution found, and three null values for fields not used for this
        algorithm</returns>
    '''

    def defaultRandomTour( self, time_allowance=60.0 ):
        results = {}
        cities = self._scenario.getCities()
        ncities = len(cities)
        foundTour = False
        count = 0
        bssf = None
        start_time = time.time()
        while not foundTour and time.time()-start_time < time_allowance:
            # create a random permutation
            perm = np.random.permutation( ncities )
            route = []
            # Now build the route using the random permutation
            for i in range( ncities ):
                route.append( cities[ perm[i] ] )
            bssf = TSPSolution(route)
            count += 1
            if bssf.cost < np.inf:
                # Found a valid route
                foundTour = True
        end_time = time.time()
        results['cost'] = bssf.cost if foundTour else math.inf
        results['time'] = end_time - start_time
        results['count'] = count
        results['soln'] = bssf
        results['max'] = None
        results['total'] = None
        results['pruned'] = None
        return results


    ''' <summary>
        This is the entry point for the greedy solver, which you must implement for
        the group project (but it is probably a good idea to just do it for the branch-and
        bound project as a way to get your feet wet).  Note this could be used to find your
        initial BSSF.
        </summary>
        <returns>results dictionary for GUI that contains three ints: cost of best solution,
        time spent to find best solution, total number of solutions found, the best
        solution found, and three null values for fields not used for this
        algorithm</returns>
    '''

    def greedy( self, time_allowance=60.0 ):
        
        # initialize variables for keeping track
        numSolutions = 0
        bestSolution = {'cost': float('inf'), 'soln': None, 'time': 0}
        cities = self._scenario.getCities()


        # get the start time
        start = time.time()

        # loop through all the cities in the scenario and find the path from each
        for c1 in cities:
            
            # initialize the solution and the cost for it
            cSolution = []
            cCost = 0

            # set the initial city to search from
            outCity = c1

            # set a flag for if no solution is possible
            noSolution = False


            # do a loop to make sure you visit all the cities
            for i in range(len(cities)):

                # initialize values and loop all cities to find the closest one
                bestCity = None
                bestDistance = float('inf')
                for inCity in cities:

                    # make sure this city isn't already in the solution
                    if inCity in cSolution:
                        continue
                    
                    # find the cost of going there
                    cityCost = outCity.costTo(inCity)
                    
                    # update the best city if needed
                    if cityCost < bestDistance:
                        bestCity = inCity
                        bestDistance = cityCost

                # if we couldn't find a shortest distance city, stop this search
                if bestDistance == float('inf'):
                    noSolution = True
                    break

                # add the best city to the solution
                cSolution.insert(len(cSolution), bestCity)
                cCost += bestDistance
                outCity = bestCity


            # stop with this city if there is no solution
            if noSolution:
                continue

            # update the solution to match this one if it is the best
            numSolutions += 1
            if cCost < bestSolution['cost']:
                bestSolution['cost'] = cCost
                bestSolution['soln'] = cSolution

        end = time.time()


        bssf = TSPSolution(bestSolution['soln'])

        # set up and return the result
        results = {}
        results['cost'] = bssf.cost
        results['time'] = end - start
        results['count'] = numSolutions
        results['soln'] = bssf
        results['max'] = None
        results['total'] = None
        results['pruned'] = None
        return results





    ''' <summary>
        This is the entry point for the branch-and-bound algorithm that you will implement
        </summary>
        <returns>results dictionary for GUI that contains three ints: cost of best solution,
        time spent to find best solution, total number solutions found during search (does
        not include the initial BSSF), the best solution found, and three more ints:
        max queue size, total number of states created, and number of pruned states.</returns>
    '''

    def branchAndBound( self, time_allowance=60.0 ):

        # get the priority queue
        pq = PQ()

        # initialize some variables
        self.children = 0
        self.pruned = 0
        self.numSolutions = 0
        self.switched = False
        self.topDog = None

        # run greedy to get bssf
        self.res = self.greedy()
        self.best = self.res['cost']

        # create the initial state
        cities = self._scenario.getCities()
        size = len(cities)

        matrix = list(range(size))
        for i in range(size):
            matrix[i] = list(range(size))

        for i in range(size):
            for j in range(size):
                matrix[i][j] = cities[i].costTo(cities[j])

        firstState = State(matrix, 0, 1, [], [], 0)
        firstState.ReduceMatrix()
        
        pq.Insert(firstState)

        # start the while loop
        start = time.time()
        while not pq.IsEmpty() and not time.time() - start >= time_allowance:

            # grab the top of the queue
            top = pq.Delete()
            # print(top.ToString())

            # prune it if we need to
            if top.bound >= self.best:
                self.pruned += 1
                continue

            # determine if we are at the end of the line and adjust the indices accordingly
            firstIndex = 1
            lastIndex = size
            if top.depth == size - 1:

                # only look at the first index
                firstIndex = 0
                lastIndex = 1

            elif top.depth == size:

                # see if we have a new bssf
                if top.bound <= self.best:
                    self.numSolutions += 1
                    self.best  = top.bound
                    self.switched = True
                    self.topDog = top
                    continue

            # loop to make states as needed
            for i in range(firstIndex, lastIndex):

                # make sure we don't go down our own road
                if i == top.index:
                    continue

                # make a new state with this child
                self.children += 1
                newState = State(copy.deepcopy(top.matrix), copy.deepcopy(top.depth + 1), copy.deepcopy(top.bound), copy.deepcopy(top.rows), copy.deepcopy(top.path), i)

                # infinitize and reduce the matrix
                newState.Infinitize(top.index, newState.index)
                newState.ReduceMatrix()

                # check if the bound is less than the BSSF
                if newState.bound <= self.best:
                    pq.Insert(newState)
                else:
                    self.pruned += 1

        # see if we ran out of time
        if not pq.IsEmpty():
            self.pruned += len(pq.heap)

        # get the end time
        end = time.time()

        # get the solution if you switched from the old bssf, else return the greedy
        if self.switched:
            
            # build the path
            thePath = list(range(size))
            for i in range(size):
                thePath[i] = cities[self.topDog.path[i]]

            # get the actual solution
            bssf = TSPSolution(thePath)

            # set up and return the results
            results = {}
            results['cost'] = bssf.cost
            results['time'] = end - start
            results['count'] = self.numSolutions
            results['soln'] = bssf
            results['max'] = pq.max
            results['total'] = self.children
            results['pruned'] = self.pruned
            return results
            

        else:
            results = {}
            results['cost'] = self.res['cost']
            results['time'] = end - start
            results['count'] = self.numSolutions
            results['soln'] = self.res['soln']
            results['max'] = pq.max
            results['total'] = self.children
            results['pruned'] = self.pruned
            return results

        # start adding to queue and keep at it until time or the queue is empty
        # for each, make the next state, reduce it, see if bound is lower than bssf, add it or prune it and update that as you go
        # check depth amybe to see if you have a solution
        # once you have a solution, the one, loop the path of that solution state and make an array of the cities using the indices there to pass to TSPSolution Class
        # return everything you need to




    ''' <summary>
        This is the entry point for the algorithm you'll write for your group project.
        </summary>
        <returns>results dictionary for GUI that contains three ints: cost of best solution,
        time spent to find best solution, total number of solutions found during search, the
        best solution found.  You may use the other three field however you like.
        algorithm</returns>
    '''

    def fancy( self,time_allowance=60.0 ):
        pass
