import unittest
from math import pi
from unit_test_example.circle import circle_area

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(1), pi*1**2)
        self.assertEqual(circle_area(0), pi*0**2)
        self.assertEqual(circle_area(2.5), pi*2.5**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -1)
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5+2j)
        self.assertRaises(TypeError, circle_area, 'семь')
        self.assertRaises(TypeError, circle_area, [42, 7])
        self.assertRaises(TypeError, circle_area, [52])
        self.assertRaises(TypeError, circle_area, True)