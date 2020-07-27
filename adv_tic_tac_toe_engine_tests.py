import unittest
from adv_tic_tac_toe_engine import AdvTicTacToeNode


class MyTestCase(unittest.TestCase):
    def test_simple_1(self):
        ttt_game_0 = AdvTicTacToeNode({0: {0: 0, 1: 0, 2: 0},
                                       1: {0: 0, 1: 1, 2: 0},
                                       2: {0: 0, 1: 0, 2: 2}}, 2, None)
        print(ttt_game_0.print_board())
        next_value, next_node = ttt_game_0.negamax()
        print(f"{next_value} \n {next_node}")
        print(f"Player {next_node.player} moves to {next_node.prev_move}")
        self.assertEquals(next_node.prev_move, (2, 1))

    def test_simple_2(self):
        ttt_game_0 = AdvTicTacToeNode({0: {0: 2, 1: 0, 2: 0},
                                       1: {0: 0, 1: 0, 2: 0},
                                       2: {0: 2, 1: 1, 2: 1}}, 1, None)
        print(ttt_game_0.print_board())
        next_value, next_node = ttt_game_0.negamax()
        print(f"{next_value} \n {next_node}")
        print(f"Player {next_node.player} moves to {next_node.prev_move}")
        self.assertEquals(next_node.prev_move, (1, 2))

    def test_simple_3(self):
        ttt_game_0 = AdvTicTacToeNode({0: {0: 2, 1: 0, 2: 0},
                                       1: {0: 0, 1: 0, 2: 1},
                                       2: {0: 2, 1: 1, 2: 1}}, 2, None)
        print(ttt_game_0.print_board())
        next_value, next_node = ttt_game_0.negamax()
        print(f"{next_value} \n {next_node}")
        print(f"Player {next_node.player} moves to {next_node.prev_move}")
        self.assertEquals(next_node.prev_move, (1, 0))

    def test_simple_4(self):
        ttt_game_0 = AdvTicTacToeNode({0: {0: 2, 1: 0, 2: 0},
                                       1: {0: 1, 1: 0, 2: 0},
                                       2: {0: 2, 1: 1, 2: 1}}, 2, None)
        print(ttt_game_0.print_board())
        next_value, next_node = ttt_game_0.negamax()
        print(f"{next_value} \n {next_node}")
        print(f"Player {next_node.player} moves to {next_node.prev_move}")
        self.assertEquals(next_node.prev_move, (0, 2))

    def test_simple_5(self):
        ttt_game_0 = AdvTicTacToeNode({0: {0: 2, 1: 0, 2: 0},
                                       1: {0: 1, 1: 2, 2: 0},
                                       2: {0: 2, 1: 1, 2: 1}}, 1, None)
        print(ttt_game_0.print_board())
        next_value, next_node = ttt_game_0.negamax()
        print(f"{next_value} \n {next_node}")
        print(f"Player {next_node.player} moves to {next_node.prev_move}")
        self.assertEquals(next_node.prev_move, (0, 2))


if __name__ == '__main__':
    unittest.main()
