import random
import itertools as it

"""
curl -d '{ "0" : { "0" : "P", "1" : "C", "2" : "P"}, "1" : { "0" : "", "1" : "", "2" : "P"}, "2" : { "0": "P", "1" : "P", "2" : "C"}}' -H "Content-Type: application/json" -X POST 0.0.0.0:8080/tic_tac_toe_engine

"""


class TicTacToeEngine:
    """ A tic-tac-toe player. """

    def __init__(self, board):
        """ The board is received as a json object. """
        self.board = {}
        for i, j in it.product(range(0, 3), range(0, 3)):
            self.board[i, j] = board[str(i)][str(j)]

    def get_board(self):
        """
        :return: the current board.
        """
        return self.board

    def play(self):
        """
        Pick a random open position on the board to play.
        If there are no more open positions, returns None.
        :return: a randomly chosen open position.
        """
        open_positions = []
        for i, j in it.product(range(0, 3), range(0, 3)):
            if self.board[i, j] == '':
                open_positions += [(i, j)]
        return random.choice(open_positions) if len(open_positions) > 0 else None
