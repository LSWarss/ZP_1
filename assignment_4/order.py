import datetime
from employee import Employee
from book import Book
from student import Student
from typing import List


class Order:
    def __init__(
        self,
        employee: str,
        student: Student,
        books: List[Book],
        order_date: datetime.date,
    ):
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        return f"""Order by: {self._employee}, for student:
            {self._student.__str__()}, with {self._books.count}
            books, order on: {self._order_date}"""
