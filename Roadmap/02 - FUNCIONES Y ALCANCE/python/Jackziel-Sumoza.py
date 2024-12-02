# function without argument
def function():
    pass
function()

# function with unique argument and without return
def function_1(name):
    print(f"Hello {name}")
function_1("World")


# function with two argument and one return
def function_2(name,lastname):
    return f"Hello {name} and hello {lastname}"
result = function_2("world","Python")
print(result)

# function multi-argument
def function_3(*num):
    print(sum(num))
function_3(1,2,3,4,5,6,7,8,9)

# function with one default argument 
def function_4(name="Python"):
    print(f"Hello {name}")
function_4()

# function key-value
def function_5(**values):
    for key, value in values.items():
        print(f"The {key} is {value}")
function_5(name="Jackziel",lastname="Sumoza",age="?")

# function in function
def hello(name):
    print(f"hello {name}")
    def bye(name):
        print(f"see you soon {name}")
    bye(name)
hello("World")

# native function
print(type(4.4))

# local variable
def function_6():
    local_var = "Python"
    print(f"Hello, {local_var}")
# print(local_var); error
function_6()

# global variable
global_variable = "This is a global variable"
print(global_variable)

# additional difficult
print()
def occurrence(text_1,text_2):
    occurrence_num = 0
    for num in range(1,101):
        if num % 3 == 0:
            print(text_1)
        elif num % 5 == 0:
            print(text_2)
        elif num % 3 == 0 and num % 5 == 0:
            print(text_1 + text_2)
        else:
            occurrence_num += 1
            print(num)
    return occurrence_num

result = occurrence("Hello","Bye")
print()
print(result)