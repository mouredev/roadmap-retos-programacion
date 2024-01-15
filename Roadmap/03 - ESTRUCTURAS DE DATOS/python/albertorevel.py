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

print("\n")


# PART 1.2 - Sets

print("\n** 1.2 - SETS **\n")

a_set = {1,2,"3",True,1}

print("""Sets are created like lists but whitout duplicates (1 is equivalent to True)
 - 'a_set = {1,2,"3",True,1}' -> """ + f"{a_set}\n")

print("\n")


# PART 1.3 - Tuples

print("\n** 1.3 - TUPLES **\n")

a_tuple = (1,2,"3",True,1)

print("""Tuples are inmutables lists
 - 'a_tuple = (1,2,"3",True,1)' -> """ + f"{a_tuple}\n")

print("\n")


# PART 1.4 - Matrices

print("\n** 1.4 - MATRICES **\n")

matrix = [['X','O',' '], ['X','O',' '], ['O','X','X ']]
print(f"""A matrix is a list containing other lists
 - 'matrix = [['X','O',' '], ['X','O',' '], ['O','X','X ']]' 
      -> {matrix}\n""")


# PART 1.5 - Dictionaries

print("\n** 1.5 - DICTIONARIES **\n")

dictionary = {"name": "Alberto", "surname": "Revel", "birthYear": 1992}
print("""A dictionary contains key-value pairs
 - "dictionary = \{'name': 'Alberto', 'surname': 'Revel', 'brithYear': 1992\}' 
      -> """+f"{dictionary}\n")

"""
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""