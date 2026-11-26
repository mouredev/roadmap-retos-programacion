# EJERCICIO
# FOR
for i in range(1, 11):
    print(i) 
    
# WHILE
i = 1
while i <= 10:
    print(i)
    i += 1

#RECURSIVIDAD
def count_ten(i = 1):
    if i <= 10:
        print(i)
        count_ten(i+1)
count_ten() 

# EXTRA
for e in [5, 6, 7, 8]:
    print(e)
     
for e in {9, 10, 11, 12}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)
    
# List Comprehension
print(*[i for i in range(1, 11)], sep="\n")
[print(i) for i in range(21, 31)]

nums = [i for i in range(41, 51)]
print(*nums, sep="\n")


for c in "Python":
    print(c) 

for e in reversed([5, 6, 7, 8]):
    print(e)
    
for x in sorted(["R", "I", "C", "K"]) :
    print(x) 
    
for x in enumerate(sorted(["R", "I", "C", "K"])) :
    print(x)

for i, x in enumerate(sorted(["R", "I", "C", "K"])) :
    print(f"índice:{i},  valor:{x}")
    
    
# FUNCION GENERADORA CON YIELD
def contar_hasta(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in contar_hasta(10):
    print(num)
    
gen = contar_hasta(7)
print(next(gen)) # 1
print(next(gen)) 
print(next(gen))
print(next(gen))
print(next(gen)) 
print(next(gen))
print(next(gen)) #7
 

# EXPRESION GENERADORA
cuadrados = (x**2 for x in range(10))

# List Comprehension
cubos = [x**3 for x in range(10)] # guarda los valores en una lista en memoria

for c in cuadrados:
    print(c)
    
for k in cubos:
    print(k)
    
print(cubos[2])        # 8, funciona
print(len(cubos))      # 10
#print(cuadrados[2])  # TypeError: no admite indexación
#print(len(cuadrados))# TypeError: no tiene len    
    


# map() con función
list(map(print, range(61, 71)))   
    

# zip(): iterar dos iterables en paralelo
for n, letra in zip(range(1, 4), "abcd"):
    print(n, letra)
    
# Diccionario con .items()
for key, value in {"a": 1, "b": 2}.items():
    print(key, value)
    
# Walrus en un while
datos = iter(range(5, 11))
while (n := next(datos, None)) is not None:
    print(n)
    
# SIN Walrus
datos = iter(range(5, 11))   # nuevo iterador
while True:
    n = next(datos, None)
    if n is None:
        break
    print(n)   
