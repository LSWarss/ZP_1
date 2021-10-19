
def printer(namesArray):
    for name in namesArray:
        print(name) 

printer(["Kasia", "Basia", "Michał", "Piotr", "Kot", "Ziobro"])

def doubler(numbers):
    returnArray = []
    for number in numbers:
        returnArray.append(number * 2)
    return returnArray

print(doubler([1,2,3,4,5,6]))

def arrayDoubler(numbers):
    return [(number * 2) for number in numbers]

print(arrayDoubler([1,2,3,4,5,6]))

def oddInArray(numbers): 
    for number in numbers: 
        if number % 2 != 0:
            print(number)

def evenInArray(numbers): 
    for number in numbers: 
        if number % 2 == 0:
            print(number)

print(oddInArray([1,2,3,4,5,6,7,8,9,10]))
print(evenInArray([1,2,3,4,5,6,7,8,9,10]))

def everySecondFromArray(numbers):
    for i,n in enumerate(numbers):
        if i % 2 == 0:
            print(n)

print(everySecondFromArray([1,3,5,123,23,23,56,1]))