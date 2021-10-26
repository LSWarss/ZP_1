import typing

class Student: 
    def __init__(self, name : str, marks: int):
        self._name = name
        self._marks = marks

    def is_passed(self): return self._marks > 50