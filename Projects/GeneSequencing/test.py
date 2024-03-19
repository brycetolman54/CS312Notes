
import sys

# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

class GeneSequencing:

    def __init__( self ):
        pass

# This is the method called by the GUI.  _seq1_ and _seq2_ are two sequences to be aligned, _banded_ is a boolean that tells
# you whether you should compute a banded alignment or full alignment, and _align_length_ tells you
# how many base pairs to use in computing the alignment

    def align( self, seq1, seq2, banded, align_length):
        self.banded = banded
        self.MaxCharactersToAlign = align_length
        self.seq1 = seq1
        self.seq2 = seq2

        # get the edit distance based on which of the methods you choose
        if banded:
            
            # get the seq lengths
            self.length1 = min(len(self.seq1), self.MaxCharactersToAlign)
            self.length2 = min(len(self.seq2), self.MaxCharactersToAlign)

            # if the lengths are not reachable return not accessible
            if not self.length2 <= self.length1 + MAXINDELS or not self.length2 >= self.length1 - MAXINDELS:
                self.score = float('inf')
                self.alignment1 = "No Alignment Possible"
                self.alignment2 = "No Alignment Possible"
            else:
                self.banded_edit()
                self.get_banded_sequences()

        else:
            self.edit_dist()
            self.get_sequences()

        return {'align_cost':self.score, 'seqi_first100':self.alignment1, 'seqj_first100':self.alignment2}


    # function to get the edit distance matrix
    def edit_dist(self):

        # get the size of the matrix
        self.length1 = min(len(self.seq1), self.MaxCharactersToAlign)
        self.length2 = min(len(self.seq2), self.MaxCharactersToAlign)
        
        # initialize the matrix
        self.distMatrix = list(range(self.length1 + 1))
        for i in range(self.length1 + 1):
            self.distMatrix[i] = list(range(self.length2 + 1))

        # fill in the base cases
        for i in range(self.length1 + 1):
            action = "d" if i != 0 else "N"
            prev = {"i": i - 1, "j": 0} if i != 0 else None
            value = i * INDEL
            self.distMatrix[i][0] = Node(value, action, prev)
        for i in range(self.length2 + 1):
            action = "i" if i != 0 else "N"
            prev = {"i": 0, "j": i - 1} if i != 0 else None
            value = i * INDEL
            self.distMatrix[0][i] = Node(value, action, prev)
                
        # fill in the rest of the matrix
        for i in range(1, self.length1 + 1):
            for j in range(1, self.length2 + 1):

                # get all options and find the min
                delete = INDEL + self.distMatrix[i - 1][j].value
                insert = INDEL + self.distMatrix[i][j - 1].value
                matchSub = MATCH + self.distMatrix[i - 1][j - 1].value if self.seq1[i - 1] == self.seq2[j - 1] else SUB + self.distMatrix[i - 1][j - 1].value
                best = min(insert, delete, matchSub)

                # set the prev and action based on the best option
                action = None
                prev = None
                if best == delete:
                    action = "d"
                    prev = {"i": i - 1, "j": j}
                elif best == insert:
                    action = "i"
                    prev = {"i": i,"j": j - 1}
                elif best == matchSub:
                    action = "s"
                    prev = {"i": i - 1,"j": j - 1}

                # set the value of the new location
                self.distMatrix[i][j] = Node(best, action, prev)

        pMat = ""
        for i in range(self.length1 + 1):
            for j in range(self.length2 + 1):
                value = str(self.distMatrix[i][j].value)
                action = self.distMatrix[i][j].action if i != 0 or j != 0 else "N"
                pMat += "\t" + value + "," + action
            pMat += "\n\n"

        print(pMat)

    # function to get the banded edit distances
    def banded_edit(self):

        # get the banded lengths
        self.lengthA = min(self.length1, self.length2)
        self.lengthB = 2 * MAXINDELS + 1

        # set up the matrix
        self.distMatrix = list(range(self.lengthA + 1))
        for i in range(self.lengthA + 1):
            self.distMatrix[i] = list(range(self.lengthB))

        # set the base cases
        for i in range(MAXINDELS + 1):
            action = "i" if i != 0 else "N"
            prev = {"i": 0, "j": i + MAXINDELS - 1} if i != 0 else None
            value = i * INDEL
            self.distMatrix[0][i + MAXINDELS] = Node(value, action, prev)
        for i in range(MAXINDELS + 1):
            action = "d" if i != MAXINDELS else "N"
            prev = {"i": MAXINDELS - i - 1, "j": i + 1} if i != MAXINDELS else None
            value = (MAXINDELS - i) * INDEL
            self.distMatrix[MAXINDELS - i][i] = Node(value, action, prev)

        # fill in the matrix
        for i in range(1, self.lengthA + 1):
            for j in range(self.lengthB):

                if i <= MAXINDELS and j <= MAXINDELS - i:
                    continue

                # get all options and find the min
                delete = float('inf') if j == self.lengthB - 1 else INDEL + self.distMatrix[i - 1][j + 1].value
                insert = float('inf') if j == 0 else INDEL + self.distMatrix[i][j - 1].value
                matchSub = MATCH + self.distMatrix[i - 1][j].value if i + j - MAXINDELS - 1 >= 0 and i + j - MAXINDELS - 1 < self.length1 and i - 1 < self.length2 and self.seq1[i + j - MAXINDELS - 1] == self.seq2[i - 1] else SUB + self.distMatrix[i - 1][j].value
                best = min(insert, delete, matchSub)

                # set the prev and action based on the best option
                action = None
                prev = None
                if best == delete:
                    action = "d"
                    prev = {"i": i - 1, "j": j + 1}
                elif best == insert:
                    action = "i"
                    prev = {"i": i,"j": j - 1}
                elif best == matchSub:
                    action = "s"
                    prev = {"i": i - 1,"j": j}

                # set the value of the new location
                self.distMatrix[i][j] = Node(best, action, prev)

        pMat = ""
        for i in range(self.lengthA + 1):
            for j in range(self.lengthB):
                value = "0" if type(self.distMatrix[i][j]) != Node else str(self.distMatrix[i][j].value)
                action = "N" if type(self.distMatrix[i][j]) != Node else self.distMatrix[i][j].action
                pMat += "\t" + value + "," + action
            pMat += "\n\n"
        print(pMat)

    # function to get the alignments of the two sequences
    def get_sequences(self):

        # initialize the indices and the alignment sequences
        newSeq1 = ""
        newSeq2 = ""
        ind1 = self.length1
        ind2 = self.length2
        curNode = self.distMatrix[ind1][ind2]
        self.score = curNode.value

        while curNode.prev != None:

            # add to the alignment based on the action taken
            if curNode.action == "s": 
                newSeq1 = self.seq1[ind1 - 1] + newSeq1
                newSeq2 = self.seq2[ind2 - 1] + newSeq2
                ind1 -= 1
                ind2 -= 1
            elif curNode.action == "i":
                newSeq2 = self.seq2[ind2 - 1] + newSeq2
                newSeq1 = "-" + newSeq1
                ind2 -= 1
            elif curNode.action == "d":
                newSeq2 = "-" + newSeq2
                newSeq1 = self.seq1[ind1 - 1] + newSeq1
                ind1 -= 1

            # get the next node
            curNode = self.distMatrix[curNode.prev["i"]][curNode.prev["j"]]
        
        # set the alignments to be the first 100 of the sequences
        self.alignment1 = newSeq1[:100]
        self.alignment2 = newSeq2[:100]   

    def get_banded_sequences(self):

        # initialize the indices and the alignment sequence
        newSeq1 = ""
        newSeq2 = ""
        inda = self.lengthA
        indb = MAXINDELS + abs(self.length1 - self.length2)
        ind1 = self.length1 - 1
        ind2 = self.length2 - 1
        curNode = self.distMatrix[inda][indb]
        self.score = curNode.value

        while curNode.prev != None:

            # add to the alignments based on the action taken
            if curNode.action == "s":
                newSeq1 = self.seq1[ind1] + newSeq1
                newSeq2 = self.seq2[ind2] + newSeq2
                ind1 -= 1
                ind2 -= 1
            elif curNode.action == "i":
                newSeq2 = "-" + newSeq2
                newSeq1 = self.seq1[ind1] + newSeq1
                ind1 -= 1
            elif curNode.action == "d":
                newSeq2 = self.seq2[ind2] + newSeq2
                newSeq1 = "-" + newSeq1
                ind2 -= 1


            # get the next node in the path and update the indices
            inda = curNode.prev["i"]
            indb = curNode.prev["j"]
            curNode = self.distMatrix[inda][indb]
                        

        # set the alignments to be the first 100 of the sequence
        self.alignment1 = newSeq1[:100]
        self.alignment2 = newSeq2[:100]

# class to hold the node values for each box in the edit distance matrix
class Node:

    def __init__(self, value, action, prev):
        self.value = value
        self.action = action
        self.prev = prev




if __name__ == "__main__":
    # make sure we have enough arguments
    if len(sys.argv) != 5:
        print("Usage: python test.py <seq1> <seq2> <banded (t or f)> <align_length>")
        sys.exit(1)

    # if all is good, extract the n
    seq1 = sys.argv[1]
    seq2 = sys.argv[2]
    banded = True if sys.argv[3] == "t" else False
    align_length = int(sys.argv[4])

    # get the stuff
    data = GeneSequencing()
    values = data.align(seq1, seq2, banded, align_length)
    print(f"Cost: {values['align_cost']}\nAlignment 1: {values['seqi_first100']}\nAlignment 2: {values['seqj_first100']}")

