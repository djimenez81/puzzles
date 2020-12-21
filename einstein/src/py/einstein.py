#!/usr/bin/python
# module einstein

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
# - The Englishman lives in the red house.
# - The Swede keeps dogs.
# - The Dane drinks tea.
# - The green house is just to the left of the white one.
# - The owner of the green house drinks coffee.
# - The Pall Mall smoker keeps birds.
# - The owner of the yellow house smokes Dunhills.
# - The man in the center house drinks milk.
# - The Norwegian lives in the first house.
# - The Blend smoker has a neighbor who keeps cats.
# - The man who smokes Blue Masters drinks bier.
# - The man who keeps horses lives next to the Dunhill smoker.
# - The German smokes Prince.
# - The Norwegian lives next to the blue house.
# - The Blend smoker has a neighbor who drinks water.
#
# The question to be answered is: Who keeps fish?
#
# In general, the idea is that there are N individuals and M cathegories on
# which they differ, and given some hints that allows you to deduce to which
# individual each characteristic corresponds within each cathegory.
#
# The problem may be abstracted in the following way. There is an unknown MxN
# matrix where each row is a rearrangement of the  numbers 1,2,...,N, where at
# least one row (usually the first one) in order. You have to deduce the entire
# matrix based only on "hints" that tell you if two numbers in two specific rows
# are or are not in the same column. Any matrix obtained by permuting the
# columns should be acceptable. 
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
