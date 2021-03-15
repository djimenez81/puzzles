#!/usr/bin/python
# module binaris

# Copyright (c) 2018 David Jimenez.
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

#
# Binaris is a game where, for a given n, the player is given a 2n x 2n square
# board, empty except for a some clues. On each cell one has to place either a
# 0 or a 1, following the next three rules.
#
#   I. There cannot be three (or more) consecutive 0s or 1s, neither on a
#      column nor on a row.
#  II. Each column and each row has to have exactly n 0s and exactly n 1s.
# III. There cannot be two identical rows, or two identical columns.
#
# It is expected that each puzzled proposed has only possible solution.
#
# The puzzle looks interested, so, this code (more as a ludic pursuit) pretends
# to implement objects and algorithms with the next ends:
#
# 1. Finding out how many valid full boards are there.
# 2. Making a solving algorithm.
# 3. Finding out how to generate valid puzzles.
# 4. Finding out what is the minimum number of clues for a valid puzzle.
#



###########
# IMPORTS #
###########
# from math import sqrt

####################
# GLOBAL VARIABLES #
####################



#################################
#################################
#################################
###                           ###
###                           ###
###   METHODS AND FUNCTIONS   ###
###                           ###
###                           ###
#################################
#################################
#################################
def checkRow(bin_row):
    # This function checks if a given list of 0s and 1s are valid rows for a
    # valid binaris board.
    k = len(bin_row)
    if k % 2 == 0:
        reading_ones  = False
        error_flag    = False
        current_ones  = 0
        current_zeros = 0
        total_ones    = 0
        total_zeros   = 0
        counter       = 0
        while counter < k:
            this_val = bin_row[counter]
            # First update all the values
            if this_val == 0 and not reading_ones:
                total_zeros   += 1
                current_zeros += 1
            elif this_val == 0:
                reading_ones   = False
                current_ones   = 0
                current_zeros += 1
                total_zeros   += 1
            elif not reading_ones:
                reading_ones   = True
                current_zeros  = 0
                current_ones  += 1
                total_ones    += 1
            else:
                total_ones    += 1
                current_ones  += 1
            # Now check if there are three consecutive equal values.
            if (not reading_ones and current_zeros > 2) or \
               (reading_ones and current_ones > 2):
                error_flag = True
            counter += 1
        if error_flag:
            return False
        elif total_ones != total_zeros:
            return False
        else:
            return True
    else:
        return False


def listRows(n):
    # This function returns all the valid rows for a row of a 2n-binaris board
    # that starts with 0 (one that starts with 1 is the compliment of one that)
    # starts with 0.
    # This probably should not be run for values of n much larger than 16
    row_list = []
    for k in range(2**(2*n-3),2**(2*n-1)):
        row      = [(k // (2**i)) % 2 for i in range(2*n)]
        if checkRow(row):
            row.reverse()
            row_list.append(row)
    return row_list



# Some crap
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def binom(n,k):
    num = den = 1
    if k < 0 or k > n:
        return 0
    else:
        if 2*k < n:
            k = n-k
        for j in range(1,n-k+1):
            num *= k + j
            den *= j
            div = gcd(num,den)
            num //= div
            den //= div
        return num

def hanna(n):
    val = 0
    for k in range(n+1):
        val += (binom(k,n-k)+binom(k+1,n-k-1))**2
    return val//2

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
