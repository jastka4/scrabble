#!/usr/local/bin/python

import itertools
import numpy
import random


# TODO - put letters on the board

def update_my_letters(my_letters, all_letters):
    for x in xrange(7 - len(my_letters)):
        my_letters.extend(all_letters.pop(all_letters.index(random.choice(all_letters))))
    return my_letters


def is_sub_array(sub, lst):
    ln = len(sub)
    for i in range(len(lst) - ln + 1):
        if all(sub[j] == lst[i + j] for j in range(ln)):
            return i
    return -1


def get_available_words(permutations, all_words):
    words = []
    for permutation in permutations:
        for word in all_words:
            if is_sub_array(word, permutation) == 0:
                if word not in words:
                    words.append(word)
    return words


def get_empty_places(board_letters):
    empty_places = 0
    for x in range(len(board_letters)):
        if not board_letters[x].strip():
            empty_places += 1
    return empty_places


def fill_empty_places(my_letters, board_letters):
    possibilities = []
    empty_places = get_empty_places(board_letters)
    additional_letters = list(itertools.permutations(my_letters, empty_places))
    for row in range(len(additional_letters)):
        temp_board_letters = list(board_letters)
        col = 0
        for x in range(len(temp_board_letters)):
            if not temp_board_letters[x].strip():
                temp_board_letters[x] = additional_letters[row][col]
                col += 1
        possibilities.append(temp_board_letters)
    return possibilities


def put_word_on_board(board, available_words, direction):
    word = available_words[0]
    if direction is 'horizontal':
        return
    elif direction is 'vertical':
        return


def scan_horizontally(board, my_letters, words):
    # scanning left-right looking for neighbours top-down
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y].strip() and not board[x - 1][y].strip():
                chars = []
                for neighbour in range(x, x + 7 + 1):
                    if neighbour < len(board):
                        chars.append(board[neighbour][y])
                available_words = get_available_words(fill_empty_places(my_letters, chars), words)

                if available_words:
                    for word in available_words:
                        if not len(word) <= len(chars) - get_empty_places(chars):
                            print chars
                            print available_words
                            put_word_on_board(board, available_words, 'horizontal')


def scan_vertically(board, my_letters, words):
    # scanning top-down looking for neighbours left-right
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y].strip() and not board[x][y - 1].strip():
                chars = []
                for neighbour in range(y, y + 7 + 1):
                    if neighbour < len(board):
                        chars.append(board[x][neighbour])
                available_words = get_available_words(fill_empty_places(my_letters, chars), words)

                if available_words:
                    for word in available_words:
                        if not len(word) <= len(chars) - get_empty_places(chars):
                            print chars
                            print available_words
                            put_word_on_board(board, available_words, 'vertical')


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

    letters = ['E'] * 12 + ['A'] * 9 + ['I'] * 9 + ['O'] * 8 + ['N'] * 6 + ['R'] * 6 + ['T'] * 6 + ['L'] * 4 + ['S'] \
              * 4 + ['U'] * 4 + ['D'] * 4 + ['G'] * 3 + ['B'] * 2 + ['C'] * 2 + ['M'] * 2 + ['P'] * 2 + ['F'] \
              * 2 + ['H'] * 2 + ['V'] * 2 + ['W'] * 2 + ['Y'] * 2 + ['K'] + ['J'] + ['X'] + ['Q'] + ['Z']

    my_letters = update_my_letters([], letters)

    # while(len(letters) > 0):
    print(numpy.matrix(board))

    # for i in range(10):
    scan_horizontally(board, my_letters, words)
    scan_vertically(board, my_letters, words)


if __name__ == "__main__":
    main()
