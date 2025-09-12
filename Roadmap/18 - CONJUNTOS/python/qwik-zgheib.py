# -- exercise

data_list: list[int] = [2, 3, 4, 5]
print(f"original data_list: {data_list}")
print(f"add element at the end: {data_list.append(6)}")
print(f"add element at the beginning: {data_list.insert(0, 1)}")
print(f"add multiple elements at the end: {data_list.extend([7, 8, 9])}")
print(f"add multiple elements at a specific position: {data_list.insert(2, 10)}")
print(f"remove an element at a specific position: {data_list.pop(3)}")
print(f"update the value of an element at a specific position: {data_list[3] == 11}")
print(f"check if an element is in a set: {11 in data_list}")
print(f"remove all content from the set")
data_list.clear()
print(f"final data_list: {data_list}")

# -- extra challenge
set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}

print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
print(f"union: {set_a | set_b}")
print(f"intersection: {set_a & set_b}")
print(f"difference: {set_a - set_b}")
print(f"symmetric difference: {set_a ^ set_b}")
