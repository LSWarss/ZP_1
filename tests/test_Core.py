import unittest
from unittest.case import TestCase
from assignment.Core import *

class TestCore(TestCase):
    def test_printer(self):
        with self.assertStdout("Kasia\nBasia\nMichał\nPiotr\nKot\nZiobro\n"):
            Core.printer(["Kasia", "Basia", "Michał", "Piotr", "Kot", "Ziobro"])


if __name__ == '__main__':
    unittest.main()