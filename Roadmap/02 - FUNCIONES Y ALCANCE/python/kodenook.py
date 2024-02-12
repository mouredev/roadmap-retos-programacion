
def name() -> None:
    print('kodenook')

name()

def full_name(fname: str = 'my', lname: str = 'name') -> None:
    print(f'{fname} {lname}')

full_name(lname = 'lname')

def addition(*nums: int|float) -> int|float:
    result: int = 0

    for num in nums:
        result += num

    return result

print(addition(2, 3, 1, 10, 1.5))

def person(**persons: str|int) -> None:
    for attribute in persons:
        print(persons[attribute])

person(name = 'kodenook', age = 27, country = 'chile')

def first() -> None:
    print('first')

    def second() -> None:
        print('second')

    second()

first()

x = "awesome"

def global_variable():
  print("Python is " + x)

global_variable()

x = "awesome"

def local_variable():
  x = "fantastic"
  print("Python is " + x)

local_variable()

print("Python is " + x)

x = lambda a, b : a + b

print(x(1, 5))

""" Exercise """

def exercise(word1: str ,word2: str) -> int:
    count_numbers = 0

    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print(word1)
        elif x % 3 == 0:
            print(word1)
        elif x % 5 == 0:
            print(word2)
        else:
            count_numbers += 1

    return count_numbers


print(f'number of times it was a number and not words: {exercise('hello', 'python')}')