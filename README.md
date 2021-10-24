# Advanced Programming Python Repo

## Lab 3 Branch
---
### List of assignments: 

1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
wyświetlić ( print )
2. Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
mnożenia obu liczb.
3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
"Liczba nieparzysta"
4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
jako typ logiczny bool
5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int
. Funkcja ma sprawdzić, czy lista z parametru pierwszego zawiera taką wartość
jaką przekazano w parametrze drugim.
6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.
7. Dla chętnych Stworzyć skrypt pythonowy, który połączy się z API, które zawiera
informacje o browarach (dokumentacja
https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę Brawery , która będzie zawierała takie atrybuty jakich
dostarcza API wraz z odpowiednim typowaniem.
W klasie należy zaimplementować magiczną metodę __str__ która będzie
opisywała dane przechowywane w obiekcie.
Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
utworzyć listę 20 instancji klasy Brawery , którą przeiteruje i wyświetli każdy obiekt z
osobna.
8. Dla chętnych Rozszeczyć skrypt z punktu 7 o przyjmowanie parametru city , który
może być przekazywany w wierszu poleceń podczas wykonywania (np. python
main.py --city=Berlin ). Należy wykorzystać moduł argparse do wczytywania
przekazywanych parametrów, a w razie przekazania wartości ograniczyć pobierane
browary do miasta, które zostało wskazane.

Implemented all of them in assignment package, but strugle with unit testing in Python :') 