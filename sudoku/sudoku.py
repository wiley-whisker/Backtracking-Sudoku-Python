"""
sudoku.py

A program that solves a Sudoku puzzle.

author: Wiley Matthews
"""
import argparse
import sys
import os
from typing import List

from model import Model, print_board
from view import View
from controller import Controller


def check_file(filename: str) -> None:
    """
    Checks that the specified file exists. If not, prints to error output then closes the program.
    :param filename: name of the file in question.
    :return: None
    """
    if not os.path.exists(filename):  # Check that data file exists
        sys.stderr.write("Error: " + filename + " does not exist!")
        exit()


def get_args() -> argparse.Namespace:
    """
    Defines and parses the program arguments.
    :return: a namespace containing the args.
    """
    parser = argparse.ArgumentParser(description="Solves a Sudoku puzzle using backtracking and displays the solution.")

    parser.add_argument('filename', help="board file")
    parser.add_argument('-d', '--display', action='store_true',
                        help='display the backtracking process')
    parser.add_argument('-s', '--save', action='store', help='save the resulting solution to the specified file')

    return parser.parse_args()


def read_board_file(filename: str) -> List[List[str]]:
    """
    Read a board file.
    :param filename: filename/directory of Sudoku board file.
    :return: nested lists representing the puzzle.
    """
    board = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            board.append(line[:-1].split(' '))  # line[:-1] to cut off newline char.
    return board


def write_board_file(board: List[List[str]], filename: str) -> None:
    """
    Takes a Sudoku puzzle as nested lists and writes them to the specified file.
    :param board: nested lists representing the puzzle.
    :param filename: filename/directory of Sudoku board file.
    :return: None
    """
    with open(filename, 'w') as f:
        for row in board:
            f.write(' '.join(row) + '\n')  # newline denotes row endings.


def main() -> None:
    """
    Parses program arguments solves the specified Sudoku puzzle, and prints the solution to standard output. Then saves
    and/or displays the solution as specified in the program arguments.
    :return: None
    """
    args = get_args()
    check_file(args.filename)
    board = read_board_file(args.filename)
    board_copy = [row[::1] for row in board]  # To save original board state if display is needed.
    model = Model(board)
    controller = Controller(model)
    controller.solveSudoku(model)
    print_board(controller.model.board)
    if args.save:
        write_board_file(model.board, args.save)
        print("Solution saved to", args.save)
    if args.display:
        view = View(board_copy)
        view.start()
        print("Display complete")


if __name__ == '__main__':
    main()
