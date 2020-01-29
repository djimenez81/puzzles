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
###           ###
###   NOTES   ###
###           ###
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
# 2. The numeration of rows and columns starts in 1, not in 0, so, this has to
#    be checked carefully when implementing functions and methods that access
#    the grid directly.


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

##############
##############
##          ##
##  PUBLIC  ##
##          ##
##############
##############

#############
# FUNCTIONS #
#############
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



###############
###############
##           ##
##  PRIVATE  ##
##           ##
###############
###############


###############
###############
##           ##
##  PRIVATE  ##
##           ##
###############
###############


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


##############################
##############################
##                          ##
##  CLASS SUDOKUPARTITIONS  ##
##                          ##
##############################
##############################
class GeneralSudokuGrid:
    # Description.

    ##############
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
        self._options = np.ones([size, size, size], dtype = np.bool)


    ###########
    # GETTERS #
    ###########
    def getPartitions(self):
        return self._partitions


    ###########
    # SETTERS #
    ###########
    def setPartitions(self,partitions):
        # There should some partition verifications system
        K = len(partitions)
        if K == 0:
            print("\nERROR: Trying to set empty partitions\n")
        else:
            self._partN = K
            self._partitions = np.asarray(partitions)


    #############
    # FUNCTIONS #
    #############
    def fillEntry(self,val,x,y):
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

        # First, remember to set the values that directly access the arrays to
        # one less, because the numbering of the entries starts in 1, not in 0.
        v = val - 1
        x -= 1
        y -= 1
        if self._grid[x,y] == 0:
            if self._options[v,x,y]:
                # 1. Fill the value in the given entry.
                self._grid[x,y] = val
                self._options[:,x,y] = False
                self._options[v,x,y] = True

                # Fill all the other cells that now cannot be filled with val.
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
        else:
            return False




    ###########
    # METHODS #
    ###########

class SomeClass:
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
    pass


###############
# END OF FILE #
###############
