import functools
import itertools

"""
ITERATIONS
"""

# for
for i in range(1, 11):
    print(i)

# while
i = 1
while i <= 10:
    print(i)
    i += 1


# recursive
def count_numbers(i: int, num: int):
    if i <= num:
        print(i)
        count_numbers(i + 1, num)


count_numbers(1, 10)


"""
    EXTRA EXERCISE
"""

# --- for variants ---

# 4. for over a list
print("4. for over a list")
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# 5. for over a tuple
print("5. for over a tuple")
for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(i)

# 6. for over a set
print("6. for over a set")
for i in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
    print(i)

# 7. for over dict keys
print("7. for over dict keys")
for i in {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
}:
    print(i)

# 8. for over dict values
print("8. for over dict values")
for v in {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
}.values():
    print(v)

# 9. for over a string
print("9. for over a string")
for c in "Python":
    print(c)

# 10. reversed
print("10. reversed")
for i in reversed(range(1, 11)):
    print(i)

# 11. sorted
print("11. sorted")
for i in sorted([10, 3, 7, 1, 5, 8, 2, 9, 4, 6]):
    print(i)

# 12. unpacking with sep
print("12. unpacking with sep")
print(*range(1, 11), sep="\n")

# --- other mechanisms ---

# 13. list comprehension
print("13. list comprehension")
[print(i) for i in range(1, 11)]

# 14. map
print("14. map")
list(map(print, range(1, 11)))

# 15. enumerate
print("15. enumerate")
for i, _ in enumerate(range(10), start=1):
    print(i)

# 16. generator expression
print("16. generator expression")
gen = (i for i in range(1, 11))
for i in gen:
    print(i)

# 17. iter + next
print("17. iter + next")
it = iter(range(1, 11))
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# 18. itertools.islice + itertools.count
print("18. itertools.islice")
for i in itertools.islice(itertools.count(1), 10):
    print(i)

# 19. functools.reduce
print("19. functools.reduce")
functools.reduce(lambda _, i: print(i), range(1, 11), None)
