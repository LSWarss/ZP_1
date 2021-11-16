from datetime import date, datetime
from employee import Employee
import unittest
import datetime


class EmployeeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee("Test", "TestSur", datetime.datetime.now(
        ), datetime.datetime.now(), "TestC", "TestS", "42-500", "666-666-666")
        self.maxDiff = None  # To see full output in tests when failed

    def test_str(self):
        hire_Str = datetime.datetime.now().strftime("%x")
        birth_Str = datetime.datetime.now().strftime("%x")
        self.assertEqual(self.employee.__str__(), f"""Employee: Test TestSur
 hired on: {hire_Str},
 born on: {birth_Str} living in city: TestC,
 on street TestS, 42-500, phone: 666-666-666""")
