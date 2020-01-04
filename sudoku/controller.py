from typing import List
import time
import threading

from model import Model


class Controller:

    def __init__(self, model, delay=0):
        # Solving elements
        self.stop = False
        self.delay = delay

        self.model = model

    def start_solving(self):
        self._worker = threading.Thread(target=self.worker_task)
        self._worker.start()

    def worker_task(self, delay=1):
        time.sleep(delay)
        self.solveSudoku(self.model)

    def solveSudoku(self, model: Model) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        model = self.model
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

