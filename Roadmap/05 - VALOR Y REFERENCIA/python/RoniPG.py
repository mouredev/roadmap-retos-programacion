# @RoniPG

# Asignación de variables por valor
"""
Al hacer la asignacion por valor se guarda la copia del original y no su direccion en memoria.
"""
original=5
copia=original
print(f"El valor de original: {original}\nEl valor de la copia: {copia}")
copia=10
print(f"El valor de original al modificar la copia: {original}\nEl nuevo valor de la copia: {copia}")

# Asignación de variables por referencia
"""
Al hacer la asignacion por referencia se pasa la direccion en memoria, en donde las variables que tengan
acceso a la misma estan sincronizadas y cualquier cambio realizado en dicha posicion afectaria a todas.
"""
lista_original=list()
lista_original.append(5)
lista_copia=list()
lista_copia=lista_original
print(f"\nEl valor de original: {lista_original}\nEl valor de la copia: {lista_copia}")
lista_copia.append(10)
print(f"El valor de original al modificar la copia: {lista_original}\nEl nuevo valor de la copia: {lista_copia}")

# Funciones con variables que se les pasan por valor
"""
Las funciones que reciben como parametro la copia del valor no pueden modificar los datos originales
"""
def porValor(a:int,b:int):
    print("***Entramos la funcion porValor***")
    a=45
    b=95
    print(f"El valor de original: {a}\nEl valor de la copia: {b}")
    print("***Salimos de la funcion porValor***")
print(f"\nEl valor de original: {original}\nEl valor de la copia: {copia}")
porValor(original,copia)
print(f"El valor de original despues de la funcion: {original}\nEl valor de la copia despues de la funcion: {copia}\n")

# Funciones con variables que se les pasan referencia
"""
Las funciones que reciben como parametro la referencia de memoria modifican los datos originales
"""
def porReferencia(a:list,b:list):
    print("***Entramos la funcion porReferencia***")
    a.append(45)
    b.append(95)
    print(f"El valor de lista_A: {a}\nEl valor de la lista_B: {b}")
    print("***Salimos de la funcion porReferencia***")
lista_A=list()
lista_A.append(5)
lista_B=list()
lista_B.append(10)
print(f"El valor de lista_A: {lista_A}\nEl valor de la lista_B: {lista_B}")
porReferencia(lista_A,lista_B)
print(f"El valor de lista_A despues de la funcion: {lista_A}\nEl valor de la lista_B despues de la funcion: {lista_B}\n")
"""
DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""
def intercambioPorValor(a:int, b:int):
    print("***Entramos en la funcion intercambioPorValor***")
    temp= a
    a=b
    b=temp
    print("***Salimos de la funcion intercambioPorValor***")
    return a,b
def intercambioPorReferencia(a:list, b:list):
    print("***Entramos en la funcion intercambioPorReferencia***")
    temp= a
    a=b
    b=temp
    print("***Salimos de la funcion intercambioPorReferencia***")
    return a,b

num_A=5
num_B=10
print(f"Valor de num_A: {num_A}.\tValor de num_B: {num_B}")
num_C,num_D=intercambioPorValor(num_A,num_B)
print(f"Valor de num_A: {num_A}.\tValor de num_B: {num_B}")
print(f"Valor de num_C: {num_C}.\tValor de num_D: {num_D}\n")

lista_num_A=list()
lista_num_A.append(5)
lista_num_B=list()
lista_num_B.append(10)
print(f"Valor de lista_num_A: {lista_num_A}.\tValor de lista_num_B: {lista_num_B}")
lista_num_C,lista_num_D=intercambioPorReferencia(lista_num_A,lista_num_B)
print(f"Valor de lista_num_A: {lista_num_A}.\tValor de lista_num_B: {lista_num_B}")
print(f"Valor de lista_num_C: {lista_num_C}.\tValor de lista_num_D: {lista_num_D}")
