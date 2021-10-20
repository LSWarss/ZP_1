from typing import * 

def printer(namesArray : list[str]):
    """Prints names from the given array

    Args:
        namesArray (list[str]): List of strings preferable names
    """
    for name in namesArray:
        print(name) 

def doubler(numbers : Union[list[int], list[float]]) -> Union[list[int], list[int]]:
    """Returns given array with all numbers multiplied by 2

    Args:
        numbers (Union[list[int], list[float]]): Array of numbers

    Returns:
        Union[list[int], list[int]]: Array of numbers muliplied by 2
    """
    returnArray = []
    for number in numbers:
        returnArray.append(number * 2)
    return returnArray

def arrayDoubler(numbers : Union[list[int], list[float]]) -> Union[list[int], list[int]]:
    """Returns given array with all numbers multiplied by 2

    Args:
        numbers (Union[list[int], list[float]]): Array of numbers

    Returns:
        Union[list[int], list[int]]: Array of numbers muliplied by 2
    """
    return [(number * 2) for number in numbers]

def oddInArray(numbers : Union[list[int], list[float]]):
    """Prints out odd numbers in given array

    Args:
        numbers (Union[list[int], list[float]]): Array of number
    """
    for number in numbers: 
        if number % 2 != 0:
            print(number)

def evenInArray(numbers : Union[list[int], list[float]]):
    """Prints out even numbers in given array

    Args:
        numbers (Union[list[int], list[float]]): Array of number
    """
    for number in numbers: 
        if number % 2 == 0:
            print(number)

def everySecondFromArray(numbers : Union[list[int], list[float]]):
    """Prints out every second number in given array

    Args:
        numbers (Union[list[int], list[float]]): [
    """
    for i,n in enumerate(numbers):
        if i % 2 == 0:
            print(n)

printer(["Kasia", "Basia", "Michał", "Piotr", "Kot", "Ziobro"])
print(arrayDoubler([1,2,3,4,5,6]))
print(doubler([1,2,3,4,5,6]))
print(oddInArray([1,2,3,4,5,6,7,8,9,10]))
print(evenInArray([1,2,3,4,5,6,7,8,9,10]))
print(everySecondFromArray([1,3,5,123,23,23,56,1]))