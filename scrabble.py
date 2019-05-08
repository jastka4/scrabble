#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import itertools
import numpy
import random

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'S', 'H', 'A', 'R', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 'S', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'M', 'E', ' ', 'E', ' ', 'L', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'I', ' ', 'C', 'R', 'E', 'A', 'T', 'E', ' ', ' ', ' '],
         [' ', ' ', 'F', 'U', 'N', ' ', ' ', ' ', ' ', 'U', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'D', ' ', ' ', ' ', ' ', 'G', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

words = []
words.append(['T', 'E', 'A'])
words.append(['H', 'U', 'G'])
words.append(['B', 'U', 'G'])
words.append(['F', 'I', 'N', 'D'])
words.append(['T', 'H', 'A', 'N', 'K'])
words.append(['A', 'N'])

letters = ['E'] * 12 + ['A'] * 9 + ['I'] * 9 + ['O'] * 8 + ['N'] * 6 + ['R'] * 6 + ['T'] * 6 + ['L'] * 4 + ['S'] * 4 + ['U'] * 4 + ['D'] * 4 + ['G'] * 3 + ['B'] * 2 + ['C'] * 2 + ['M'] * 2 + ['P'] * 2 + ['F'] * 2 + ['H'] * 2 + ['V'] * 2 + ['W'] * 2 + ['Y'] * 2 + ['K'] + ['J'] + ['X'] + ['Q'] + ['Z']

def updateMyLetters(myLetters):
    for x in xrange(7 - len(myLetters)):
        myLetters.extend(letters.pop(letters.index(random.choice(letters))))
    return myLetters

myLetters = updateMyLetters([])

# while(len(letters) > 0):
print(numpy.matrix(board))

permutations = []
for x in itertools.permutations(myLetters):
    permutations.append(x)

# TODO - find permutations containg words
for permutation in permutations:
    for word in words:
        if all(elem in permutation for elem in word):
            print permutation

# scanning left-right looking for neighbours top-down
# for x in range(len(board)):
#     for y in range(len(board[x])):
#         if board[x][y].strip():
#             for neigbour in range(x, x + 7 + 1):
#                 if (neigbour < len(board)):
#                     print board[neigbour][y]

# scanning top-down looking for neighbours left-right
# for x in range(len(board)):
#     for y in range(len(board[x])):
#         if board[x][y].strip():
#             for neigbour in range(y, y + 7 + 1):
#                 if (neigbour < len(board)):
#                     print board[x][neigbour]
