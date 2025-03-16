# Assignment by value (immutable types)
num1 = 5
num2 = num1
num2 = 7
print(num1)  # Output: 5
print(num2)  # Output: 7

# Assignment by reference (mutable types)
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # Output: [1, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4]


# Function with variable passed by value
def increment(num):
    num += 1
    return num


num = 5
increment(num)
print(num)  # Output: 5


# Function with variable passed by reference
def append_elem(lst, elem):
    lst.append(elem)


lst = [1, 2, 3]
append_elem(lst, 4)
print(lst)  # Output: [1, 2, 3, 4]


# Program 1: Immutable types (mimics pass by value)
def swap_values(a, b):
    a, b = b, a
    return a, b


x = 5
y = 10
new_x, new_y = swap_values(x, y)

print(x, y)  # Output: 5 10
print(new_x, new_y)  # Output: 10 5


# Program 2: Mutable types (pass by reference)
def swap_lists(a, b):
    a[:], b[:] = b[:], a[:]
    return a, b


list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list1, new_list2 = swap_lists(list1, list2)

print(list1, list2)  # Output: [4, 5, 6] [1, 2, 3]
print(new_list1, new_list2)  # Output: [4, 5, 6] [1, 2, 3]
