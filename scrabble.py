#!/usr/local/bin/python

import itertools
import numpy
import random


def update_my_letters(my_letters, all_letters):
    for x in xrange(7 - len(my_letters)):
        my_letters.extend(all_letters.pop(all_letters.index(random.choice(all_letters))))
    return my_letters


def is_sub_array(sub, lst):
    ln = len(sub)
    for i in range(len(lst) - ln + 1):
        if all(sub[j] == lst[i + j] for j in range(ln)):
            return True
    return False


def get_permutations_of_my_letters(letters):
    permutations = []
    for x in itertools.permutations(letters):
        permutations.append(x)
    return permutations


def get_available_words(permutations, all_words):
    words = []
    for permutation in permutations:
        for word in all_words:
            if is_sub_array(word, permutation):
                words.append(permutation)
    return words


def fill_empty_places(my_letters, board_letters):
    return


def get_permutations_of_my_lettersAndBoard(my_letters, board_letters):
    return


def main():
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

    words = [['T', 'E', 'A'], ['H', 'U', 'G'], ['B', 'U', 'G'], ['F', 'I', 'N', 'D'], ['T', 'H', 'A', 'N', 'K'],
             ['A', 'N']]

    letters = ['E'] * 12 + ['A'] * 9 + ['I'] * 9 + ['O'] * 8 + ['N'] * 6 + ['R'] * 6 + ['T'] * 6 + ['L'] * 4 + [
        'S'] * 4 + ['U'] * 4 + ['D'] * 4 + ['G'] * 3 + ['B'] * 2 + ['C'] * 2 + ['M'] * 2 + ['P'] * 2 + ['F'] * 2 + [
                  'H'] * 2 + ['V'] * 2 + ['W'] * 2 + ['Y'] * 2 + ['K'] + ['J'] + ['X'] + ['Q'] + ['Z']

    my_letters = update_my_letters([], letters)

    # while(len(letters) > 0):
    print(numpy.matrix(board))

    permutations = get_permutations_of_my_letters(my_letters)

    available_words = get_available_words(permutations, words)

    # scanning left-right looking for neighbours top-down
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y].strip():
                chars = []
                for neighbour in range(x, x + 7 + 1):
                    if neighbour < len(board):
                        chars.append(board[neighbour][y])
                # print chars

    # scanning top-down looking for neighbours left-right
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y].strip():
                chars = []
                for neighbour in range(y, y + 7 + 1):
                    if neighbour < len(board):
                        chars.append(board[x][neighbour])
                # print chars
                fill_empty_places(my_letters, chars)


if __name__ == "__main__":
    main()
