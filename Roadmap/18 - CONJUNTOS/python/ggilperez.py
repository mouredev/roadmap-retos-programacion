# 18 Sets

data = [1, 2, 3, 4]
print(f"Initial {data = }")

data.append(5)
print(f"Insert at end {data = }")

data.insert(0, 0)
print(f"Insert at beginning {data = }")

data.extend([6,7,8])
print(f"Insert multiple elements {data = }")

data[2:2] = [9,11]
print(f"Insert multiple elements at some index {data = }")

data.pop(1)
print(f"Remove element at index {data = }")

data[3] = 54
print(f"Update element at index {data = }")

print(f"Check if element 3 exists in data: {3 in data}")

data.clear()
print(f"Clear {data = }")

# Extra
print(f"Union {set([1,2]).union(set([3,4])) = }")
print(f"Intersection {set([1,2]).intersection(set([2,3])) = }")
print(f"Union {set([1,2]).difference(set([2,3])) = }")
print(f"Union {set([1,2]).symmetric_difference(set([2,3])) = }")


