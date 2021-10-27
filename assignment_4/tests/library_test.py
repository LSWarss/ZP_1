from library import Library
import unittest

class LibraryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library("Test", "Test", "21 - 37", "666-666-666")
    
    def test_is_passed(self):
        self.assertEqual(self.library.__str__(), "Library in Test, on street: Test, with open hours: 21 - 37 and phone number: 666-666-666")