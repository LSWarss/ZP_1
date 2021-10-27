from datetime import datetime
from employee import Employee
from property import Property
from library import Library
from book import Book
from student import Student
from order import Order
from house import House
from flat import Flat

library1 = Library("Katowice", "Katowicka 1", "7.00-16.00", "666-666-666")
library2 = Library("Katowice", "Katowicka 1", "7.00-16.00", "666-666-666")
library3 = Library("Katowice", "Katowicka 1", "7.00-16.00", "666-666-666")

book1 = Book(library1, datetime.now(), "Taco", "Hemingway", 1)
book2 = Book(library2, datetime.now(), "Taco", "Hemingway", 1)
book3 = Book(library3, datetime.now(), "Taco", "Hemingway", 1)
book4 = Book(library1, datetime.now(), "Taco", "Hemingway", 1)
book5 = Book(library2, datetime.now(), "Taco", "Hemingway", 1)

employee1 = Employee("Marcin", "Kaczka", datetime.now(), datetime.now(), "Katowice", "Katowicka 1", "40-000", "666-666-666")
employee2 = Employee("Marcin", "Kaczka", datetime.now(), datetime.now(), "Katowice", "Katowicka 1", "40-000", "666-666-666")
employee3 = Employee("Marcin", "Kaczka", datetime.now(), datetime.now(), "Katowice", "Katowicka 1", "40-000", "666-666-666")

student1 = Student("Michał", 50)
student2 = Student("Michał", 1)
student3 = Student("Michał", 20)

order1 = Order(employee1, student1, [book1, book2, book3, book4, book5], datetime.now())
order1 = Order(employee2, student2, [book3, book4, book5], datetime.now())

property = Property(42.0, 2, 420.000, "Katowica 1")
house = House(property, 200)
flat = Flat(property, 2)

