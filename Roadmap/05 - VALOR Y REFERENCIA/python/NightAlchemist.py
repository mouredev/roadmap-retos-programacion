import copy

# Assignment by value (immutable types)
a = 10
b = a
b = 20
print("a:", a)  # Output: a: 10
print("b:", b)  # Output: b: 20

# Assignment by reference (mutable types)
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print("list1:", list1)  # Output: list1: [1, 2, 3, 4]
print("list2:", list2)  # Output: list2: [1, 2, 3, 4]

# To avoid reference assignment with mutable types, use copy
list3 = [1, 2, 3]
list4 = copy.copy(list3)
list4.append(4)
print("list3:", list3)  # Output: list3: [1, 2, 3]
print("list4:", list4)  # Output: list4: [1, 2, 3, 4]

# Function demonstrating assignment by value
def modify_value(x):
    x = 20
    print("Inside modify_value, x:", x)  # Output: x: 20

# Function demonstrating assignment by reference
def modify_list(lst):
    lst.append(4)
    print("Inside modify_list, lst:", lst)  # Output: lst: [1, 2, 3, 4]

# Assignment by value
a = 10
print("Before modify_value, a:", a)  # Output: a: 10
modify_value(a)
print("After modify_value, a:", a)  # Output: a: 10

# Assignment by reference
list1 = [1, 2, 3]
print("Before modify_list, list1:", list1)  # Output: list1: [1, 2, 3]
modify_list(list1)
print("After modify_list, list1:", list1)  # Output: list1: [1, 2, 3, 4]

'''
Extra
'''

# Function to swap values (immutable types)
def swap_values(x, y):
    return y, x

# Function to swap references (mutable types)
def swap_references(lst1, lst2):
    return lst2, lst1

# Immutable types
a = 5
b = 10
print("Original a:", a)  # Output: a: 5
print("Original b:", b)  # Output: b: 10
new_a, new_b = swap_values(a, b)
print("Swapped new_a:", new_a)  # Output: new_a: 10
print("Swapped new_b:", new_b)  # Output: new_b: 5
print("After swap, original a:", a)  # Output: a: 5
print("After swap, original b:", b)  # Output: b: 10

# Mutable types
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Original list1:", list1)  # Output: list1: [1, 2, 3]
print("Original list2:", list2)  # Output: list2: [4, 5, 6]
new_list1, new_list2 = swap_references(list1, list2)
print("Swapped new_list1:", new_list1)  # Output: new_list1: [4, 5, 6]
print("Swapped new_list2:", new_list2)  # Output: new_list2: [1, 2, 3]
print("After swap, original list1:", list1)  # Output: list1: [1, 2, 3]
print("After swap, original list2:", list2)  # Output: list2: [4, 5, 6]