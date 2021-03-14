#!/usr/bin/python
# module einstein

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
#   - Neither the name of the developer nor the names of its contributors
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
# This module implements, distributed in different classes, a solver for puzzles
# in the style of the famous Einstein's puzzle, that is popularly attributed to
# Albert Einstein and it was common to be sent through email  chains during the
# 1990s and the 2000s. It reads as follows (at least this variant):
#
# Let us assume that there are five houses of different colors next to each
# other on the same road. In each house lives a man of a different nationality.
# Every man has his favorite drink, his favorite brand of cigarettes, and keeps
# pets of a particular kind.
#
# Let us consider the following example. There are five people, we know their
# names and have to guess their nationality, what they eat, the type of headwear
# they often use, and their favorite denomination of currency, based on the
# following clues>
#
#  1. The one who has a one dollar bil does NOT have a Santa Claus Hat.
#  2. Johanne has a dime.
#  3. Claude has a Santa Claus Hat.
#  4. Louis does NOT have a Five Dollar Bill.
#  5. The one who eats Pineapple does NOT have a Helmet.
#  6. The one who eats Tomato does NOT have a Detective Hat.
#  7. The one who has a Quarter does NOT eat Pineapple.
#  8. The one who eats Tomato does NOT have a One Dollar Bill.
#  9. The one who eats Pineapple does NOT have a Ten Dollar Bill.
# 10. The French has a Detective Hat.
# 11. The one who has a Wizzard Hat does NOT have a Five Dollar Bill.
# 12. The one who has a Wizard Hat does NOT have a Quarter.
# 13. The one who has a Santa Claus Hat does NOT have a Quarter.
# 14. Sarah has a One Dollar Bill.
# 15. The one who has a Santa Claus Hatt does not eat Pineapple.
# 16. The one who eats Mushrooms does NOT have a One Dollar Bill.
# 17. The Swede dpes MPT jave a Wizard Hat.
# 18. The one who has a Quarter does NOT have a Helmet.
# 19. Claude is Italian.
# 20. The one who has a One Dollar Bill does NOT eat Pineapple.
# 21. The Japanese has a One Dollar Bill.
# 22. The Swede eats Steak.
# 23. The one who has a Baseball Cap does NOT have a Quarter.
# 24. The one who has a Dime does NOT eat Pineapple.
# 25. The one who has a One Dollar Bill eats Pasta
# 26. Johanne is Swede.
# 27. The Swede does not have a One Dollar Bill.
# 28. The Japanese does NOT eat Pineapple.
#
# In general, the idea is that there are N individuals and M cathegories on
# which they differ, and given some hints that allows you to deduce to which
# individual each characteristic corresponds within each cathegory.
#
# The solution is the following>
# - Claude is Italian, eats Tomato, has a Ten Dollar Bill and wears a Santa Claus Hat.
# - Johanne is Swede, eats Steak, has a Dime and wears a Helmet.
# - Louis is French, eats Mushrooms, has a Quarter and wears a Detective Hat.
# - Pete is Korean, eats Pineapple, has a Five Dollar Bill and wears a Baseball Hat.
# - Sarah is Japanese, eats Pasta, has a One Dollar Bill and wears a Wizard Hat.
#
# The problem may be abstracted in the following way. There is an unknown MxN
# matrix where each row is a rearrangement of the  numbers 1,2,...,N, where at
# least one row (usually the first one) in order. You have to deduce the entire
# matrix based only on "hints" that tell you if two numbers in two specific rows
# are or are not in the same column. Any matrix obtained by permuting the
# columns should be acceptable.
#
# For example, if we do the following: Consider the cathegories in the order
# specified: 1. name, 2. nationality, 3. food, 4. currency, 5. hat; and the
# options as follows:
#
# Name: 1. Claude, 2. Johanne, 3. Louise, 4. Pete, 5. Sarah.
# Nationality: 1. French, 2. Italian, 3. Japanese, 4. Korean, 5. Swede.
# Food: 1. Mushrooms, 2. Pasta,  3. Pineaple, 4. Steak, 5. Tomato.
# Currency: 1. Dime, 2. Quarter, 3. $1, 4. $5, 5. $10.
# Hat: 1. Baseball Hat, 2. Detective Hat, 3. Helmet, 4. Santa Claus Hat, 5. Wizard Hat.
#
# In this case, the clues can be given in as
#
#  - [posneg [cathegory1 option1] [cathegory2 option2] ]
#
# For example the first few clues could be translated as:
#
#  1. [False [4 3] [5 4] ]
#  2. [True [1 2] [4 1] ]
#  3. [True [1 1] [5 4] ]
#  4. [False [1 3] [4 4] ]
# etc.
#
# The output response should be something like:
#
# [
#   [ 1 2 3 4 5 ]
#   [ 2 5 1 4 3 ]
#   [ 5 4 1 3 2 ]
#   [ 5 1 2 4 3 ]
#   [ 4 3 2 1 5 ]
# ]
#
# Any permutation of the columns should be also acceptable.
#


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


##################
##################
##              ##
##  CLASS CLUE  ##
##              ##
##################
##################
