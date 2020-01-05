"""
model.py

A module containing the Model class and the print_board function.

author: Wiley Matthews
"""
import sys
from typing import List


def print_board(board: List[List[str]]) -> None:
    """
    Prints a soduku puzzle to standard output.
    :param board: nested lists representing the puzzle
    :return: None
    """
    for i in board:
        for j in i:
            if j == '.':
                print('_', end='')
            else:
                print(j, end="")
        print()


class Model(object):

    def __init__(self, start_board: List[List[str]]) -> None:
        """
        Model that represents the state and operation of a sudoku puzzle.
        :param start_board: nested lists representing the initial puzzle state
        """
        self.board = start_board
        self.observers = []

    def add_observer(self, obs) -> None:
        """
        Add a view as an observer of this model.
        :param obs: View to observe this model.
        :return: None
        """
        self.observers.append(obs)

    def make_move(self, new_char: str, i: int, j: int) -> None:
        """
        Change a character in the puzzle. (coordinates in i,j list notation, not x,y notation.)
        :param new_char: new value of specified index.
        :param i: i coordinate of change
        :param j: j coordinate of change
        :return: None
        """
        self.board[i][j] = new_char
        self.update_observers()

    def update_observers(self) -> None:
        """
        Update any/all observers of this model that a state change has occurred.
        :return: None
        """
        try:
            for observer in self.observers:
                observer.update_state()
        except Exception as e:
            sys.stderr.write("Suppressed exception in model.")
            print(e)
            sys.stderr.write("Exiting program.")
            exit()
