#5 { Retos para Progarmadores } VALOR Y REFERENCIA
log = print  # Shortening print function to log

# Variables by Value

# In Python, immutable data types (such as int, float, str, and tuple) are assigned by value.
# This means that when you assign a primitive value to a variable, a copy of that value is made.

a = 44  # a is an integer (immutable type)
b = a   # b is assigned the value of a

log(a)  # 44
log(b)  # 44

b += 20  # Changing b does not affect a
log(a)  # 44
log(b)  # 64

# Variables by Reference

# In Python, mutable data types (such as list, dict, and set) are assigned by reference.
# This means that when you assign a mutable object to a variable, you are actually assigning a reference to that object, not a copy of it.

obj1 = {"name": "Julia"}  # obj1 is a dictionary (mutable type)
obj2 = obj1                # obj2 is assigned the reference of obj1

log(obj1["name"])  # Julia
log(obj2["name"])  # Julia

obj2["name"] = "Karla"  # Changing obj2 affects obj1 because they reference the same object
log(obj1["name"])  # Karla
log(obj2["name"])  # Karla

obj2["age"] = 32
log(obj2["age"])  # 32
log(obj1["age"])  # 32

# Lists (Mutable Type) in Python are also reference types.

arr1 = [7, 4, 90]  # arr1 is a list (mutable type)
arr2 = arr1        # arr2 is assigned the reference of arr1

log(arr1)  # [7, 4, 90]
log(arr2)  # [7, 4, 90]

arr2.append(42)  # Modifying arr2 affects arr1
log(arr1)  # [7, 4, 90, 42]
log(arr2)  # [7, 4, 90, 42]

# By Value: Immutable types (e.g., int, str) are copied when assigned to a new variable.
# By Reference: Mutable types (e.g., dict, list) are assigned by reference, meaning changes to one variable affect the other if they reference the same object.

# In Python, functions are also first-class objects, which means they can be assigned to variables, passed as arguments, and returned from other functions.
# When you assign a function to a variable, you are assigning a reference to that function, not a copy of it.

# Functions Assigned by Reference

# When you assign a function to a new variable, both variables point to the same function in memory.

def greet():
    log("Hello everybody! It's time for coding...")

greet_copy = greet  # greet_copy is assigned the reference of greet

greet()      # Hello everybody! It's time for coding...
greet_copy()  # Hello everybody! It's time for coding...

# Changing the function reference
greet_copy = lambda: log("This world is turning into a weird scenario with all those AIs, M2M (technology), and there are cyber attacks that can explode beepers, cell phones, and big media that shows only a tiny fragment of reality.")

greet_copy()  # This world is turning into a weird scenario with all those AIs, M2M (technology), and there are cyber attacks that can explode beepers, cell phones, and big media that shows only a tiny fragment of reality.

# Passing Functions as Arguments

# You can pass functions as arguments to other functions. This demonstrates that functions are treated as reference types.

def call_funct(fn):
    fn()

def say_bye_lady():
    log("See you later, lady!")

call_funct(say_bye_lady)  # See you later, lady!

# Returning Functions from Functions

# You can also return functions from other functions, which shows that functions can be created dynamically and assigned by reference.

# Function that returns another function (closure)
def say_something_to(greeting):
    return lambda name: log(f"{greeting}, {name}!")

say = say_something_to("Welcome to coding lab")
say2 = say_something_to("It's a long way home")

say("Nicky")  # Welcome to coding lab, Nicky
say2("Jhon")  # It's a long way home, Jhon

# Modifying Functions

# Since functions are reference types, if you modify a function that is referenced by multiple variables, it will affect all references.

def hi_miss():
    log("Hello, miss. Have a beautiful day")

func_ref = hi_miss  # func_ref points to hi_miss

func_ref()  # Hello, miss. Have a beautiful day

# Modifying the original function
hi_miss = lambda: log("Sometimes I feel jealous of the wind that caresses your hair, sometimes the rain....")

func_ref()  # Hello, miss. Have a beautiful day (still points to the original function)

# But if we do, for example...
func_ref = lambda: hi_miss()

func_ref()  # Sometimes I feel jealous of the wind that caresses your hair, sometimes the rain.... (now every change in hi_miss will be reflected)

# In Python, when you pass arguments to a function, the behavior depends on whether the argument is a primitive type (passed by value) or a reference type (passed by reference).

# Function that takes a primitive type (passed by value)
def do_something(value):
    value = 20  # This change does not affect the original variable
    log("Value Inside do_something:", value)  # Value Inside do_something: 20

# Function that takes an object (passed by reference)
def set_user_name(obj, name):
    obj['name'] = name  # This change affects the original object
    log("Value Inside set_user_name:", obj['name'])

# Testing the functions
num = 'something'
log("Value Before do_something:", num)  # Value Before do_something: something
do_something(num)
log("After do_something:", num)  # After do_something: something (remains unchanged)

user = {'name': "Luna", 'age': 32}
log("Before set_user_name:", user['name'])  # Before set_user_name: Luna
set_user_name(user, 'Kia')  # Value Inside set_user_name: Kia
log("After set_user_name:", user['name'])  # After set_user_name: Kia (changed)

# Note: the same applies to lists that are reference values.

# Simulating a window load event (not applicable in standard Python, but for demonstration)
def on_load():
    body_style = {
        'background': '#000',
        'text-align': 'center'
    }
    
    title = {
        'text': 'Retosparaprogramadores #5.',
        'font-size': '3.5vmax',
        'color': '#fff',
        'line-height': '100vh'
    }
    
    log("Title:", title['text'])
    
    # Simulating a delay (not applicable in standard Python, but for demonstration)
    import time
    time.sleep(2)
    log('Retosparaprogramadores #5')  # this will be logged at the end

# Call the simulated load function
on_load()

# EXTRA DIFFICULTY (optional):

user1 = {
    'name': 'Kasperle',
    'age': 12
}

user2 = {
    'name': 'Snoopy',
    'age': None
}

log('user1:', user1)  # user1: {'name': 'Kasperle', 'age': 12}
log('user2:', user2)  # user2: {'name': 'Snoopy', 'age': None}

def change_user(obj1, obj2):
    provisional = obj1.copy()  # Create a shallow copy
    obj1.update(obj2)  # Update obj1 with obj2
    obj2.update(provisional)  # Update obj2 with the original obj1

change_user(user1, user2)

log('user1:', user1)  # user1: {'name': 'Snoopy', 'age': None}
log('user2:', user2)  # user2: {'name': 'Kasperle', 'age': 12}

def swap_values(a, b):
    return b, a  # Return the swapped values as a tuple

# You can call the function and use tuple unpacking to assign the returned values to new variables:

x = 85
y = 17

log("Before swap:", x, y)  # Before swap: 85 17

# Call the function and unpack the returned tuple
d, e = swap_values(x, y)

log("After swap:", x, y)  # After swap: 85 17
log('New variables with values swapped:', d, e)  # New variables with values swapped: 17 85

# Note: tuple unpacking allows us to achieve the effect of reference values with primitive values.
# By using tuple unpacking, we can achieve both effects: conserving the original values or swapping the values.
log("Before swap:", x, y)  # Before swap: 85 17
x, y = swap_values(x, y)

log("After swap:", x, y)  # After swap: 17 85

# Note: using tuple unpacking allows us to achieve both effects: conserving the original values or swapping the values.

# Note2: Keep in mind that when you use copying methods like copy(), it creates a shallow copy,
# which means that if there are nested objects inside, the nested ones won't be copied.


