# @author Alberto Revel

"""
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
"""

print("\n**** PART 1 - CREATING DATA STRUCTURES ****\n")


# PART 1.1 - Lists

print("\n** 1.1 - LISTS **\n")

list1 = []
list2 = list()
print(f"""There are two ways to create lists, that produces the same result
 - 'list1 = []' -> {list1}
 - 'list2 = list()' ->  {list2}\n""")

list1 = [1,2,True,'something',5,1]
list2 = list([1,2,True,'something',5,1])
print(f"""\nWe can initiate lists with some elements (that can have different types)
 - list1 = '[1,2,True,'something',5,1]' ->  {list1}
 - list2 = 'list([1,2,True,'something',5,1])' -> {list2}\n""")


# PART 1.2 - Sets

print("\n** 1.2 - SETS **\n")

set1 = {1,2,"3",True,1}
print("""Sets are created like lists but whitout duplicates (1 is equivalent to True)
 - 'set1 = {1,2,"3",True,1}' -> """ + f"{set1}\n")


# PART 1.3 - Tuples

print("\n** 1.3 - TUPLES **\n")

tuple1 = (1,2,"3",True,1)
print("""Tuples are inmutables lists
 - 'tuple1 = (1,2,"3",True,1)' -> """ + f"{tuple1}\n")


# PART 1.4 - Matrixes

print("\n** 1.4 - MATRIXES **\n")

matrix1 = [['X','O',' '], ['X','O',' '], ['O','X','X ']]
print(f"""A matrix is a list containing other lists
 - 'matrix1 = [['X','O',' '], ['X','O',' '], ['O','X','X ']]' 
      -> {matrix1}\n""")


# PART 1.5 - Dictionaries

print("\n** 1.5 - DICTIONARIES **\n")

dictionary1 = {"name": "Alberto", "surname": "Revel", "birthYear": 1992}
print("""A dictionary contains key-value pairs
 - "dictionary1 = \{'name': 'Alberto', 'surname': 'Revel', 'brithYear': 1992\}' 
      -> """+f"{dictionary1}\n")

"""
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""


print("\n**** PART 2 - OPERATING WITH DATA STRUCTURES ****\n")


# PART 2.1 - List

print("\n** 2.1 - LIST **\n")
list3 = [5,2,-1,10,0]
print(f"Being the initial list : {list3}")
list3.append(2)
print(f" - We add the element '2' at the end with append(): {list3}")
list3.extend([5,9,1])
print(f" - We add the elements '[5,9,1]' at the end with extend() : {list3}")
list3.insert(2,4)
print(f" - We add the element '4' at the position 2 with insert(): {list3}")
list3+=[8,11]
print(f" - We add the elements '[8,11]' at the end through concatenation: {list3}")
list3.remove(2)
print(f" - We remove the first element '2' with remove() : {list3}")
list3.pop()
print(f" - We remove the last element with pop(): {list3}")
list3.pop(5)
print(f" - We remove the element at position 5 with pop(): {list3}")
list3.sort(reverse=True)
print(f" - We sort the list in reverse order with sort(reverse=): {list3}")
list3.clear()
print(f" - We remove all the elements with clear() : {list3}")

# PART 2.2 - Set

print("\n** 2.2 - SET **\n")
set2 = {5,2,-1,10,0}
print(f"Being the initial set : {set2}")
set2.add(3)
print(f" - We add the element '3' with add() : {set2}")
set2.add(3)
print(f" - We add the element '3' with add() (nothing happens because duplicates aren't possible in a set) : {set2}")
set2.update([5,9,1])
print(f" - We add the elements '[5,9,1]' with update() : {set2}")
set2.remove(2)
print(f" - We remove the element '2' with remove() : {set2}")
set2.discard(2)
print(f" - We remove the element '2' with discard() if present : {set2}")
set2.discard(3)
print(f" - We remove the element '3' with discard() if present : {set2}")
set2.pop()
print(f" - We remove an arbitrary element with pop() : {set2}")
set2.intersection_update({1,2,3,4,5,8,9,11})
print(" - We keep only the elements contained in set and in '{1,2,3,4,5,8,9,11}' with intersection_update(): "+f"{set2}")
set2.difference_update({1,2,8,6,10})
print(" - We remove the elements contained in '{1,2,8,6,10}' with difference_update(): "+f"{set2}")
set2.symmetric_difference_update({1,2,8,9,10})
print(" - We keep only the elements contained in set or in '{1,2,8,9,10}' but not both with symmetric_difference_update(): "+f"{set2}")
set2.clear()
print(f" - We remove all the elements with clear() : {set2}")

# PART 2.3 - Tuple

print("\n** 2.3 - TUPLE **\n")
tuple2 = (5,2,-1,10,0)
print(f"Being the initial tuple : {tuple2}")
tuple2+=(3,)
print(f" - We add the element '3' using the addition operator : {tuple2}")
tuple2+=(8,2)
print(f" - We add the elements '(8,2)' using the addition operator : {tuple2}")


# PART 2.4 - Matrix

print("\n** 2.3 - Matrix **\n")
matrix2 = [['X','O','X'], ['X','O',' '], ['O','X','X ']]
print(f"Being the initial matrix : {matrix2}")
matrix2.append(['O','O','X'])
print(f"- We add the elements '['O','O','X']' with append() : {matrix2}")
matrix2.pop()
print(f"- We remove elements at the end with pop() : {matrix2}")
matrix2.sort()
print(f" - We remove all the elements with clear() : {matrix2}")
print("PS: As a matrix is a list of lists, all list operations are allowed")
