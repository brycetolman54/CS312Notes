#!/usr/bin/env python3

from QP import PQ
from Item import Item
from State import State
import signal
import sys
import random

if __name__ == '__main__':

    # allow CTRL+C to stop
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # get the args and see if we want the PQ or the State
    if not len(sys.argv) >= 2:
        print("usage: python test.py <[s]tate|[q]ueue> [state option: random as <t|f>]")
        sys.exit(1)

    # get the type of program we want
    tp = sys.argv[1]
    if len(sys.argv) > 2:
        r = True if sys.argv[2] == "t" else False

    # check to see if it is one of the options
    if not (tp == "state" or tp == "s" or tp == "queue" or tp == "q"):
        print("usage: python test.py <[s]tate|[q]ueue>")
        sys.exit(1)

    if tp == "q" or tp == "queue":

        # start the queue
        mine = PQ()

        # REPL
        reply = ""
        while not (reply == "q" or reply == "quit"):
            reply = input('   # ')
            if reply == "i" or reply == "input" or reply.split()[0] == "i":
                tokens = reply.split()
                if len(tokens) == 1:
                    item = input('      item[id, value]: ')
                    tokens = item.split()
                    mine.Insert(Item(tokens[0], int(tokens[1])))
                elif len(tokens) == 3:
                    mine.Insert(Item(tokens[1], int(tokens[2])))
            elif reply == "d" or reply == "delete":
                item = mine.Delete()
                print("      Item Removed: id({}), value({})".format(item.id, item.value))
            elif reply == "p" or reply == "print":
                print(mine.ToString())
            elif reply == "t" or reply == "tree":
                print(mine.ToTree())
            elif reply == "c" or reply == "clear":
                print("\u001b[H\u001b[2J")
            elif reply == "h" or reply == "help":
                print("Commands:\n\t[i]nput\t\tinput an item (as 'id value')\n\t[d]elete\tremove the top item in the heap\n\t[p]rint\t\tprint the priority queue\n\t[t]ree\t\tprint the tree version of the queue\n\t[c]lear\t\tclear the screen\n\t[h]elp\t\tget the list of commands\n\t[q]uit\t\tstop the REPL")

    elif tp == "s" or tp == "state":

        # create the matrix
        mat = []
        if r:
           
            # initialize the matrix
            mat = list(range(10))
            for i in range(10):
                mat[i] = list(range(10))

            # loop to create a matrix with random numbers
            for i in range(10):
                for j in range(10):
                   mat[i][j] = float('inf') if random.randint(1,10) > 9 else random.randint(1,100)
            
        else:

            mat = [
                [11, 12, 13, 14, 15, 16, 17, 18, 19],
                [21, 22, 23, 24, 25, 26, 27, 28, 29],
                [31, 32, 33, 34, 35, 36, 37, 38, 39],
                [41, 42, 43, 44, 45, 46, 47, 48, 49],
                [51, 52, 53, 54, 55, 56, 57, 58, 59],
                [61, 62, 63, 64, 65, 66, 67, 68, 69],
                [71, 72, 73, 74, 75, 76, 77, 78, 79],
                [81, 82, 83, 84, 85, 86, 87, 88, 89],
                [91, 92, 93, 94, 95, 96, 97, 98, 99]
            ]

        # make the state
        mine = State(mat, 1, 0, [], [], 1)

        # start the REPL
        reply = ""
        while not (reply == "q" or reply == "quit"):
            reply = input("    # ")
            if len(reply) == 0:
                continue
            if reply == "i" or reply == "infinitize" or reply.split()[0] == "i":
                tokens = reply.split()
                if len(tokens) == 1:
                    row = int(input("      Row: "))
                    col = int(input("      Col: "))
                elif len(tokens) == 3:
                    row = int(tokens[1])
                    col = int(tokens[2])
                else:
                    continue
                mine.Infinitize(row - 1, col - 1)
            elif reply == "r" or reply == "reduce":
                mine.ReduceMatrix()
            elif reply == "p" or reply == "print":
                print(mine.ToString())
            elif reply == "c" or reply == "clear":
                print("\u001b[H\u001b[2J")
            elif reply == "h" or reply == "help":
                print("Commands:\n\t[i]nfinitize\tset the col and rows to infinity (as 'row col')\n\t[r]educe\treduce the matrix\n\t[p]rint\t\tprint the state matrix\n\t[c]lear\t\tclear the screen\n\t[h]elp\t\tget the list of commands\n\t[q]uit\t\tstop the REPL")


    else:
        print("Usage: python test.py <[s]tate|[q]ueue>")
        sys.exit(1)

