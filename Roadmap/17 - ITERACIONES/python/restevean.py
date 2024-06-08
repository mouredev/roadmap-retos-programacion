"""
Exercise
"""

print("#01 - Using 'for' with a range")
for i in range(1, 11):
    print(i)

print("#02 - Using 'while':")
i = 1
while i <= 10:
    print(i)
    i += 1

print("#03 - Using list comprehension:")
print(*[i for i in range(1, 11)], sep='\n')

"""
Extra
"""

print("#04 - List iteration:")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    print(item)

print("#05 - Using 'map':")
list(map(print, range(1, 11)))

print("#06 - Using dictionaries iteration:")
my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
for key, value in my_dict.items():
    print(key, value)

print("#07 - Using 'Iterators':")
iterable = iter(range(1, 11))
for value in iterable:
    print(value)

print("#08 - Using 'generators':")


def generate_numbers():
    for i in range(1, 11):
        yield i


for number in generate_numbers():
    print(number)

print("#09 - Using 'enumerate':")
for index, value in enumerate(range(1, 11), start=1):
    print(index, value)

print("#10 - Using recursion:")


def recursive_print(n):
    if n > 0:
        recursive_print(n - 1)
        print(n)


recursive_print(10)
