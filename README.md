# Advanced Programming

## Lab 4 Branch
---
### List of assignments: 

1. Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
logiczną, pozytywną gdy ocena jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .
2. Stworzyć następujące klasy:

Zajęcia 4 3

Library (klasa opisująca bibliotekę), posiadająca pola:
city
street
zip_code
open_hours (str)
phone
Order (klasa opisująca zamówienie), posiadająca pola:
employee
student
books
order_date
Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
first_name
last_name
hire_date
birth_date
city
street
zip_code
phone
Book (klasa opisująca książkę), posiadająca pola
library
publication_date
author_name
author_surname
number_of_pages
Dodatkowo:
Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt oraz ewentualne obiekty
znajdujące się w tym obiekcie (np. obiekt Library w obiekcie Book).
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )
3. Stworzyć następujące klasy:
Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
area
rooms (int)
price
address

Zajęcia 4 4

House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
floor
Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
4. Zadania dla chętnych obowiązują z zajęć wcześniejszych.

### Running Tests
```bash
 python -m unittest discover -s tests -p '*_test.py'
```
