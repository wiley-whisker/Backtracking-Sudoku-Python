def print_board(board):
    for i in board:
        for j in i:
            if j == '.':
                print('_', end='')
            else:
                print(j, end="")
        print()


class Model(object):

    def __init__(self, start_board):
        self.board = start_board
        self.observers = []

    def add_observer(self, obs):
        self.observers.append(obs)

    def make_move(self, new_char, i, j):
        self.board[i][j] = new_char
        self.update_observers()

    def update_observers(self):
        # print("Update")
        #         # print_board(self.board)
        try:
            for observer in self.observers:
                observer.update_state(self.board)
        except:
            exit()
