x = 5
y = x  # Assign the value of x to y

y = 10  # Modify y, but it won't affect x

print(x)  # Output: 5
print(y)  # Output: 10

# Value assignment example with a function and variables passed by value -----------------------------------------------------------------------
number_list = [1, 2, 3]
PRINCIPAL_VAR = 5

# Function with a variable passed by value
def double_value(number):
    number *= 2
    return number

print(double_value(PRINCIPAL_VAR))
print(PRINCIPAL_VAR, "- Its value has not been affected\n")  # Original value remains unchanged

# Function with a variable passed by reference
def double_values(numbers):
    for item, number in enumerate(numbers):
        numbers[item] *= 2

double_values(number_list)
print(number_list, "- Its value has been affected")  # Original value modified

# Value assignment example with tuples -----------------------------------------------------------------------
# Tuples are immutable, so they behave as if they are passed by value:
original_tuple = (1, 2, 3)
tuple_copy = original_tuple  # Value assignment with tuples

tuple_copy += (4,)  # Modify tuple_copy, but it won't affect original_tuple because tuples are immutable
# The comma after the 4 is necessary to differentiate it from a simple parenthesis surrounding a value.
print(original_tuple)  # Output: (1, 2, 3)
print(tuple_copy)     # Output: (1, 2, 3, 4)

# Value assignment example with function and variables passed by value -----------------------------------------------------------------------

original_tuple = (1, 2, 3)  # Value assignment with tuples

def modify_tuple(tupla):
    tupla = tupla + (4,)  # Create a new tuple and assign it to the local variable 'tupla'
    print("Inside the function:", tupla)  # The new tuple created inside the function does not affect the original tuple outside the function.

modify_tuple(original_tuple)
print("Outside the function:", original_tuple)  # Output: (1, 2, 3)

# Value assignment by reference -----------------------------------------------------------------------
# The variable points to the same object in memory. Changes to a variable affect both the function and outside the function
# The original variable is directly modified, so the modifications affect the variable outside the function.

list1 = [1, 2, 3]
list2 = list1  # Assign list1's reference to list2

list2.append(4)  # Modify list2, and it affects list1

print("list1:", list1)  # Output: [1, 2, 3, 4]
print("list2:", list2)  # Output: [1, 2, 3, 4]

# Another example with a list -----------------------------------------------------------------------

original = [1, 2, 3]  # Assign the list to original
copy = original  # original and copy are the same list

original[0] = 99  # Modify original

original = [4, 5, 6]  # Reassign a new list to original
print(original)  # Output: [4, 5, 6]
print(copy)  # Output: [99, 2, 3]

# Value assignment example with function and variables passed by reference -----------------------------------------------------------------------

x = [10, 20, 30]
def function(input_param):
    input_param.append(40)

function(x)
print(x)  # Output: [10, 20, 30, 40]


# Note: Reassigning is different from modifying -----------------------------------------------------------------------
# They are different objects, and the original does not change because I am not modifying the variable, but reassigning it, which creates a new temporary one

x = [10, 20, 30]
def function_obj(entry):
    entry.append(40)

function_obj(x)
print(x)    # Output: [10, 20, 30, 40]


# Note, reassigning is different from modifying ----------------------------------------------
# They are different objects, and the original does not change because I am not modifying the variable, but reassigning it, which creates a new temporary one
x = [10, 20, 30]
def function(input_var):
    input_var = []

function(x)
print(x)    # Output: [10, 20, 30]


# id() function -------------------------------------------------------------
# This function returns a unique identifier for each object.
# Returning to the first example, we can see how the objects that "x" and "input_var" point to are different

# id with example of value variable -------------------------------------------------------------
x = 10
print("id value variable: ", id(x)) # 140724755286744
def function(input_var):
    input_var = 0
    print(id(input_var)) # 140724755286744

function(x)  # Output: 10

# id with example of reference variable -------------------------------------------------------------
x = [10, 20, 30]
print("id reference variable: ", id(x)) # 1737715235264
def function(input_var):
    input_var.append(40)
    print(id(input_var)) # 1737715235264

function(x)  # Output: [10, 20, 30, 40]

# id with the last example -------------------------------------------------------------
# It creates a new list in memory and assigns the variable input_var to that new list
# the id of input_var inside the function will be different from the id of x outside the function.

x = [10, 20, 30]
print (id(x))   #1737715235200
def function(input_var):
    input_var = []
    print (id(input_var)) #1737715235264

function(x)
print(x)    # Output: [10, 20, 30]



print()
value_variable1 = 1             # integer
value_variable2 = "Moure"       # string

reference_variable1 = [30, 60, 90]             # list
reference_variable2 = {True, "set", 0}    # set

def swap_value_variables(var1, var2):
    var1, var2 = var2, var1
    print(f"Var1 that was 1, inside the function: {var1}")
    print(f"Var2 that was 'Moure', inside the function: {var2}")
    return var1, var2

def swap_reference_variables(ref1, ref2):
    ref1, ref2 = ref2, ref1
    return ref1, ref2

# call the functions
result_value1, result_value2 = swap_value_variables(value_variable1, value_variable2)
result_reference1, result_reference2 = swap_reference_variables(reference_variable1, reference_variable2)

# print results
print()
print("Whether it's value or reference, it reverses the values")
print(f"Original Values: {value_variable1}, {value_variable2}")
print(f"After passing through the function: {result_value1}, {result_value2}")
print(f"Original Ref: {reference_variable1}, {reference_variable2}")
print(f"After passing through the function: {result_reference1}, {result_reference2}")


# test another function, assign outside the function -------------------------------------------------------------
print()
print("It's a list, it's mutable, and it's by reference, it modifies both")
list1 = [1, 2, 3]
print ("Original List1:", list1)
list2 = list1     
print("List1 reference assigned to List2 outside the function")
print("Original List2:", list2)
num=4

def add_number(temp_list):
    temp_list.append(num) 
    print("Temporary list inside the function:", temp_list)

add_number(list2)
print("Added number 4 to list2 with the add_number function...")
print("List1:", list1)
print("List2:", list2)
print("Both have been modified and only passed the 2 through the add function")

# retrieve the previous list I reversed: reference_variable1 = [30, 60, 90]  
# another test, assign inside the function -------------------------------------------------------------
print()
print("Trying to assign inside the function ref1 as ref2")
print("Original ref1:", reference_variable1)
print("Original ref2:", reference_variable2)
def assign_same_reference_vars(rv1, rv2):
    rv2= rv1
    return rv1, rv2

new_rv1, new_rv2= assign_same_reference_vars(reference_variable1, reference_variable2)
print("New ref1:", new_rv1)
print("New ref2:", new_rv2)


# Another test of Modifying by reference -------------------------------------------------------------
print()
numbers = [1,2,3]
letters = ["a","b","c"]
print("Originals before function:",numbers, letters)

def modify_nums_and_letters(value1, value2):
    numbers.append(value1)
    letters.append(value2)
    return(numbers, letters)

numbers2 , letters2 = modify_nums_and_letters(value1=4, value2="d")

print("With addition:", numbers2, letters2)