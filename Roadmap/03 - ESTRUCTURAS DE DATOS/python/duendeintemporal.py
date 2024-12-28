#3 { Retos para Programadores } ESTRUCTURAS DE DATOS
# # Assigning the print function to log
log = print

# Primitive Data Types
# Number: Represents both integer and floating-point numbers.
# Python uses the built-in float type to represent both integers and floating-point values.

age = 35  # Integer
total = 118.87  # Floating-point
log('age:', age, ', total:', total)  # age: 35, total: 118.87
log(0.3)  # 0.3
# To define a floating-point value, you must include a decimal point and at least one number after the decimal point.

oct_num = 0o45  # Octal representation
log(oct_num)  # 37

hex_num = 0x2f  # Hexadecimal representation
log(hex_num)  # 47
# Note: Numbers created using octal or hexadecimal format are treated as decimal numbers in all arithmetic operations.

# There is a special numeric value called NaN (Not a Number) in Python, represented by float('nan').
# It indicates when an operation intended to return a number has failed.
# For example, dividing any number by 0 raises an error in Python, unlike JavaScript.

# The value NaN has unique properties. Any operation involving NaN always returns NaN.
# In Python, we can check for NaN using math.isnan().

import math

log('Hi man how you doing?' * 4)  # Hi man how you doing?Hi man how you doing?Hi man how you doing?Hi man how you doing?
log(math.isnan(math.nan))  # True, since NaN is not equal to itself

# For this reason, Python provides the math.isnan() function.

try:
    # Attempt to check if the value is NaN
    print(math.isnan("04"))  # This will raise a TypeError
except TypeError as e:
    # Handle the TypeError that occurs when the input is not a float
    print(f"Error: {e}. The input must be a float. Cannot be converted to NaN")

# Note: There is a particular difference between the float() and int() functions when they are used to convert types.

# String: Represents a sequence of characters.
# The str data type represents a sequence of zero or more Unicode characters.
# Strings can be delineated by either double quotes ("), single quotes ('), or triple quotes (''' or """)

dreamy_girl = "Lucy"
song = dreamy_girl + ' in the sky with diamonds'
song_info = f'"{song}" is a song from The Beatles that alludes to LSD'
log(song_info)  # "Lucy in the sky with diamonds" is a song from The Beatles that alludes to LSD

# Character Literals
# The String data type includes several character literals to represent nonprintable or otherwise useful characters.
# In Python, escape sequences are similar to JavaScript.

# Example of escape sequences:
# \n New line
# \t Tab
# \\ Backslash (\)
# \' Single quote (')
# \" Double quote (")

# Template literals in Python can be achieved using f-strings.
num1 = 40
num2 = 80

sum_result = f'{num1} + {num2} = {num1 + num2}'
log(sum_result)  # "40 + 80 = 120"

# Raw Strings
# In Python, raw strings can be created by prefixing the string with 'r'.
# This prevents escape sequences from being processed.

# Unicode demo
# \u57A8 is the 垨 character.
log('\u57A8')  # 垨

# Raw string demo
log(r'\u57A8')  # \u57A8

# Newline demo
log('first line\nsecond line')  # first line\nsecond line
log(r'first line\nsecond line')  # first line\nsecond line

# Boolean: Represents a logical entity and can have two values: True and False.
# The Boolean type is one of the most frequently used types in Python.
# In Python, True and False are case-sensitive and distinct from numeric values.

is_checked = True
log(not is_checked)  # False
# Note that the Boolean literals True and False are case-sensitive.

# Undefined: A variable that has been declared but has not yet been assigned a value.
somebody = None  # In Python, None is used to represent the absence of a value.
log(somebody)  # None

explicitly_undefined = None  # Using None instead of void(0)
log(explicitly_undefined)  # None
# Note: The use of void(0) is not applicable in Python.

# Null: Represents the intentional absence of any object value.
# In Python, None is commonly used to initialize variables.
animals = None
log(animals)  # None

# Symbol: A unique and immutable primitive value, often used as object property keys.
# Python does not have a direct equivalent to JavaScript's Symbol, but we can use unique objects.

class UniqueSymbol:
    def __init__(self, name):
        self.name = name

Id = UniqueSymbol('xm')
other_id = UniqueSymbol('xm')
log('equal symbols:', Id == other_id)  # False, as they are different instances

# You can also use unique identifiers as object properties.

# Create a unique identifier for the email property
email_symbol = UniqueSymbol('email')

class User:
    def __init__(self, name, email):
        self.name = name
        self.__dict__[email_symbol.name] = email  # Use the unique symbol as the key for the email property

    # Method to get the email
    def get_email(self):
        return self.__dict__[email_symbol.name]

# Create a new user
user1 = User('Barbarella', 'softbaby@something.com')

log(user1.name)  # Barbarella
log(user1.get_email())  # softbaby@something.com

# Trying to access the email property directly
log(user1.__dict__.get(email_symbol.name))  # softbaby@something.com
log(getattr(user1, 'email', None))  # None, as 'email' is not a property of the object

# BigInt: Represents integers with arbitrary precision.
big_number = 765466743212345679874653358945321
log(big_number)  # 765466743212345679874653358945321

# Note: Many modern cryptographic libraries and implementations do use arbitrary precision integers
# to handle large integers, especially for operations that involve large prime numbers.

# Reference Data Types

# Object: A collection of key-value pairs. In Python, this is represented by a dictionary.
debian = {
    'name': 'Debian',
    'description': 'Ardilla parlante cuyo nucleo esta basado en un Sistema Operativo del mismo nombre, lucha contra el Sistema establecido y habita más alla del Borde(el Universo conocido)',
    'location': 'No Found',
}

# Method to simulate speaking (not directly translatable from JS arrow function)
def speak():
    log(debian['description'])

# Call the speak function
speak()  # Ardilla parlante cuyo nucleo esta basado en un Sistema Operativo del mismo nombre, lucha contra el Sistema establecido y habita más alla del Borde(el Universo conocido)

import random

# Array: A special type of object used to store ordered collections of values.
# In Python, lists are used to store ordered collections of values and can hold elements of any type.

friends = ['Susan', 'Maryatta', 'Denise', 'Luna', 'Kena', 'Maria']
log(friends)  # Logs the list of friends

# Function: A special type of object that can be called to perform a specific task.
# Functions can also be stored in variables, passed as arguments, and returned from other functions.

from_value = 4
to_value = 12

def random_value(from_value, to_value):
    return random.randint(from_value, to_value)

count = from_value
while count <= to_value:
    log('random value:', random_value(from_value, to_value))
    count += 1
# Logs: numbers between 4 and 12 inclusive

# Specialized Data Structures
# Set: A collection of unique values. In Python, sets can store any type of value, and duplicate values are automatically removed.

unique_numbers = {4, 4, 3, 5, 8, 1, 8, 1, 7}
log(unique_numbers)  # Logs: {1, 3, 4, 5, 7, 8}

# Dictionary: A collection of key-value pairs where keys can be of any type.
# In Python, dictionaries maintain the insertion order of their elements.

map_dict = {}
map_dict['gopi_name'] = 'Khamala'
map_dict['age'] = 35
log(map_dict['gopi_name'])  # Logs: Khamala

# Note: Python does not have a direct equivalent to WeakSet and WeakMap.
# However, we can use weak references from the `weakref` module.

import weakref

# Define a custom class that can be weakly referenced
class MyObject:
    pass

# WeakSet: Similar to a Set, but it holds "weak" references to its values.
weak_set = weakref.WeakSet()
obj = MyObject()  # Create an instance of MyObject
weak_set.add(obj)
print(obj in weak_set)  # Logs: True

# WeakMap: Similar to a Map, but it holds "weak" references to its keys.
weak_map = weakref.WeakKeyDictionary()
key_obj = MyObject()  # Create an instance of MyObject
weak_map[key_obj] = "crasylady"
print(weak_map[key_obj])  # Logs: crazylady

# Note: Garbage collection allows memory management by automatically allocating what is needed
# and reclaiming memory that is no longer being used.

# Typed Arrays: Python does not have a direct equivalent to JavaScript's typed arrays.
# However, we can use the `array` module for similar functionality.

from array import array

# int8Array: Represents an array of 8-bit integers.
int8_array = array('b', [-3, 5, -8, 99, 76])
log(int8_array.tolist())  # Logs: [-3, 5, -8, 99, 76]

# Uint8Array: Represents an array of 8-bit unsigned integers.
uint8_array = array('B', [1, 2, 3])

# Uint8ClampedArray: Not directly available in Python, but we can clamp values manually.
uint8_clamped_array = [max(0, min(255, x)) for x in [-1, 256, 100]]

# Int16Array: Represents an array of 16-bit signed integers.
int16_array = array('h', [1, -2, 3])

# Uint16Array: Represents an array of 16-bit unsigned integers.
uint16_array = array('H', [1, 2, 3])

# Int32Array: Represents an array of 32-bit signed integers.
int32_array = array('i', [1, -2, 3])

# Uint32Array: Represents an array of 32-bit unsigned integers.
uint32_array = array('I', [1, 2, 3])

# Float32Array: Represents an array of 32-bit floating-point numbers.
float32_array = array('f', [1.5, 2.5, 3.5])

# Float64Array: Represents an array of 64-bit floating-point numbers.
float64_array = array('d', [1.5, 2.5, 3.5])

# BigInt64Array: Python's int can handle arbitrary precision, so we can use it directly.
big_int64_array = [1, 2, 3]  # Using a regular list for BigInt64Array

# BigUint64Array: Similar to BigInt64Array, using regular list for BigUint64Array.
big_uint64_array = [1, 2, 3]

# Logs: [1, 2, 3]
# Note: In Python, integers can be of arbitrary precision, so we don't have a specific BigInt type.

# Simulating a window event listener in a web environment
# In Python, we don't have a direct equivalent to the browser's window object,
# but we can simulate the behavior using a function.

def on_load():
    # Simulating the body of a web page
    body_style = {
        'background': '#000',
        'text-align': 'center'
    }
    
    title = 'Retosparaprogramadores #3.'
    title_style = {
        'font-size': '3.5vmax',
        'color': '#fff',
        'line-height': '100vh'
    }
    
    # Simulating the addition of the title to the body
    log(f"Title: {title} (styled with {title_style})")
    
    # Simulating an alert
    print('Retosparaprogramadores #3. ')

# Simulating the load event
on_load()


'''   EXTRA DIFFICULTY (optional):
   Create a contact book via the terminal.
       You must implement functionalities for searching, inserting, updating, and deleting contacts.
       Each contact must have a name and a phone number.
       The program first asks which operation you want to perform, and then the necessary data to carry it out.
       The program cannot allow the input of non-numeric phone numbers and those with more than 11 digits (or the number of digits you choose).
       An option to terminate the program should also be provided.
'''

import re

# Initialize an empty list to store contacts
contacts = []

def show_menu():
    print("--- List of Contacts ---")
    print("1. Insert Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    option = input("Choose an Option: ")
    if option == '1':
        insert_contact()
    elif option == '2':
        search_contact()
    elif option == '3':
        update_contact()
    elif option == '4':
        delete_contact()
    elif option == '5':
        print("Exiting the program...")
    else:
        print("No Valid Option. Try again.")
        show_menu()

def insert_contact():
    try:
        name = input("Type the contact name: ")
        
        telefone = input("Type the telephone number (11 digits): ")
        if not re.match(r'^\d{11}$', telefone):
            print("Invalid telephone number. Must be a numeric value and have 11 digits.")
            return show_menu()
        
        email = input("Type the email of the contact: ")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            print("Invalid email. Must be a valid email address.")
            return show_menu()
        
        contacts.append({'name': name, 'telefone': telefone, 'email': email})
        print(f"Contact {name} added.")
    
    except Exception as error:
        print("An error occurred:", error)
    finally:
        show_menu()

def search_contact():
    name = input("Enter the name of the contact to search: ")
    contact = next((c for c in contacts if c['name'].lower() == name.lower()), None)
    if contact:
        print(f"Contact found: {contact['name']}, Telefone: {contact['telefone']}, Email: {contact['email']}")
    else:
        print("Contact not found.")
    show_menu()

def update_contact():
    try:
        name = input("Type the name of the contact to update: ")
        contact = next((c for c in contacts if c['name'].lower() == name.lower()), None)
        
        if contact:
            telefone = input("Type the new telephone number (11 digits): ")
            if re.match(r'^\d{11}$', telefone):
                contact['telefone'] = telefone
                print(f"Contact {name} updated with new number.")
            else:
                print("Invalid telephone number. Must be a numeric value and have 11 digits.")
            
            email = input("Type the email of the contact: ")
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(email_regex, email):
                contact['email'] = email
                print(f"Contact {name} updated with new email.")
            else:
                print("Invalid email. Must be a valid email address.")
        else:
            print("Contact not found.")
    
    except Exception as error:
        print("An error occurred:", error)
    finally:
        show_menu()

def delete_contact():
    name = input("Type the name of the contact to delete: ")
    index = next((i for i, c in enumerate(contacts) if c['name'].lower() == name.lower()), None)
    if index is not None:
        deleted_contact = contacts.pop(index)
        print(f"Contact {deleted_contact['name']} deleted.")
    else:
        print("Contact not found.")
    show_menu()

# Start the program
show_menu()


