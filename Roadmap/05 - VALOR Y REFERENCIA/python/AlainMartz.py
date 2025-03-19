#05 VALOR Y REFERENCIA

# EJERCICIO:
# - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
# - Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo
#   se comportan en cada caso en el momento de ser modificadas. 
#   (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

# Variables por valor
# Una variable almacena directamente el valor asignado. Al copiar la variable, se crea una copia independiente del valor orinal.
# Aunque Python no utiliza estrictamente variables por valor, el comportamiento de tipos inmutables (como enteros, flotantes, cadenas, tuplas, booleanos) puede parecerse a este concepto.

x = 123                                   #   
y = x                                     # 'x' e 'y' son independientes luego de la asignación de y=x, entonces, cambiar 'y' no afecta a 'x'  
y = "ciento veintitres"                                 
print(f"""
      x = 123
      y = x
      y = 'ciento veintitres'

La asignación de y = x, no afecta los valores x: {x}, y: {y}
Dirección en la memoria de x: {id(x)}
Dirección en la memoria de y: {id(y)}
      """)

a = 9
b = 4.9
c = "veintiseis"
d = (2,3)
e = True
print(f"Tipos inmutables que son pasados como valor\nEntero: {a}\nFlotante: {b}\nCadena: {c}\nTuplas: {d}\nBooleanos: {e}\n")


# En este ejemplo

n = 10  
def doblar_valor(numero):
    numero *= 2
    return numero

x = doblar_valor(n)
print(f"El valor de x es {x}\nSu ubicación en la memoria es {id(x)}")
print(f"El valor de x es {n}\nSu ubicación en la memoria es {id(n)}")


# Variables por referencia
# Una variable almacena una referencia (o dirección de memoria) al valor real. Al copiar la variable, ambas variables se refieren al mismo valor en memoria.

x = [1,4,7]
y = x
y.append(10)

print(f"""
      x = [1,4,7]
      y = x
      y.append(10)

La asignación de y = x, afecta los valores x: {x}, y: {y}, que tienen la misma asignación de memoria
Dirección en la memoria de x: {id(x)}
Dirección en la memoria de y: {id(y)}
      """)


# otros tipos de variables por referencia

f = ['a','b','c']
g = {'a':1,'b':2,'c':3}
h = {1,2,3}

print(f"Tipos mutables\nLista: {f}\nDiccionario: {g}\nSet: {h}")


### Desafío extra ### 

print("\nDesafio extra\n")

a = 1
b = 2
def reverse(v1,v2):
    v1,v2 = v2,v1
    return v1,v2
x,y = reverse(a,b)

print(f"Variables originales => a:{a}, b:{b}\nVariables nuevas     => x:{x}, y:{y}")

reverse(a,b)

c = [1,2,3]
d = [4,5,6]

def inverse(r1,r2):
    r1,r2 = r2,r1
    return r1, r2

v,w = inverse(c,d)
print(f"Variables originales => a:{c}, b:{d}\nVariables nuevas     => x:{v}, y:{w}")