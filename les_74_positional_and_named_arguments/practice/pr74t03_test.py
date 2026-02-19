import unittest
from les_74_positional_and_named_arguments.practice.pr74t03 import get_latin

class TestGetLatin(unittest.TestCase):

    def test_get_latin(self):
        self.assertEqual(get_latin('Лучший курс по Python!'), 'luchshiy-kurs-po-python!')
        self.assertEqual(get_latin('Лучший курс по Python!', '+'), 'luchshiy+kurs+po+python!')