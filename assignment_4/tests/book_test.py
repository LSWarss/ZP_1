from datetime import datetime
from assignment_4.library import Library
from book import Book
import unittest
import datetime

class BookTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library("Test", "Test", "21 - 37", "666-666-666")
        self.book = Book(library=self.library, publication_date=datetime.datetime.now().strftime("%x"),
         author_name="TestName", author_surname="TestSurname", number_of_pages=10)
        self.maxDiff = None
    
    def test_str(self):
        publicationTest = datetime.datetime.now().strftime("%x")
        self.assertEqual(self.book.__str__(), f"""Book from {self.library.__str__()} publicated on: 
{publicationTest}, 
author: TestName TestSurname, 
number of pages: 10""")