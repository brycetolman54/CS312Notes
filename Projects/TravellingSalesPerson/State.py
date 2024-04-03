# Class to hold all information for a state in the search space and to perform its functions

class State:

    def __init__(self, matrix, depth, bound, rows, path, index):
        self.matrix = matrix
        self.size = len(self.matrix)
        self.depth = depth
        self.bound = bound
        self.value = float('inf')
        self.rows = rows
        self.path = path
        self.index = index

    def ReduceMatrix(self):

        # set up the return variable to be true
        ret = True

        # initialize the min variables
        theMins = []
        
        # loop each row to get the min
        for i in range(self.size):

            # skip if you have infinitized the row
            if i in self.rows:
                theMins.insert(len(theMins), 0)
                continue

            # else grab the min
            theMin = float('inf')
            for j in range(self.size):
                if self.matrix[i][j] < theMin:
                    theMin = self.matrix[i][j]
            theMins.insert(len(theMins), theMin)

        # make sure we don't have an invalid solution
        if float('inf') in theMins:
            return False

        # now subtract the min of each row from that row and add that number to the bound
        for i in range(self.size):

            # skip we have infinitized the row
            if i in self.rows:
                continue

            # else subtract the value
            loss = theMins[i]
            self.bound += loss
            for j in range(self.size):
                self.matrix[i][j] = self.matrix[i][j] - loss

    
        # set the mins back to empty for the cols
        theMins = []

        # loop each col to get the min
        for i in range(self.size):

            # skip if you have infinitized the row
            if i in self.path:
                theMins.insert(len(theMins), 0)
                continue

            # else grab the min
            theMin = float('inf')
            for j in range(self.size):
                if self.matrix[j][i] < theMin:
                    theMin = self.matrix[j][i]
            theMins.insert(len(theMins), theMin)

        # make sure we don't have an invalid solution
        if float('inf') in theMins:
            return False

        # now subtract the min of each row from that row and add that number to the bound
        for i in range(self.size):

            # skip we have infinitized the row
            if i in self.path:
                continue

            # else subtract the value
            loss = theMins[i]
            self.bound += loss
            for j in range(self.size):
                self.matrix[j][i] = self.matrix[j][i] - loss

        # update the value for the PQ
        self.value = self.bound / self.depth if self.depth != 0 else self.bound


        # return the ret value if nothing has gone wrong, if our matrix is reduceable
        return ret


    def Infinitize(self, row, col):

        # update the bound, path, and col/row arrays to tell what we don't need to check in the reduction
        self.bound += self.matrix[row][col]
        self.path.insert(len(self.path), col)
        self.rows.insert(len(self.rows), row)
        
        # loop the matrix and set the row and col to infinity
        for i in range(self.size):
            self.matrix[row][i] = float('inf')
            self.matrix[i][col] = float('inf')

        return

    def ToString(self):

        # initialize the return string
        str = ""

        # loop the matrix
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == float('inf'):
                    str += "\u001b[38;5;160m"
                elif self.matrix[i][j] == 0:
                    str+= "\u001b[38;5;12m"
                str += "\t{}\u001b[38;5;15m".format(self.matrix[i][j])
            str += "\n\n"

        str += "\nBound: {}\nDepth: {}\nValue: {}\nPath: {}\nRows: {}".format(self.bound, self.depth, self.value, self.path, self.rows)

        return str
            
