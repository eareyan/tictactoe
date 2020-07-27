import unittest
from adv_tic_tac_toe_engine import AdvTicTacToeNode


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ttt_game_0 = AdvTicTacToeNode({0: {0: 0, 1: 0, 2: 0},
                                       1: {0: 0, 1: 1, 2: 0},
                                       2: {0: 0, 1: 0, 2: 2}}, 2, None)
        print(ttt_game_0.print_board())
        next_value, next_node = ttt_game_0.negamax()
        print(f"{next_value} \n {next_node}")
        print(f"Player {next_node.player} moves to {next_node.prev_move}")
        self.assertEquals(next_node.prev_move, (2, 1))

if __name__ == '__main__':
    unittest.main()
