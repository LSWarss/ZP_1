import datetime
from dataclasses import dataclass
from student import Student

@dataclass
class Book(): 
    def __init__(self, title: str, author: str, code: int):
        self._title = title
        self._author = author
        self._code = code

    def __str__(self) -> str:
        return f"Book {self._title}, by {self._author} with code: {self._code}"


class Order():

    def __init__(self, employee: str, student: Student, books: list[Book], order_date: datetime.date):
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date
    
    def __str__(self) -> str:
        return f"Order by: {self._employee}, for student: {self._student.__str__()}, with {self._books.count} books, order on: {self._order_date}"