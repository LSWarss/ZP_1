from library import Library
from datetime import date

class Book():
    def __init__(self, library: Library, publication_date: date, author_name: str, author_surname: str, number_of_pages: int):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages
    
    def __str__(self) -> str:
        return f"Book from {self._library.__str__()} publicated on: {self._publication_date}, author: {self._author_name} {self._author_surname}, number of pages: {self._number_of_pages}"

