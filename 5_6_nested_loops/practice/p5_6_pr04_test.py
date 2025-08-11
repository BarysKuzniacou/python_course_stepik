import unittest
from p5_6_pr04 import units_do_not_touch

class TestUnitsTouch(unittest.TestCase):

    def test_units_touch(self):
        self.assertEqual(units_do_not_touch([[1, 0, 0, 0, 0], # ДА
                                             [0, 0, 1, 0, 1],
                                             [0, 0, 0, 0, 0],
                                             [0, 1, 0, 1, 0],
                                             [0, 0, 0, 0, 0]]), 'ДА')

        self.assertEqual(units_do_not_touch([[1, 0, 0, 0, 0,],
                                             [0, 1, 0, 0, 1],
                                             [0, 0, 0, 0, 0],
                                             [0, 1, 0, 0, 0],
                                             [0, 0, 0, 1, 0]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[1, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 1],
                                             [0, 0, 1, 0, 0],
                                             [0, 0, 0, 0, 0],
                                             [1, 0, 0, 0, 1]]), 'ДА')

        self.assertEqual(units_do_not_touch([[0, 0, 0, 0, 0],
                                             [0, 0, 1, 0, 1],
                                             [0, 0, 1, 0, 0],
                                             [0, 1, 0, 1, 0],
                                             [0, 0, 0, 0, 0]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[1, 1, 1, 0, 0],
                                             [0, 0, 0, 0, 1],
                                             [0, 0, 0, 0, 0],
                                             [0, 1, 0, 1, 0],
                                             [0, 0, 0, 0, 0]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[1 0 0 0 0
1 0 1 0 1
1 0 0 0 0
1 1 0 1 0
1 0 0 0 0]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[1 0 0 1 1
0 0 0 0 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[1 0 0 0 1
0 0 1 0 1
0 0 0 0 1
0 1 0 0 1
0 0 0 0 1]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[1 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 1 0 0 0
1 1 1 1 1]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[0 0 0 0 1
0 0 0 1 0
0 0 1 0 0
0 1 0 0 0
1 0 0 0 0]]), 'НЕТ')

        self.assertEqual(units_do_not_touch([[0 0 1 0 1
0 1 0 0 0
1 0 0 0 1
0 0 0 1 0
1 0 1 0 0]]), 'НЕТ')