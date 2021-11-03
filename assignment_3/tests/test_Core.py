import unittest
from helper import TestCase
from Core import Core


class TestCore(unittest.TestCase):
    def test_print1(self):
        with self.assertStdout("test\n"):
            print("test")

    def test_printer(self):
        with self.assertStdout("Kasia\nBasia\nMichał\nPiotr\nKot\nZiobro\n"):
            Core.printer(["Kasia", "Basia", "Michał",
                         "Piotr", "Kot", "Ziobro"])
