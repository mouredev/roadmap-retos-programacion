for number in range(1,11):
    print(number)

print("Termina la iteración del bucle for con range()\n")

number = 0
while number < 10:
    number += 1
    print(number)

print("Termina la iteración del bucle while\n")

numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

print("Termina la iteración del bucle for en listas\n")

#EXTRA
print("EXTRA")
numbers = {1,2,3,4}

for number in numbers:
    print(number)

print("\n----------------------")

dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

for key, value in dictionary.items():
    print(f"{key}: {value}")

print("\n----------------------")

list = [number**2 for number in range(1,6)]
print(list)

print("\n----------------------")

numbers = (1,2,3,4)

for number in numbers:
    print(number)

print("\n----------------------")    

number = 0
while number < 5:
    number += 1
    print("La variable number vale", number)
else:
    print("Se ha completado toda la iteración y la variable number vale", number)