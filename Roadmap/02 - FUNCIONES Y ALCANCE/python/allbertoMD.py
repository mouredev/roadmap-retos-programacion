# Function Without Parameters
print("\nFunction Without Parameters")
def function_without_parametars():
    print("I'm a function")
function_without_parametars()


# Function With One Parameter
print("\nFunction With One Parameter")
def function_with_one_parameter(name):
    print(f"Hello, {name}")
function_with_one_parameter("Reggie")


# Function With Default Parameters
print("\nFunction With Default Parameters")
def function_with_default_parameters(name = "Samantha"):
    print(f"Hello, {name}")
function_with_default_parameters()


# Function With Multiple Parameters
print("\nFunction With Multiple Parameters")
def function_with_multiple_parameters(name, age):
    print(f"{name} is {age} year old")
function_with_multiple_parameters("Carl", 40)


# Function With Return Value
print("\nFunction With Return Value")
def function_with_return_value(a, b) -> int:
    return a * b
return_value = function_with_return_value(20, 40)
print(return_value)

    
# Function With Variable Number of Parameters
print("\nFunction With Variable Number of Parameters")
def function_with_variable_number_of_parameters(*parameters):
    print(parameters)
function_with_variable_number_of_parameters("a", "e", "i", "o", "u")


## Funciton with Variable Parameters key Value
print("\nFunciton with Variable Parameters key Value")
def function_with_variable_key_value_parameters(**user_data):
    for key, value in user_data.items():
        print(f"{key}: {value}")
function_with_variable_key_value_parameters(name="Tamy", age=32, city="New York")


# Function Inside a Function
print("\nFunction Inside a Function")
def function_insede_the_function():
    print("I'm a main function.")
    def second_function():
        print("I'm a function inside other function")
    second_function()    
function_insede_the_function()


# Function With Function as Parameter
print("\nFunction With Function as Parameter")
def function_with_function_as_parameter(function, a, b):
    print(function(a, b))
function_with_function_as_parameter(lambda  a, b: a + b, 4, 10)


# Sistem Function
print("\nSistem Function")
tuple = (1, 2, 3)
list = list(tuple)
print(sum(list))


# Global Variable
print("\nGlobal Variable")
global_variable = 100
def Function_with_global_variable():
# Local Variable
    print(f"The global variable value is: {global_variable}")
Function_with_global_variable()

# Local Variable
print("\nLocal Variable")
def function_with_local_variable():
    local_variable = 200
    print(f"The local variable value is: {local_variable}")
function_with_local_variable()




##############################################################

# Extra Difficulty
print("\nExtra Difficulty")

def multiples_by_word(w1="Hello", w2="World"):
    counter = 0

    for number in range(0, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(w1 + " " + w2)
        elif number % 3 == 0:
            print(w2)
        elif number % 5 == 0:
            print(w2)
        else:
            counter += 1
            print(number)

    return counter
multiples_by_word()
print(f"The number appear {multiples_by_word()} times")