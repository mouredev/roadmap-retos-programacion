"""
Problem #02 functions
"""


# Different functions
def simple_func():
    """
    Simplest function, without params neither return
    """
    print("Simple Function")
    # No return statement means return None by default


print(f"{simple_func()=}")


def args_func(num1, num2):
    """
    Function with params
    """
    print(f"My params => {num1=} {num2=}")
    return num1 + num2  # with explicit return


print(f"{args_func(1, 2)=}")


def kwargs_func(num1=2, num2=2):
    """
    Function with key word arg params
    """
    print(f"My params => {num1=} {num2=}")
    return num1 ** num2


print(f"{kwargs_func()=}")


def args_and_kwargs_func(num1, num2=2):
    """
    Function with param as arg and key word arg
    """
    print(f"My params => {num1=} {num2=}")
    return num1 // num2


print(f"{args_and_kwargs_func(1)=}")


def n_params_func(*args, **kwargs):
    """
    Function with N args and N key word args
    """
    print(f"My params:")
    print(f"\t{args = }")
    print(f"\t{kwargs = }")
    return args, kwargs  # Multiple values returned as tuple


print(f"{n_params_func([1, 2, 3, 4], key1='param1', key2='param2')=}")


# Function inception
def outer_func():
    def inner_func():
        print("Hello from inner_func")

        def ultra_inner_func():
            print("Hello from ultra_inner_func")
            # ... and so on

        ultra_inner_func()

    print("Hello from outer_func")
    inner_func()


print(outer_func())

# Built-in functions
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"my_list has {len(my_list)} elements")
print(f"rounded division {int(10/9) = }")  # Also for casting types
print("Hello World")  # print it's a builtin function

# LOCAL and GLOBAL variables
my_global_int = 10


def print_int():
    my_local_int = 20
    print(f"{my_local_int=}")  # can use local vars
    print(f"{my_global_int=}")  # can use global vars


print(f"{my_global_int=}")  # can use global vars
# can't use function local vars, out of scope

# EXTRA
def extra(arg1: str, arg2: str) -> int:
    printed = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(arg1 + arg2)
        elif num % 3 == 0:
            print(arg1)
        elif num % 5 == 0:
            print(arg2)
        else:
            print(num)
            printed += 1
    return printed


print(extra("multiple of 3", "multiple of 5"))