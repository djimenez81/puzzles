#!/usr/bin/python
# module skyscraper

# Copyright (c) 2021 David Jimenez.
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
# This module contains the code necessary to generate and solve puzzles of the
# kind normally called "Skyscraper". It is a grid based logic puzzle, where an
# empty n x n grid is provided, that should be completed as a Latin Square, but
# all that is provided are numbers, four arrays of n numbers, where each
# represents the number of skyscrapers visible from that vantage point. For
# example:
#
#        2   1   4   3   2
#       ___ ___ ___ ___ ___
#   2  |   |   |   |   |   | 3
#       ___ ___ ___ ___ ___
#   1  |   |   |   |   |   | 5
#       ___ ___ ___ ___ ___
#   4  |   |   |   |   |   | 1
#       ___ ___ ___ ___ ___
#   3  |   |   |   |   |   | 2
#       ___ ___ ___ ___ ___
#   2  |   |   |   |   |   | 2
#       ___ ___ ___ ___ ___
#        2   4   1   2   2
#
# Se resuelve de la siguiente manera:
#
#        2   1   4   3   2
#       ___ ___ ___ ___ ___
#   2  | 4 | 5 | 1 | 3 | 2 | 3
#       ___ ___ ___ ___ ___
#   1  | 5 | 4 | 3 | 2 | 1 | 5
#       ___ ___ ___ ___ ___
#   4  | 1 | 3 | 2 | 4 | 5 | 1
#       ___ ___ ___ ___ ___
#   3  | 2 | 1 | 4 | 5 | 3 | 2
#       ___ ___ ___ ___ ___
#   2  | 3 | 2 | 5 | 1 | 4 | 2
#       ___ ___ ___ ___ ___
#        2   4   1   2   2
#

###########
# IMPORTS #
###########
import copy

import numpy as np

from math import sqrt

####################
# GLOBAL VARIABLES #
####################

# Exampls of finished boards
# board1 = np.array([[4,5,1,3,2],[5,4,3,2,1],[1,3,2,4,5],[2,1,4,5,3],[3,2,5,1,4]],dtype=int)
# board2 = np.array([[1,2,4,3,5],[2,3,5,4,1],[4,1,3,5,2],[5,4,2,1,3],[3,5,1,2,4]],dtype=int)
# board3 = np.array([[6,7,1,4,3,5,2],[7,1,2,3,4,6,5],[4,6,3,2,5,7,1],[2,3,4,5,6,1,7],[1,2,5,6,7,4,3],[3,5,6,7,1,2,4],[5,4,7,1,2,3,6]],dtype=int)


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

def generateLURD(board):
    # This method takes a valid board (it assumes that it is a valid Latin
    # Square) and generates the set of clues that should result in such a board.
    # The clues we call LURD because they are Left, Up, Right, Down.
    #
    # INPUT:
    #  - board: An n x n NumPy array containint a Latin Square.
    #
    # OUTPUT:
    #  - lurd: A 4 x n NumPy array containint the clues to recreate the board.
    #
    n = board.shape[0]
    lurd = np.zeros((4,n),dtype = int)
    for j in range(n):
        cur_max_x = 0
        cur_max_y = 0
        count_x = 0
        count_y = 0
        for k in range(n):
            if board[j,k] > cur_max_x:
                cur_max_x = board[j,k]
                count_x += 1
            if board[k,j] > cur_max_y:
                cur_max_y = board[k,j]
                count_y += 1
        lurd[0,j] = count_x
        lurd[1,j] = count_y
    for j in range(n):
        cur_max_x = 0
        cur_max_y = 0
        count_x = 0
        count_y = 0
        for k in range(n):
            if board[j,n-1-k] > cur_max_x:
                cur_max_x = board[j,n-1-k]
                count_x += 1
            if board[n-1-k,j] > cur_max_y:
                cur_max_y = board[n-1-k,j]
                count_y += 1
        lurd[2,j] = count_x
        lurd[3,j] = count_y
    return lurd

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
##  CLASS SKYSCRAPERPUZZLE  ##
##                          ##
##############################
##############################
class SkyScraperPuzzle:
    # This class contains the clues, board and other attributes, as well as the
    # logic necessary to solve puzzles of the SkyScraper type, as well as the
    # logic to generate clues to solve one.
    #
    # NOTE:
    #  - Could consider both to solve and to generate puzzles with clues given
    #    for those cases when the clues (LURD) have more than one solution.
    #

    ##############
    # ATTRIBUTES #
    ##############
    _size    = 0
    _lurd    = []
    _board   = []
    _options = []


    ############
    # CREATORS #
    ############
    def __init__(self,lurd, board = np.zeros((1,2),dtype = int)):
        # This is the creator of the class. It takes one mandatory argument,
        # LURD (Left, Up, Right, Down) that contains the clues, and an optional
        # board, that should contain the actual board of the solution, maybe
        # blank, maybe full, or something in between.
        #
        # INPUT:
        #  - lurd: This is an Nx4 NumPy integer array, where N is the size of
        #          the puzzle, and such array contains, row by row, the clues
        #          corresponding to the left side, upper side, right side and
        #          lower side. The name comes from Left, Up, Right, and Down.
        #
        #  - board: This is an OPTIONAL input. It should contain an NxN NumPy
        #           array, with N the size of the puzzle. This array should
        #           contain either a valid solution for lurd, a zero matrix, or
        #           a partially filled board of a valid solution, with zeros in
        #           the unfilled position.
        #
        # NOTE:
        #  - Consider adding a verification step for the board.
        #
        N = lurd.shape[1]
        self._size = N
        self._lurd  = lurd
        self._options = np.ones((N,N,N), dtype = int)
        if board.shape[0] == board.shape[1] == N:
            self._board = board
            # There should be a better initialization of the of the option array
        else:
            self._board = np.zeros((N,N), dtype = int)


    ###########
    # GETTERS #
    ###########
    def getSize(self):
        # Returns the size of the puzzle.
        return self._size

    def getClues(self):
        # Return the array with the clues.
        return self._lurd

    def getBoard(self):
        # Returns the board in the current state.
        return self._board

    def getOptions(self):
        # Returns the 3D array with all the options given.
        return self._options


    ###########
    # SETTERS #
    ###########
    def setSize(self,size):
        # Sets the size given as the size of the puzzle.
        # Should consider if it is necessary to have a way to modify the size/
        self._size = size

    def setClues(self,lurd):
        # Sets the clues (lurd) to the array
        # Is it necessary to have a way to modify lurd?
        self._lurd = lurd

    def setBoard(self,board):
        # Sets the board.
        # Should consideer adding some verification steps
        self._board = board

    def setOptions(self,options):
        # Sets the option 3D array.
        # Should consideer adding some verification steps
        self._options = options


    ###########
    # METHODS #
    ###########
    def fullBoard(self):
        # This method returns true if and only if the board does not contain any
        # unfilled (zero) cell. 
        return np.where(self._board == 0)[0].size == 0



#######################
#######################
##                   ##
##  CLASS SOMECLASS  ##
##                   ##
#######################
#######################
# class SomeClass:
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
