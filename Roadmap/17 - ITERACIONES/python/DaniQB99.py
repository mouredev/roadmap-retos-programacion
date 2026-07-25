'''
EJERCICIO:
Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
números del 1 al 10 mediante iteración.
'''
# FOR 
for i in range(1,11):
    print(i)

# WHILE
i = 1 
while i <= 10:
    print(i)
    i +=1

# RECURSIVIDAD
def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)

count_ten()
    

'''
DIFICULTAD EXTRA (opcional):
Escribe el mayor número de mecanismos que posea tu lenguaje para 
iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
'''

print("\n\nDIFICULTAD EXTRA\n")

# FOR in list
print('LIST')
for x in [1, 2, 3, 4, 5 , 6 ,7, 8, 9, 10]:
    print(x)
    
# FOR in set
print('SET')
for x in {1, 2, 3, 4 , 5 , 6 ,7, 8, 9, 10}:
    print(x)
    
# FOR in tuple
print('TUPLE')
for x in (1, 2, 3, 4, 5 , 6 ,7, 8, 9, 10):
    print(x)
    
# FOR in dict
print('DICT')
for x in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}:
    print(x)
    
# FOR in dict values
print('DICT VALUES')
for x in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.values():
    print(x)

# FOR in dict keys
print('DICT KEYS')
for x in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.keys():
    print(x)

# FOR in list unpack
print('*' * 10)
print(*[i for i in range(1, 11)], sep="\n")

# FOR in reverse list
print('LIST REVERSA')
for x in reversed([1, 2, 3, 4, 5 , 6 ,7, 8, 9, 10]):
    print(x)

# FOR in sort list
print('LIST SORT')
for x in sorted(["a", "d", "r", "i"]):
    print(x)

# FOR in list enumerate
print('LIST ENCUENTE')
for i, x in enumerate(sorted(['p', 'h', 'y', 't', 'h', 'o', 'n'])):
    print(f"Índice: {i}, valor: {x}")   

# FOR in string'
print('STRING')
for x in 'Python':
    print(x)