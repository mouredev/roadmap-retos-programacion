#FUNCTIONS 
# 1. Function without parameters and without return
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

# 2. Function with parameters and without return
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Maria")  # Output: Hello, Maria!
greet_person("Juan")   # Output: Hello, Juan!

# 3. Function without parameters but with return
def get_greeting():
    return "Hello, World!"
message = get_greeting()
print(message)  # Output: Hello, World!

# 4. Function with parameters and with return
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8
result = add(10, 20)
print(result)  # Output: 30
result = add(-1, 1)
print(result)  # Output: 0

# 5. Function with default parameters
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")
greet_with_default()          # Output: Hello, Guest!
greet_with_default("Laura")   # Output: Hello, Laura!

# 6. Function with variable number of parameters

#6.1 Using *args (positional arguments)
def sum_all(*args):
    return sum(args)
total = sum_all(1, 2, 3)
print(total)  # Output: 6
total = sum_all(10, 20, 30, 40)
print(total)  # Output: 100

#6.2 Using **kwargs (keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Rodrigo", age=30, city="New York")
# Output:   name: Rodrigo
#           age: 30 

#7. Functions with returning multiple values
def get_coordinates():
    return (10, 20) # returns a tuple
x, y = get_coordinates()
print(f"x: {x}, y: {y}")  # Output: x: 10, y: 20

#8. Lambda functions (anonymous functions)
square = lambda x: x * x 
print(square(5))  # Output: 25
print(square(10)) # Output: 100
#------------------------------
double = lambda x: x * 2
print(double(5))  # Output: 10
print(double(10)) # Output: 20
#------------------------------
triple = lambda x: x * 3
print(triple(5))  # Output: 15
print(triple(10)) # Output: 30

#9. Recursive functions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1
print(factorial(6))  # Output: 720

#2. We can create functions inside other functions using nested functions.
#3.Example 
def greet():
    def greet_person(name):
        print(f"Hello, {name}!")
    print("Hello, World!")
    greet_person("Oliver")

greet()
# Output:   Hello, World!
#           Hello, Oliver!

#Example nested for calculation of area and perimeter of a rectangle
def rectangle_properties(length, width):
    def area():
        return length * width
    def perimeter():
        return 2 * (length + width)
    return area(), perimeter()
area, perimeter = rectangle_properties(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")
# Output: Area: 15, Perimeter: 16

#4. Scope of variables
#Example of local and global scope  
x = 10  # Global variable (available throughout the entire script)
def modify_variable():
    x = 5  # Local variable (only exists while the function runs.)
    print(f"Inside function, x: {x}")  # Output: Inside function, x: 5
modify_variable()
print(f"Outside function, x: {x}")  # Output: Outside function, x: 10

#Example of using global keyword to modify global variable inside a function
y = 20  # Global variable   
def modify_global_variable():
    global y
    y = 15  # Modifies the global variable
    print(f"Inside function, y: {y}")  # Output: Inside function, y: 15
modify_global_variable()
print(f"Outside function, y: {y}")  # Output: Outside function, y: 15


#Optional Challenge

def transform_string(str_input, str_input2):
    for char in range(1, 101):
        count = 0
        if char % 3 == 0 and char % 5 == 0:
            print(str_input + str_input2)
        elif char % 3 == 0:
            print(str_input)
        elif char % 5 == 0:
            print(str_input2)
        else:
            print(char)
            count += 1
    return count
            
            
