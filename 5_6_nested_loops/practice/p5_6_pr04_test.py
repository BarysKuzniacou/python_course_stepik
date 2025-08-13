import unittest
from p5_6_pr04 import units_do_not_touch

class TestUnitsTouch(unittest.TestCase):

    def test_units_touch_01(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 1],
                                            [0, 0, 0, 0, 0],
                                            [0, 1, 0, 1, 0],
                                            [0, 0, 0, 0, 0]], 1), 'ДА')

    def test_units_touch_02(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 0, 0, 0, 0],
                                            [0, 1, 0, 0, 1],
                                            [0, 0, 0, 0, 0],
                                            [0, 1, 0, 0, 0],
                                            [0, 0, 0, 1, 0]], 2), 'НЕТ')

    def test_units_touch_03(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 1],
                                            [0, 0, 1, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [1, 0, 0, 0, 1]], 3), 'ДА')

    def test_units_touch_04(self):
        self.assertEqual(units_do_not_touch([
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 1],
                                            [0, 0, 1, 0, 0],
                                            [0, 1, 0, 1, 0],
                                            [0, 0, 0, 0, 0]], 4), 'НЕТ')

    def test_units_touch_05(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 1, 1, 0, 0],
                                            [0, 0, 0, 0, 1],
                                            [0, 0, 0, 0, 0],
                                            [0, 1, 0, 1, 0],
                                            [0, 0, 0, 0, 0]], 5), 'НЕТ')

    def test_units_touch_06(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 0, 0, 0, 0],
                                            [1, 0, 1, 0, 1],
                                            [1, 0, 0, 0, 0],
                                            [1, 1, 0, 1, 0],
                                            [1, 0, 0, 0, 0]], 6), 'НЕТ')

    def test_units_touch_07(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 0, 0, 1, 1],
                                            [0, 0, 0, 0, 1],
                                            [0, 0, 0, 0, 0],
                                            [0, 1, 0, 1, 0],
                                            [0, 0, 0, 0, 0]], 7), 'НЕТ')

    def test_units_touch_08(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 0, 0, 0, 1],
                                            [0, 0, 1, 0, 1],
                                            [0, 0, 0, 0, 1],
                                            [0, 1, 0, 0, 1],
                                            [0, 0, 0, 0, 1]], 8), 'НЕТ')

    def test_units_touch_09(self):
        self.assertEqual(units_do_not_touch([
                                            [1, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 1],
                                            [0, 0, 0, 0, 0],
                                            [0, 1, 0, 0, 0],
                                            [1, 1, 1, 1, 1]], 9), 'НЕТ')

    def test_units_touch_10(self):
        self.assertEqual(units_do_not_touch([
                                            [0, 0, 0, 0, 1],
                                            [0, 0, 0, 1, 0],
                                            [0, 0, 1, 0, 0],
                                            [0, 1, 0, 0, 0],
                                            [1, 0, 0, 0, 0]], 10), 'НЕТ')

    def test_units_touch_11(self):
        self.assertEqual(units_do_not_touch([
                                            [0, 0, 1, 0, 1],
                                            [0, 1, 0, 0, 0],
                                            [1, 0, 0, 0, 1],
                                            [0, 0, 0, 1, 0],
                                            [1, 0, 1, 0, 0]], 11), 'НЕТ')