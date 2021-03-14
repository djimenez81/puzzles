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
