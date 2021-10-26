from student import Student
import unittest

class StudentTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.studentHigh = Student("Tester", 51)
        self.studentLow = Student("Tester", 49)
    
    def test_is_passed(self):
        self.assertTrue(self.studentHigh.is_passed, "This student should pass")
        self.assertFalse(self.studentLow.is_passed)