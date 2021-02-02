import math
import random


class EightQueen:
    def __init__(self):
        self.size = 8
        self.temp = 100
        # random numbers for destination of queen
        self.board = [random.randint(0, self.size - 1) for i in range(0, self.size)]
        print('initial State:')
        self.show_board(self.board)

    def show_board(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[j] != i:
                    print('0', end='  ')
                else:
                    print('1', end='  ')
            print()
        print('queens strike number: {}'.format(self.get_cost(board)))

    def random_simulate(self):
        board_copy = self.board.copy()
        i = random.randint(0, self.size - 1)
        while True:
            j = random.randint(0, self.size - 1)
            if board_copy[i] != j:
                board_copy[i] = j
                return board_copy

    def get_cost(self, board):
        strike = 0
        for queen in range(0, self.size):
            for next_queen in range(queen + 1, self.size):
                if self.board[queen] == self.board[next_queen] or abs(queen - next_queen) == abs(
                        board[queen] - board[next_queen]):
                    strike += 1

        return strike

    def simulated_annealing(self):
        while self.get_cost(self.board) != 0 and self.temp > 0.2:
            self.temp = self.temp - 1
            new_board = self.random_simulate()
            dE = self.get_cost(new_board) - self.get_cost(self.board)
            if dE <= 0 or random.uniform(0, 1) < math.e ** (dE / self.temp) < 1:
                print("dE " , dE)
                print("temp " , self.temp)
                print("ehtemal ", math.e ** (-dE / self.temp))
                # if you want to see step by step
                # self.show_board()
                self.board = new_board

        print('final State:')
        self.show_board(self.board)
