"""
    Types of functions...
"""
# Anonymous function
anonymous = lambda: print(
    "Anonymous function: <FUNCTION NAME> = lambda(<PARAMETERS...>): <INSTRUCTIONS...>"
)


# Common function
def common():
    print("Common function: def <FUNCTION NAME>(<PARAMETERS...>): <INSTRUCTIONS...>")


# With parameter
def with_parameters(name):
    print(
        f"Common function (with parameter): def <FUNCTION NAME>(name): <INSTRUCTIONS...> --> Hello {name}!"
    )


# Without parameter
def without_parameters():
    print(
        "Common function (without parameter): def <FUNCTION NAME>(): <INSTRUCTIONS...> --> Hello!"
    )


# With default parameter
def with_default_parameters(last_name="Hoz"):
    print(
        f"Common function (with default parameter): def <FUNCTION NAME>(last_name = 'Hoz'): <INSTRUCTIONS...> --> By {last_name}!"
    )


# With keyword parameter
def with_keyword_parameter(last_name, first_name):
    print(
        f"Common function (with keyword parameter): def <FUNCTION NAME>(last_name, first_name): <INSTRUCTIONS...> --> {first_name} {last_name}!"
    )


# With arbitrary keyword parameter
def with_arbitrary_keyword_parameter_v1(*argv):
    print(
        f"Common function (with arbitrary keyword parameter v1): def <FUNCTION NAME>(*argv): <INSTRUCTIONS...> --> {argv}!"
    )


def with_arbitrary_keyword_parameter_v2(**kwargv):
    print(
        f"Common function (with arbitrary keyword parameter v2): def <FUNCTION NAME>(**kwargv): <INSTRUCTIONS...> --> {kwargv}!"
    )


# With return
def with_return():
    return "Python 3.12.0"


# Without return
def without_return():
    print(
        "Common function (without return): def <FUNCTION NAME>(): <INTRUCTIONS (return not included)...> --> return void"
    )


anonymous()
common()
with_parameters("Lucas")
without_parameters()
with_default_parameters()
with_keyword_parameter(first_name="Lucas", last_name="Hoz")
with_arbitrary_keyword_parameter_v1("Martin", "Jose", "Tomás")
with_arbitrary_keyword_parameter_v2(name="Juan", last_name="Gonzales", city="New York")
print(
    f"Common function (with return): def <FUNCTION NAME>(): <INTRUCTIONS (with return definition included)...> --> return '{with_return()}'"
)
without_return()


"""
    Function definition inside another function...
"""


def wrapper():
    def inner():
        print("Inner function called")

    print("\nWrapper function called")
    inner()


wrapper()


"""
    Native functions...
"""

ARRAY = ["HTML", "CSS", "JavaScript", "Python"]
print(f"Native functions: len({ARRAY}) --> {len(ARRAY)}")

HEX = 255
print(f"Native functions: hex({HEX}) --> {hex(HEX)}")

NUMBER = 1.6
print(f"Native functions: round({NUMBER}) --> {round(NUMBER)}")


"""
    Global and local variables...
"""

COUNTRY = "United States"


def showCountry():
    STATE = "Florida"
    return f"function call with a global variable --> COUNTRY = '{COUNTRY}'"


print(f"\nGlobal variable: {showCountry()}")
# print(f"Local variable: variable defined inside a function but called outside it --> STATE = {STATE}") # Throw an undefined error.
print(
    f"Local variable: variable defined inside a function but called outside it --> STATE = Undefined"
)


"""
    Additional challenge...
"""


def additional_challenge(str01, str02):
    counter = 0

    print("")
    for i in range(1, 101):
        MULTIPLE_OF_FIVE = i % 5 == 0
        MULTIPLE_OF_THREE = i % 3 == 0

        if MULTIPLE_OF_FIVE and MULTIPLE_OF_THREE:
            print(str01 + str02)
            continue

        if MULTIPLE_OF_FIVE:
            print(str02)
            continue

        if MULTIPLE_OF_THREE:
            print(str01)
            continue

        print(i)
        counter += 1

    return counter


print(
    f"\n{additional_challenge('fizz', 'buzz')} numbers was printed instead of 'fizz' or 'buzz' (function arguments)!"
)
