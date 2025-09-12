"""
Exercise
"""
list_data = [10, 20, 30, 40, 50]
print(f"Initial list: {list_data}")

list_data.append(60)
print(f"Adden an element at the end: {list_data}")

list_data.insert(0, 5)
print(f"Element added at the begin: {list_data}")

list_data.extend([70, 80, 90])
print(f"Several elements added at the end: {list_data}")

list_data[3:3] = [25, 35]
print(f"Several elements added at a specific position: {list_data}")

list_data.pop(2)
print(f"Element removed at position 2: {list_data}")

list_data[5] = 45
print(f"Value of an element updated at position 5: {list_data}")

element_present = 50 in list_data
print(f"Element present: {element_present}")

list_data.clear()
print(f"List cleared: {list_data}")


"""
Extra
"""
a = {1, 2, 3}
b = {3, 4, 5}
print(f"Conjuntos a y b: {a}, {b}")

union_result = a | b
intersection_result = a & b
difference_result = a - b
symmetric_difference_result = a ^ b

print({
    "union": union_result,
    "intersection": intersection_result,
    "difference": difference_result,
    "symmetric_difference": symmetric_difference_result
})
