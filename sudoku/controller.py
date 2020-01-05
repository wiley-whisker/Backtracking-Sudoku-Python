"""
controller.py

Contains the Controller class for solving sudoku puzzles. This is where the solving takes place. If not used in an MVC
context, the Controller class can be thought of as a "SudokuSolver" class.

author: Wiley Matthews
"""
from typing import List
import time
import threading

from model import Model


class Controller:

    def __init__(self, model, delay=0):
        # Solving elements
        self.stop = False

        # Display elements
        self.delay = delay
        self.model = model

    def start_solving(self) -> None:
        """
        This method starts the worker thread that will spawn from the main-view thread and do the solving.
        :return: None
        """
        self._worker = threading.Thread(target=self.worker_task)
        self._worker.start()

    def worker_task(self, delay=1) -> None:
        """
        The task to be carried out by the worker thread. Waits for a specified delay (default 1 second) before starting
        to solve in order to give the UI time to finish initializing.
        :param delay: time delay between method call and solving start (in seconds).
        :return: None
        """
        time.sleep(delay)  # To give UI time to initialize.
        self.solveSudoku(self.model)

    def solveSudoku(self, model: Model) -> None:
        """
        Recursively use backtracking to solve a Sudoku puzzle in-place.
        :param model: model containing puzzle.
        :return: None
        """
        if not (self.is_solution(model.board) or self.stop):
            for i in range(len(model.board)):
                for j in range(len(model.board[i])):
                    if model.board[i][j] == '.':
                        for k in range(1, 10):
                            model.make_move(str(k), i, j)
                            time.sleep(self.delay)
                            if self.is_valid(model.board):
                                self.solveSudoku(model)
                                if self.stop:
                                    break
                            model.make_move('.', i, j)
                            time.sleep(self.delay)
                        return
                    if self.stop:
                        break
                if self.stop:
                    break
        else:
            self.stop = True

    def is_valid(self, board: List[List[str]]) -> bool:
        """
        Determines if the state of the supplied sudoku puzzle is valid.
        :param board: nested lists representing the puzzle state
        :return: True if valid state, false if invalid.
        """
        for i in range(len(board)):
            row = []
            col = []
            for j in range(len(board)):
                if board[i][j] not in col and board[j][i] not in row:
                    if board[j][i] != '.':
                        row.append(board[j][i])
                    if board[i][j] != '.':
                        col.append(board[i][j])
                else:
                    return False
        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    for l in range(3):
                        if board[k + i*3][l + j*3] not in square:
                            if board[k + i*3][l + j*3] != '.':
                                square.append(board[k + i*3][l + j*3])
                        else:
                            return False
        return True

    def is_solution(self, board: List[List[str]]) -> bool:
        """
        Determines if the state of the supplied sudoku puzzle is a solution.
        :param board: nested lists representing the puzzle state
        :return: True if solution, false if not a solution.
        """
        for i in range(len(board)):
            row = []
            col = []
            for j in range(len(board)):
                if board[i][j] == "." or board[j][i] == ".":
                    return False
                if board[i][j] not in col and board[j][i] not in row:
                    row.append(board[j][i])
                    col.append(board[i][j])
                else:
                    return False
        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    for l in range(3):
                        if board[k + i*3][l + j*3] == ".":
                            return False
                        if board[k + i*3][l + j*3] not in square:
                            square.append(board[k + i*3][l + j*3])
                        else:
                            return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()

