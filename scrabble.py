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

def updateMyLetters(myLetters, allLetters):
    for x in xrange(7 - len(myLetters)):
        myLetters.extend(allLetters.pop(allLetters.index(random.choice(allLetters))))
    return myLetters
    
def isSubArray(sub, lst):
    ln = len(sub)
    for i in range(len(lst) - ln + 1):
        if all(sub[j] == lst[i+j] for j in range(ln)):
            return True
    return False

def getPermutationsOfMyLetters(letters):
    permutations = []
    for x in itertools.permutations(letters):
        permutations.append(x)
    return permutations

def getAvailableWords(permutations, allWords):
    words = []
    for permutation in permutations:
        for word in allWords:
            if isSubArray(word, permutation):
                words.append(permutation)
    return words

myLetters = updateMyLetters([], letters)

# while(len(letters) > 0):
print(numpy.matrix(board))

permutations = getPermutationsOfMyLetters(myLetters)

availableWords = getAvailableWords(permutations, words)

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
