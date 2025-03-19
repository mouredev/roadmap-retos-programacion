for i in range(1, 11):
    print(f"for: {i}")

i = 1
while i <= 10:
    print(f"while: {i}")
    i += 1

def count_recursiva(numero: int):
    if numero <= 10:
        print(f"recursividad: {numero}")
        count_recursiva(numero + 1)

count_recursiva(1) 

#extra

for i in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1):
    print(i[1])

for i in reversed(range(1,11)):
    print(i)

lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])

dict = {'alan': 1, 'shakir': 2, 'ramirez': 3, 'lugo': 4, 'chile': 5, 'santiago': 6, 'puente': 7, 'alto': 8, 'sancarlos': 9, 'skatepark': 10}
for i in dict.values():
    print(i)

set = (1,2,3,4,5,6,7,8,9,10)
for i in set:
    print(i)

languages = ['Python', 'C', 'Java', 'Cobol', 'Typescript', 'Javascript']
for i in sorted(languages):
    print(i)
