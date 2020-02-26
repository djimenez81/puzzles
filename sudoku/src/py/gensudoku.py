#!/usr/bin/python
# module gensudoku

# This file, if I manage to do so, contains a generalized class for Sudoku
# Puzzles. Generalized in the sense that it pretends to implement the methods
# for any size of a square grid, and for any combination of partitions. What is
# a partition? A partition is the division of the grid NxN into N sets, each
# with N cells, where the digits 1 to N are all exactly once on the set. In
# the regular Sudoku, there are three partitions: the rows, the colums, and the
# boxes. Here I want to implement the classes necessary to play the thing, but
# also, come with my own methods to solve (both backtracking and using strategy)
# as well with a way to generate valid full grids, to generate valid clues from
# a full grid, and to rate a grid.
#
# Copyright (c) 2020 David Jimenez.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   - Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   - Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#   - Neither the name of the <organization> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL DAVID JIMENEZ BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#################
#################
#################
###           ###
###   NOTES   ###
###           ###
#################
#################
#################

################################
################################
##                            ##
##  IMPLEMENTATION DECISIONS  ##
##                            ##
################################
################################
# 1. The empty cell is a 0.
# 2. The numeration of rows and columns starts in 0. This also means that the
#    value has to be taken into consideration


###################
###################
##               ##
##  LIMITATIONS  ##
##               ##
###################
###################
#
# 1. The maximum size that can be used is 255, as we are using numpy type uint8
#    for the values
#


###########
# IMPORTS #
###########
import numpy as np
import math
# from math import sqrt

####################
# GLOBAL VARIABLES #
####################

################################
################################
################################
###                          ###
###                          ###
###   METHODS AND FUNCTIONS  ###
###                          ###
###                          ###
################################
################################
################################

#################
#################
##             ##
##  FUNCTIONS  ##
##             ##
#################
#################
def latinSquarePartitions(N):
    # This function returns partitions corresponding to the regular Latin
    # Squares. This means, that the partitions are, first, the rows, and second,
    # the columns.
    #
    # INPUT:
    #   - N: unsigned integer up to 255 (uint8)
    #
    # OUTPUT:
    #   - partitions: NumPy arrays of uint8 elements, NxN, where on the first,
    #                 each row is a part of the partition, and on the second,
    #                 each column is a part of the partition.
    #
    A = np.zeros([N, N], dtype = np.uint8)
    B = np.zeros([N, N], dtype = np.uint8)
    for n in range(N):
        A[n,:] = n + 1
        B[:,n] = n + 1
    return (A,B)


def regularSudokuPartitions(N):
    # This function returns the partition corresponding to the regular sudoku.
    # This means, the partitions are, first, the rows, second, the columns, and
    # third, the boxes.
    #
    # INPUT:
    #   - N: unsigned square integer up to 225 (uint8)
    #
    # OUTPUT:
    #   - partitions: A list of three NumPy array of uint8 elements, NxN, with
    #                 the respective partitions.
    #
    # First check if the number given is a perfect square.
    K = math.sqrt(N)
    if not K.is_integer():
        print("\nERROR: Trying to make a sudoku grid with no square size\n")
        return False
    else:
        K = int(K)
    A = np.zeros([N, N], dtype = np.uint8)
    B = np.zeros([N, N], dtype = np.uint8)
    C = np.zeros([N, N], dtype = np.uint8)
    for n in range(N):
        p = n // K
        q = n % K
        A[n,:] = n + 1
        B[:,n] = n + 1
        C[K*p:(K*p+K),K*q:(K*q+K)] = n+1
    return (A,B,C)




###################
###################
###################
###             ###
###   CLASSES   ###
###             ###
###################
###################
###################


##############################
##############################
##                          ##
##  CLASS SUDOKUPARTITIONS  ##
##                          ##
##############################
##############################
class GeneralSudokuGrid:
    # This class contains some basic structure and functionality for the
    # implementation of a more general puzzle based on Sudoku. In this case, it
    # is based on an NxN grid, that is separated in k partitions of N parts each
    # where each part has N cells. This is, for example, one of the partitions
    # can be consider, in the regular sudoku, as the rows, another as the
    # columns, and the last as the boxes. But in this case, it is not necessary
    # to have only three. One is too few, but beyond that, anything is allowed.
    #
    # One of the thins we could consider is partitions with less than N parts.
    #

    ##############n
    # ATTRIBUTES #
    ##############
    _size       = 1  # Size of the grid.
    _partN      = 0  # Number of partitions
    _grid       = [] # Grid of values solved.
    _options    = [] # The options that are still possible.
    _partitions = [] # List of the partitions


    ############
    # CREATORS #
    ############
    def __init__(self,size):
        self._size    = size
        self._grid    = np.zeros([size, size], dtype = np.uint8)
        self._options = np.ones([size, size, size],  dtype = np.bool)


    ###########
    # GETTERS #
    ###########
    def getPartitions(self):
        # This function is a getter. I
        return self._partitions


    ###########
    # SETTERS #
    ###########
    def setPartitions(self,partitions):
        # This method sets an array of NxN matrices as the templates for the
        # partitions to be applied to the grid.
        #
        # INPUT:
        #  - partitions: List of NxN matrices.
        #

        # There should be some partition verifications system
        K = len(partitions)
        if K == 0:
            print("\nERROR: Trying to set empty partitions\n")
        else:
            self._partN = K
            self._partitions = np.asarray(partitions)


    def setGridFromArray(self,theArray):
        # This method takes an NxN NumPy array and makes it the grid for the
        # puzzle.
        #
        # INPUT:
        #  - theArray: NxN NumPy Array with a valid puzzle.
        #
        # OUTPUT:
        #  - SUCCESS: A boolean, True only if the setting was successful.
        #
        N = self._size
        if theArray.ndim != 2:
            return False
        elif theArray.shape[0] == theArray.shape[1] == N:
            flag = True
            for x in range(N):
                for y in range(N):
                    val = theArray[x,y]
                    if val > 0:
                        flag &= self.fillEntry(val,x,y)
        else:
            return False


    #############
    # FUNCTIONS #
    #############
    def fillEntry(self, val, x, y):
        # This function checks if the entry at the coordinates [x,y] have
        # already been filled, and if they have not, and the value val is a
        # valid option, then they filled, and marks the options respectively as
        # marked, and returns True. If they have, then it just returns False.
        #
        # INPUT:
        #  - val: The value that is going to be filled in.
        #  - x:   The x coordinate of the entry to be filled.
        #  - y:   The y coordinate of the entry to be filled.
        #
        # OUTPUT:
        #  - FILLED: Returns True if the given entry was filled, False otherwise.
        #
        v = val - 1
        if self._grid[x,y] == 0 and self._options[v,x,y]:
            self._grid[x,y] = val
            self._options[:,x,y] = False
            partMates = np.zeros([self._size,self._size], dtype = np.bool)
            K = self._partitions.shape[0]
            for k in range(K):
                partition = self._partitions[k,:,:]
                N = partition[x,y]
                partRegion = (partition == N)
                partMates = np.logical_or(partMates, partRegion)
            partMates = np.logical_and(partMates, (self._grid == 0))
            idxs = np.where(partMates)
            self._options[v,idxs[0],idxs[1]] = False
            return True
        else:
            return False

    def fillEntriesfromMatrix(self,T):
        # This function takes a matrix with nonzero entries with values that
        # must be filled on the grid in the position where they are located. It
        # makes a check that the entries have not been already fill.
        #
        # INPUT:
        #  - T: Matrix whose nonzero values on positions where they must be
        #       filled
        #
        # OUTPUT:
        #  - FILLED: Returns True if all entries were succesfully entered.
        #
        A = (self._grid != 0)
        B = (T != 0)
        C = np.logical_and(A,B)
        flag = np.ndarray.any(C)
        if flag:
            return False
        else:
            P = np.where(B)
            N = len(P[0])
            for n in range(N):
                self.fillEntry(T[P[0][n],P[1][n]], P[0][n], P[1][n])
            return True


    def isFilled(self):
        # This function returns True if and only if all the cells in the grid
        # have been filled.
        #
        # OUTPUT:
        #  - FILLED: A boolean that is true only if all the cells in the grid
        #            have been filled.
        #
        M = self._grid == 0
        P = np.where(M)
        return len(P[0]) == 0


    def isViable(self):
        # This function returns True if and only if all empty cells still have
        # at least an option open. That is, if for every x and y valid, not yet
        # filled, there is at least a value v such that _options[v,x,y] is set
        # to True.
        #
        # OUTPUT:
        #  - VIABLE: Boolean, true if and only if each unfilled cell has at
        #            least one option open.
        #
        M = np.logical_and(np.sum(self._options, axis = 0) == 0, self._grid == 0)
        M = np.where(M)
        return len(M[0]) == 0


    def findCellsWithUniqueOptions(self):
        # This function fills the cells that have not been filled yet, but have
        # a single option available. Only those that already have a single
        # option when the function starts, are considered. The function returns
        # true if it filled at least one entrance. A false indicates that
        # a further technique should be considered.
        #
        # OUTPUT:
        #  - FILLING: True if at least one entry was filled.
        #
        M = np.logical_and(np.sum(self._options, axis = 0) == 1,self._grid == 0)
        M = np.where(M)
        K = len(M[0])
        N = self._size
        T = np.zeros([N, N], dtype = np.uint8)
        if K > 0:
            for k in range(K):
                x = M[0][k]
                y = M[1][k]
                v = np.where(self._options[:,x,y])[0][0]
                T[x][y] = v + 1
        return T


    def findCellsUniqueOptionOnPartition(self):
        # This function fills the cells that have not been filled and that, on
        # one of the parts, is the only one that has that option available. The
        # function returns True if it is able to fill at least one cell.
        #
        # OUTPUT:
        #  - FILLING: True if at least one entry was filled.
        #
        N = self._size
        K = self._partN
        E = (self._grid == 0)                  # Empty cells
        T = np.zeros([N, N], dtype = np.uint8)
        for k in range(K):
            for n in range(N):
                P = np.where(self._partitions[k] == n + 1)
                Q = np.sum(self._options[:,P[0],P[1]], axis = 1)
                R = np.where(Q == 1)
                r = len(R[0])
                if r > 0:
                    for s in range(r):
                        t = R[0][s]
                        u = np.where(self._options[:,P[0],P[1]][t])[0][0]
                        x = P[0][u]
                        y = P[1][u]
                        if E[x,y]:
                            T[x,y] = t+1
                        else:
                            return False
                            print("Trying to fill a filled cell")
        return T



    def simpleBacktracking(self):
        # This function performs the most basic backtracking algorithm possible,
        # where the unfilled cells are filled in order (first by row, then by
        # column), and the options are checked in increasing order (1, 2, etc).
        #
        # OUTPUT:
        #  - N: Number of options checked.
        #
        N = 0
        stack = []
        initialGrid = self._grid
        while not self.isFilled():
            if self.isViable():
                # First find first the first open cell.
                P = np.where(self._grid == 0)
                x = P[0][0]
                y = P[1][0]
                opt = np.where(self._options[:, x, y])[0]
                opt = opt + 1
                # Then find the first option possible for that cell.
                n = opt[0]
                opt = np.delete(opt,0)
                # Add to stack a list with the option to try, the set of other
                #    options possible, and the current grid and option matrix.
                stack.append([n, opt, self])
                # Add the option to the cell.
                self.fillEntry(n,x,y)
                # Increas N by 1.
                N += 1
            else:
                flag = True
                while flag:
                    # Check stack is not empty. If it is, then return N and say
                    #    that it is not possible to fill the array.
                    if len(stack) == 0:
                        print("Grid proposed cannot be filed")
                        return N
                    # If the stack is not empty, take the last state saved on
                    #    there, take the next option available, pop it and use
                    #    it to fill in the grid.
                    stackElement = stack.pop()
                    opt = stackElement[1]
                    if len(opt) > 0:
                        sudokuGrid = stackElement[2]
                        self._grid = sudokuGrid._grid
                        self._options = sudokuGrid._options
                        n = opt[0]
                        opt = np.delete(opt,0)
                        stack.append([n, opt, self])
                        self.fillEntry(n,x,y)
                    # Increas N by 1
                    N += 1
                pass
        return N




    ###########
    # METHODS #
    ###########

###############
# END OF FILE #
###############
