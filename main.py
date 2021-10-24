from typing import Union, List
import argparse

from Brawery import getBraweries, getBraweriesForCity

def printer(namesArray : List[str]):
    """Prints names from the given array

    Args:
        namesArray (List[str]): List of strings preferable names
    """
    for name in namesArray:
        print(name) 

def doubler(numbers : Union[List[int], List[float]]) -> Union[List[int], List[float]]:
    """Returns given array with all numbers multiplied by 2

    Args:
        numbers (Union[List[int], List[float]]): Array of numbers

    Returns:
        Union[List[int], List[float]]: Array of numbers muliplied by 2
    """
    returnArray = []
    for number in numbers:
        returnArray.append(number * 2)
    return returnArray

def array_doubler(numbers : Union[List[int], List[float]]) -> Union[List[int], List[float]]:
    """Returns given array with all numbers multiplied by 2

    Args:
        numbers (Union[List[int], List[float]]): Array of numbers

    Returns:
        Union[List[int], List[float]]: Array of numbers muliplied by 2
    """
    return [(number * 2) for number in numbers]

def odd_in_array(numbers : Union[List[int], List[float]]):
    """Prints out odd numbers in given array

    Args:
        numbers (Union[List[int], List[float]]): Array of number
    """
    for number in numbers: 
        if number % 2 != 0:
            print(number)

def even_in_array(numbers : Union[List[int], List[float]]):
    """Prints out even numbers in given array

    Args:
        numbers (Union[List[int], List[float]]): Array of number
    """
    for number in numbers: 
        if number % 2 == 0:
            print(number)

def every_second_from_array(numbers : Union[List[int], List[float]]):
    """Prints out every second number in given array

    Args:
        numbers (Union[List[int], List[float]]): [
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

def multiplier(number1: int, number2: int) -> int:
    """Takes two numbers and multiplies them

    Args:
        number1 (int): Number 1
        number2 (int): Number 2

    Returns:
        int: Multiplication of number 1 and 2
    """
    return number1 * number2

def is_even(number: Union[List[int], List[float]]) -> bool:
    """Checks if the given number is even

    Args:
        number (Union[List[int], List[float]]): Number of type int or float

    Returns:
        bool: Bool if the given number is true or false
    """
    return number % 2 == 0

def check_if_bigger(number1: int, number2: int, number3 : int) -> bool:
    """Checks if sum of first two numbers is bigger then third number

    Args:
        number1 (int): First number
        number2 (int): Second number
        number3 (int): Third number

    Returns:
        bool: Bool if the sum of first two numbers is greater then third
    """
    return (number1 + number2) > number3

def check_if_contains(list : list, number : int) -> bool:
    """Checks if given list contains given number

    Args:
        list (list): Generic list 
        number (int): Some number

    Returns:
        bool: Bool if the list contains given number
    """
    return list.__contains__(number)

def merge_and_pow3(list1: list, list2: list) -> list:
    """Takes in two list and merges them together and raises all elements to power of 3

    Args:
        list1 (list): List 1
        list2 (list): List 2

    Returns:
        list: Array of not duplicates raised to power of 3
    """
    in_first = set(list1)
    in_second = set(list2)
    in_second_but_not_in_first = in_second - in_first
    result = list1 + list(in_second_but_not_in_first)
    return [(number**3) for number in result]

# I printed out the assignment goals while it would trigger with every exec

# printer(["Kasia", "Basia", "Michał", "Piotr", "Kot", "Ziobro"])
# print(array_doubler([1,2,3,4,5,6]))
# print(doubler([1,2,3,4,5,6]))
# print(odd_in_array([1,2,3,4,5,6,7,8,9,10]))
# print(even_in_array([1,2,3,4,5,6,7,8,9,10]))
# print(every_second_from_array([1,3,5,123,23,23,56,1]))
# print(helloer("Łukasz", "Stachnik"))

# for brawery in getBraweries():
#     print(brawery.__str__)

parser = argparse.ArgumentParser(description="This is main executable file for Advanced Programming Classes")
parser.add_argument("--city",
                    type=str,
                    help="City which you want to search for :)")
args = parser.parse_args()

city = args.city
print(getBraweriesForCity(city))
