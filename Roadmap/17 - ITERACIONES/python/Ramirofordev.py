# Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir numeros del 1 al 10 mediante iteracion

for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1

[print(i) for i in range(1, 11)]

# Extra challenge

numbers = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 , 10]
for number in numbers:
    print(number)

for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1

def recursive_numbers(number):
    if number == 10:
        return number
    else:
        print(number)
        return recursive_numbers(number + 1)

print(recursive_numbers(1))

numberss = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 , 10]

while i < len(numberss):
    print(i)
    i += 1