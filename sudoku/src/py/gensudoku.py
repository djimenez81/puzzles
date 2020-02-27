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
#


################################
################################
##                            ##
##  IMPLEMENTATION DECISIONS  ##
##                            ##
################################
################################
#
# 1. The empty cell is a 0.
# 2. The numeration of rows and columns starts in 0. This also means that the
#    value has to be taken into consideration
#

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

#################
#################
##             ##
##  FUNCTIONS  ##
##             ##
#################
#################
def dumbBacktracking(G, display = False):
    # There are several states for backtracking:
    # 1. advance: It is time to look for a next clue.
    # 2. backtrack: It is time to backtrack a step.
    # 3. checkNow: It is time to ckeck if we can now add a new clue.
    # 4. justIncerted: A clue has just been inserted.

    N            = 0
    stack        = []
    solutions    = []
    flag         = True
    justIncerted = True
    checkNow     = False
    backtrack    = False
    advance      = False
    while flag:
        N += 1
        if justIncerted:
            justIncerted = False
            if G.isFilled():
                solutions.append(G.getGrid())
                backtrack = True
            elif G.isViable():
                advance = True
            else:
                backtrack = False
        elif checkNow:
            checkNow = False
            if len(opt) > 0:
                entry = opt.pop()
                tempFlag = G.fillEntry(entry,x,y)
                if tempFlag:
                    stack.append([(x,y),opt,G])
                    advance = True
                else:
                    checkNow = True
            else:
                backtrack = True
        elif backtrack:
            backtrack = False
            if len(stack) > 0:
                checkNow = True
                stackElement = stack.pop()
                opt = stackElement[1]
                G   = stackElement[2]
                x   = stackElement[0][0]
                y   = stackElement[0][1]
            else:
                flag = False
        elif advance:
            advance = False
            if G.isFilled():
                backtrack = True
                solutions.append(G.getGrid())
            else:
                checkNow = True
                P = np.where(G.getGrid() == 0)
                x = P[0][0]
                y = P[1][0]
                opt = list(np.where(G.getOptions()[:,x,y])[0] + 1)
        else:
            print("Opsie! This is for debugging. You should not see this")
            flag = False
    if display:
        print(N)
    return solutions

    """
    options    = G.getOptions() #
    grid       = G.getGrid() #
    N = 0 # Number of entries made to the gridself.
    stack = [] # Stack
    flag = True
    solutions = []
    if G.isFilled():
        solutions.append(grid)
        flag = False
    else:
        P = np.where(grid == 0)
        x = P[0][0]
        y = P[1][0]
        opt = list(np.where(options[:,x,y])[0] + 1)
        entry = opt.pop()
        stack.append([(x,y), opt, G])
        fillNow = True

    while flag:
        N += 1
        print(N)
        if G.isFilled():
            solutions.append(G.getGrid())
            if len(stack) == 0:
                flag = False
            else:
                stackElement = stack.pop()
                opt   = stackElement[1]
                while len(stack) > 0 and len(opt) == 0:
                    N += 1
                    stackElement = stack.pop()
                    opt = stackElement[1]
                if len(stack) == 0:
                    flag = False
                else:
                    entry = opt.pop()
                    G = stackElement[2]
                    x = stackElement[0][0]
                    y = stackElement[0][1]
                    fillNow = True
        elif fillNow:
            tempFlag = G.fillEntry(entry,x,y)
            if tempFlag:
                fillNow = False
            else:
                if len(opt) > 0:
                    entry = opt.pop()
                elif len(stack) > 0:
                    while len(stack) > 0 and len(opt) == 0:
                        N += 1
                        stackElement = stack.pop()
                        opt = stackElement[1]
                    if len(stack) == 0:
                        flag = False
                    else:
                        entry = opt.pop()
                        G = stackElement[2]
                        x = stackElement[0][0]
                        y = stackElement[0][1]
                        fillNow = True
                else:
                    flag = False
        else:
            options = G.getOptions()
            grid    = G.getGrid()
            P = np.where(grid == 0)
            x = P[0][0]
            y = P[1][0]
            opt = list(np.where(options[:,x,y])[0] + 1)
            entry = opt.pop()
            stack.append([(x,y), opt, G])
            fillNow = True
    if display:
        print(N)
    return solutions
   """


def findCellsWithUniqueOptions(G):
    # This function computes a matrix with the cells that have not been filled
    # yet, but have a single option available. Only those that already have a
    # single option when the function starts, are considered.
    #
    # INPUT:
    #  - G: A GeneralSudokuGrid object that has already been initialized.
    #
    # OUTPUT:
    #  - T: Matrix containing entries that can be filled and zeros in all other
    #       entries. It might be an all zeroes.
    #

    size    = G.getSize()
    options = G.getOptions()
    grid    = G.getGrid()

    M = np.logical_and(np.sum(options,axis = 0) == 1, grid == 0)
    M = np.where(M)
    K = len(M[0])
    T = np.zeros([size,size], dtype = np.uint8)

    for k in range(K):
        x = M[0][k]
        y = M[1][k]
        v = np.where(options[:,x,y])[0][0]
        T[x,y] = v + 1
    return T


def findCellsUniqueOptionOnPartition(G):
    # This function finds the cells that have not been filled and that, on one
    # of the parts, is the only one that has that option available.
    #
    # INPUT:
    #  - G: A GeneralSudokuGrid object that has already been initialized.
    #
    # OUTPUT:
    #  - T: Matrix containing entries that can be filled and zeros in all other
    #       entries. It might be an all zeroes.
    #

    size       = G.getSize()
    partitions = G.getPartitions()
    options    = G.getOptions()
    grid       = G.getGrid()
    partN      = G.getNumberOfPartitions()

    T = np.zeros([size,size], dtype = np.uint8)

    for k in range(partN):
        for n in range(size):
            P = np.where(partitions[k] == n + 1)
            Q = np.sum(options[:,P[0],P[1]], axis = 1)
            R = np.where(Q == 1)
            S = len(R[0])
            for s in range(S):
                t = R[0][s]
                u = np.where(options[:,P[0],P[1]][t])[0][0]
                x = P[0][u]
                y = P[1][u]
                T[x,y] = t + 1
    return T


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


##############################
##############################
##                          ##
##  CLASS SUDOKUPARTITIONS  ##
##                          ##
##############################
##############################
class GeneralSudokuGrid:
    # This class contains some basic structure and for the implementation of a
    # more general puzzle based on Sudoku. In this case, it is based on an NxN
    # grid, that is separated in k partitions of N parts each where each part
    # has N cells. This is, for example, one of the partitions can be consider,
    # in the regular sudoku, as the rows, another as the columns, and the last
    # as the boxes. But in this case, it is not necessary to have only three.
    # One is too few, but beyond that, anything is allowed.
    #
    # One of the thins we could consider is partitions with less than N parts.
    #
    # The functionality, that is, the logic of solution, is outside of this
    # class.
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
        return self._partitions

    def getGrid(self):
        return self._grid

    def getOptions(self):
        return self._options

    def getNumberOfPartitions(self):
        return self._partN

    def getSize(self):
        return self._size


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
        K = len(partitions)
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
            return flag
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
            flag = True
            P = np.where(B)
            N = len(P[0])
            for n in range(N):
                flag &= self.fillEntry(T[P[0][n],P[1][n]], P[0][n], P[1][n])
            return flag

    def deactivateOption(self,x,y,v):
        # This method is used when an option must be set to no longer be
        # considered viable.
        #
        # INPUT:
        #  - x: First coordinate of the value to be turned off.
        #  - y: Second coordinate of the value to be turned off.
        #  - v: Value to be turned off (1 to N, not 0 to N-1)
        #
        v -= 1
        self._options[v,x,t] = False



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


###############
# END OF FILE #
###############
