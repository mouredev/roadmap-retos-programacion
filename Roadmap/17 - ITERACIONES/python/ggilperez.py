# 17 Iterators
import itertools

# For loop
print("For")
for i in range(1, 11):
    print(i)
print()

# While
print("While")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

# Recursion
print("Recursion")


def countdown(i=1):
    print(i)
    if i == 10:
        return
    return countdown(i + 1)


countdown()
print()

# Extra

# List can be iterable
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

# Also sets, tuples, dict, strings
for item in (1, 2, 3, 4):
    print(item)
for item in {1, 2, 3, 4}:
    print(item)
for item in {"one": 1, "two": 2}:
    print(item)
for item in "Hello World":
    print(item)

# For loop in comprehensions
print([item for item in my_list])
print((item for item in my_list))
print({item for item in my_list})
print({str(item): item for item in my_list})

# Map
print(list(map(lambda x: x ** 2, my_list)))

# Filter
print(list(filter(lambda x: x % 2 == 0, my_list)))

# Reverse an iterable
for item in reversed(my_list):
    print(item)

# Sorted an iterable
for item in sorted([4,2,1,3]):
    print(item)

# Enumerate
for index, item in enumerate(["one", "two", "three"]):
    print(f"{index = }, {item = }")
