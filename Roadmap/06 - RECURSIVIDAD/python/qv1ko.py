def func(number):
    print(number)

    number = number + 1

    if (number <= 100):
        func(number)

def fact(number):
    if (number <= 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return number * fact(number - 1)

def fib(pos):
    if (pos <= 1):
        return 0
    elif (pos == 2 or pos == 3):
        return 1
    else:
        return fib(pos - 1) + fib(pos - 2)

func(0)

print("---")

print(fact(4))

print("---")

print(fib(5))
