from prettytable import PrettyTable
from typing import Dict, Tuple
import math
import copy


class AdvTicTacToeNode:
    """ Represents a node in the game of Tic-Tac-Toe"""

    def __init__(self, board: Dict[int, Dict[int, int]], player: int, prev_move: Tuple[int, int]):
        """
        A node of the tic-tac-toe game is composed of a board, a player, and the move that got us to this node.
        :param board: a dictionary {row : { col : player}}
        :param player: an integer, either 1 or 2.
        :param prev_move: the move that got us to this node.
        """
        # Check that the board is square.
        assert all([len(board) == len(board[i]) for i in range(len(board))])
        self.board = board
        self.size_board = len(self.board)
        # Check that all the entries of the board are either 0 or 1 or 2
        assert all([board[i][j] == 0 or board[i][j] == 1 or board[i][j] == 2 for i in range(0, self.size_board) for j in range(0, self.size_board)])
        # Check that the player is either 1 or 2.
        assert any([player == i for i in [1, 2]])
        self.player = player
        self.opponent = 1 if self.player == 2 else 2
        # Check the previous move is a tuple of two numbers in the valid range (inside the board).
        assert (prev_move is None) or (type(prev_move) is tuple and len(prev_move) == 2 and all([0 <= prev_move[i] <= self.size_board for i in [0, 1]]))
        self.prev_move = prev_move

    def check_winner(self, player: int):
        """
        Checks if the player wins in this node.
        :param player: the player to check for a win position.
        :return: True if the player wins in this node, false if it does not, or None if  the current board is at a draw.
        """
        # Compute a list with the player id.
        player_list = [player for _ in range(self.size_board)]

        # Check if the player wins by row
        if any([[self.board[i][j] for j in range(0, self.size_board)] == player_list for i in range(0, self.size_board)]):
            return True

        # Check if the player wins by col
        if any([[self.board[i][j] for i in range(0, self.size_board)] == player_list for j in range(0, self.size_board)]):
            return True

        # Check if the player wins by main diagonal or cross diagonal
        if ([self.board[i][i] for i in range(0, self.size_board)] == player_list) or \
                ([self.board[self.size_board - 1 - i][i] for i in range(0, self.size_board)] == player_list):
            return True

        return False

    def value(self):
        """
        Computes the value of a node.
        The value of a terminal node is 1 is the player wins, -1 if the player does not win, and 0 if the game is a tie,
        The value of a non-terminal node is None.
        :return: the value of a node.
        """
        if self.check_winner(self.player):
            return 1
        elif self.check_winner(self.opponent):
            return -1
        elif all([self.board[i][j] != 0 for i in range(0, self.size_board) for j in range(0, self.size_board)]):
            return 0
        return None

    def expand_node(self):
        """
        Expands the current node.
        :return: a list of nodes.
        """
        children = []
        for i in range(0, self.size_board):
            for j in range(0, self.size_board):
                if self.board[i][j] == 0:
                    new_board = copy.deepcopy(self.board)
                    new_board[i][j] = self.player
                    children += [AdvTicTacToeNode(new_board, self.opponent, (i, j))]
        return children

    def print_board(self):
        """
        A pretty table representation of this node, i.e., of the node's board.
        :return: a pretty table.
        """
        board_table = PrettyTable()
        board_table.field_names = [f"Col_{j}" for j in range(0, self.size_board)]
        for i in range(0, self.size_board):
            board_table.add_row([self.board[i][j] for j in range(0, self.size_board)])
        return board_table

    def __repr__(self):
        return f"\nboard: \n {self.print_board()} \n prev_move:  {self.prev_move} \n player: {self.player}"

    def negamax(self):
        """
        Implementation of negamax algorithm (https://en.wikipedia.org/wiki/Negamax)
        :return: the value and next node for the root node.
        """
        return AdvTicTacToeNode.negmax_helper(self, True)

    @staticmethod
    def negmax_helper(node, is_root):
        """
        A helper for recursive calls.
        :param node: the current node.
        :param is_root: a flag to keep track of whether the node is the root node.
        :return: a node and its value in case is_root is True, otherwise just the node's value.
        """
        value = node.value()
        if value is not None:
            return value

        max_value = -math.inf
        max_node = None
        for child in node.expand_node():
            value_child = -AdvTicTacToeNode.negmax_helper(child, False)
            if value_child >= max_value:
                max_value = value_child
                max_node = child

        return (max_value, max_node) if is_root else max_value
