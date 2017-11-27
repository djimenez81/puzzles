#!/usr/bin/python
# module sudoku

# This module implements, distributed in different classes, a solver for sudoku
# in a more general way.

# EXPLAIN MORE LATER

# Copyright (c) 2017 David Jimenez.
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

###########
# IMPORTS #
###########
from math import sqrt

####################
# GLOBAL VARIABLES #
####################

###################
###################
###################
###             ###
###             ###
###   METHODS   ###
###             ###
###             ###
###################
###################
###################


###############
###############
##           ##
##  PRIVATE  ##
##           ##
###############
###############
def _verifyPartition(partition, size):
    # This method verifies if the partition variable actually corresponds to a
    # partition.
    if len(partition) == size:
        if all([len(P) == size for P in partition]):
            return all([all([any([[x,y] in P for P in partition])
                    for x in range(size)]) for y in range(size)])
        else:
            return False
    else:
        return False


def _verifyClues(clues,size):
    # This method verifies if the variable clues correspond to a list of clues.
    if all([len(C) == 3 for C in clues]):
        return all([all([k < size for k in C]) for C in clues])
    else:
        return False



###################
###################
###################
###             ###
###             ###
###   CLASSES   ###
###             ###
###             ###
###################
###################
###################

# implement a class for partition
# implement class for "partition interval"
# implement a class for grid

##############################
##############################
##                          ##
##  CLASS SUDOKUPARTITIONS  ##
##                          ##
##############################
##############################
# class SudokuClass:
    # Description.

    ##############
    # ATTRIBUTES #
    ##############


    ############
    # CREATORS #
    ############


    ###########
    # GETTERS #
    ###########


    ###########
    # SETTERS #
    ###########

    ###########
    # METHODS #
    ###########

##############################
##############################
##                          ##
##  CLASS SUDOKUPARTITIONS  ##
##                          ##
##############################
##############################
class SudokuGrid:
    # A Sudoku grid is a structure that contains not only the matrix, but the
    # set of partitions, a 3D array with the posibilities that have not yet been
    # eliminated, etc.

    ##############
    # ATTRIBUTES #
    ##############
    _size       = 1  # Size of the grid.
    _partN      = 0  # Number of partitions
    _grid       = [] # Grid of values solved.
    _options    = [] # The options that are still possible.
    _partitions = [] # List of the partitions
    _filled     = [] # Grid of filled position
    _clues      = [] # List of original clues
    _symbols    = [] # List of symbols to write


    ############
    # CREATORS #
    ############
    def __init__(self,size):
        self._size = size
        self._grid = [[None for i in range(size)] for j in range(size)]
        self._options = [[[True]*size for i in range(size)]
                                        for j in range(size)]
        self._filled = [[False for i in range(size)] for j in range(size)]


    ###########
    # GETTERS #
    ###########
    def getSize(self):
        return self._size


    def getGrid(self):
        return self._grid


    def getOptions(self):
        return self._options

    def getPartitions(self):
        return self._partitions


    ###########
    # SETTERS #
    ###########
    def setClues(self,clues):
        # A clue is a list of three numbers: [n i j], that means, that in the
        # square with the coordinates [i,j], the clue given is n.
        N = len(clues)


    ###########
    # METHODS #
    ###########
    def addPartition(self,partition):
        # This method adds a partition to the grid, if that partition is indeed
        # a partition.
        sP = SudokuPartition(self._size)
        if sP.setPartition(partition):
            self._partitions.append(partition)
            self._partN = self._partN + 1


##############################
##############################
##                          ##
##  CLASS SUDOKUPARTITIONS  ##
##                          ##
##############################
##############################
class SudokuPartition:
    # A Sudoku partition of an NxN grid is a list with N list, each with N list
    # of two elements, representing all the indices of the grid. The first N
    # lists do not intersect.

    ##############
    # ATTRIBUTES #
    ##############
    _size  = 1
    _parts = []

    ############
    # CREATORS #
    ############
    def __init__(self,size):
        self._size  = size
        self._parts = [[[None, None] for x in range(size)] for y in range(size)]

    ###########
    # GETTERS #
    ###########
    def getSize(self):
        return self._size

    def getPartition(self):
        return self._parts

    def getPart(self,idx):
        return self._parts[idx]

    ###########
    # SETTERS #
    ###########
    def setPartition(self,partition):
        if _verifyPartition(partition,self._size):
            self._parts = partition
            return True
        else:
            return False

    def setPart(self,part,idx):
        if len(part) == self._size:
            self._parts[idx] = part
            return True
        else:
            return False

    ###########
    # METHODS #
    ###########
    def rowPartition(self):
        self._parts = [[[x, y] for y in range(self._size)]
                                for x in range(self._size)]

    def columnPartition(self):
        self._parts = [[[x, y] for x in range(self._size)]
                                for y in range(self._size)]

    def boxPartition(self):
        if sqrt(self._size).is_integer():
            N = int(sqrt(self._size))
            partitions = []
            for x in range(N):
                for y in range(N):
                    box = []
                    for i in range(N):
                        for j in range(N):
                            box.append([x*N+i,y*N+j])
                    partitions.append(box)
            self._parts = partitions
            return True
        else:
            self._parts = [[None]*self._size for _ in range(self._size)]
            return False


    def diagonalPartition(self):
        partitions = []
        for k in range(self._size):
            partitions.append([[(k+j)%self._size,j] for j in range(self._size)])
        self._parts = partitions


    def backDiagonalPartition(self):
        partitions = []
        for k in range(self._size):
            partitions.append([[(k-j)%self._size,j] for j in range(self._size)])
        self._parts = partitions



###############
# END OF FILE #
###############
