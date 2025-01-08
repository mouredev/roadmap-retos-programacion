
"""
    Assignment By Value
"""

var1 = 3
var2 = var1

var1 = 4

print(var1)
print(var2)

"""
    Assignment By Reference
"""

var1 = [10, 20]
var2 = var1

var2.append(30)

print(var1)
print(var2)

"""
    Exercise
"""

def ByValue(a: int, b: int) -> tuple:
    c = b
    d = a

    return c, d

original1 = 20
original2 = 30
value1, value2 = ByValue(original1, original2)

print('By Values')
print('Original Values')
print(original1)
print(original2)
print('After Function Values')
print(value1)
print(value2)

def ByReference(a: int, b: int) -> tuple:
    c = b
    d = a

    return c, d

original1 = 20
original2 = 30
value1, value2 = ByReference(original1, original2)

print('By Values')
print('Original Values')
print(original1)
print(original2)
print('After Function Values')
print(value1)
print(value2)