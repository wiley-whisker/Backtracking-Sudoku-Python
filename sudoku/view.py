"""
view.py

This module contains the classes used for the view portion of the MVC pattern. The View class is where the GUI is
controlled from and started.

author: Wiley Matthews
author: http://newcoder.io/gui/part-3/ Specifically for much of the contents of the SudokuBoard class.
"""
from tkinter import *
from typing import List

from model import Model
from controller import Controller

# SudokoBoard frame specs.
WIDTH = 500
HEIGHT = 500
MARGIN = 10
SIDE = 52


class SudokuBoard(Frame):

    def __init__(self, parent: Tk, board: List[List[str]]) -> None:
        self.board = board
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

    def __initUI(self) -> None:
        """
        Initialize the UI.
        :return: None
        """
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        self.__draw_grid()
        self.__draw_puzzle()

    def __draw_grid(self) -> None:
        """
        Draws grid divided with blue lines into 3x3 squares
        :return: None
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self) -> None:
        """
        Draws the characters that consist the puzzle.
        :return: None
        """
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.board[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    original = self.board[i][j]
                    color = "black" if answer == original else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )

    def update_state(self) -> None:
        """
        Redraws the board after a model state update.
        :return: None
        """
        self.__draw_puzzle()


class View(object):

    def __init__(self, start_board: List[List[str]]) -> None:
        """
        Creates root window and saves starting puzzle.
        :param start_board: initial state of puzzle
        """
        self.root = Tk()
        self.board = start_board

    def start(self) -> None:
        """
        Starts the UI and necesary MVC components, then starts solving.
        :return: None
        """
        self.sb = SudokuBoard(self.root, self.board)
        self.sb.pack()
        model = Model(self.board)
        model.add_observer(self)
        controller = Controller(model, 0.05)
        controller.start_solving()
        self.root.mainloop()
        exit()

    def update_state(self) -> None:
        """
        Model uses this to inform view the puzzle state has been changed, and that the puzzle needs to be redrawn.
        :return: None
        """
        self.sb.update_state()
        self.sb.pack()


def main() -> None:
    """
    test program for thn this module is run directly.
    :return: None
    """
    b = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    view = View(b)
    view.start()


if __name__ == '__main__':
    main()
