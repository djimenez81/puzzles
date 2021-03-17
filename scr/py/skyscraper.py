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


#######################
#######################
##                   ##
##  CLASS SOMECLASS  ##
##                   ##
#######################
#######################
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
