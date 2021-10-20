from typing import Union

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

def array_doubler(numbers : Union[list[int], list[float]]) -> Union[list[int], list[int]]:
    """Returns given array with all numbers multiplied by 2

    Args:
        numbers (Union[list[int], list[float]]): Array of numbers

    Returns:
        Union[list[int], list[int]]: Array of numbers muliplied by 2
    """
    return [(number * 2) for number in numbers]

def odd_in_array(numbers : Union[list[int], list[float]]):
    """Prints out odd numbers in given array

    Args:
        numbers (Union[list[int], list[float]]): Array of number
    """
    for number in numbers: 
        if number % 2 != 0:
            print(number)

def even_in_array(numbers : Union[list[int], list[float]]):
    """Prints out even numbers in given array

    Args:
        numbers (Union[list[int], list[float]]): Array of number
    """
    for number in numbers: 
        if number % 2 == 0:
            print(number)

def every_second_from_array(numbers : Union[list[int], list[float]]):
    """Prints out every second number in given array

    Args:
        numbers (Union[list[int], list[float]]): [
    """
    for i,n in enumerate(numbers):
        if i % 2 == 0:
            print(n)

def helloer(name: str, surname: str) -> str:
    """Returns Cześć string with name and surname

    Args:
        name (str): Name of the user 
        surname (str): Surname of the user

    Returns:
        str: String with "Cześć" and name + surname
    """
    return f"Cześć {name} {surname}!"

printer(["Kasia", "Basia", "Michał", "Piotr", "Kot", "Ziobro"])
print(array_doubler([1,2,3,4,5,6]))
print(doubler([1,2,3,4,5,6]))
print(odd_in_array([1,2,3,4,5,6,7,8,9,10]))
print(even_in_array([1,2,3,4,5,6,7,8,9,10]))
print(every_second_from_array([1,3,5,123,23,23,56,1]))
print(helloer("Łukasz", "Stachnik"))