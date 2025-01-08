# Asignación por Valor (Enteros, Flotantes, cadenas de texto)
# Asignación de variables 
x = 10
y = x

# Modificación de una variable
x = 20

# Imprimir variables
print("x:", x)  # Salida: x: 20
print("y:", y)  # Salida: y: 10 (No se modifica)

# Asginación por Referencia (Listas, diccionarios, conjuntos)
# Asignación de variables
lista1 = [1, 2, 3]
lista2 = lista1

# Modificación de una variable 
lista1.append(4)

# Imprimir variables
print("lista1:", lista1)  # Salida: lista1: [1, 2, 3, 4] (lista1 se modifica)
print("lista2:", lista2)  # Salida: lista2: [1, 2, 3, 4] (lista2 también se modifica)

## Modificando por valor
def modificar_valor(numero):
    numero += 10
    return numero

x = 5
print("Antes de llamar a la función:", x)  # Salida: Antes de llamar a la función: 5
modificar_valor(x)
print("Después de llamar a la función:",x)  # Salida: Después de llamar a la función: 5 (x no cambia)

resultado = modificar_valor(x)
print("En cambio aca si se modifica el valor",resultado)


## Modificando por referencia
def modificar_lista(lista, valor):
    lista.append(valor)

mi_lista = [1, 2, 3]
print("Antes de llamar a la función:", mi_lista)  # Salida: Antes de llamar a la función: [1, 2, 3]

valor = int(input("Ingrese un valor:"))
modificar_lista(mi_lista, valor)
print("Después de llamar a la función:", mi_lista) 

### Ejercicio Opcional ### 

# Modificando por valor
a = 10
b = 20

def modificar_numeros(valor1, valor2):
    a = valor2
    b = valor1
    return(a,b)

print(a,b)
c, d = modificar_numeros(a,b)

print(a, b, c, d)

# Modificando por referencia

frutas = ["Manzana","Pera", "Naranja"]
verduras = ["Pepino","Cebolla", "Repollo"]

def modifica_fruta_verdura(valor1, valor2):
    frutas.append(valor1)
    verduras.append(valor2)
    return(frutas, verduras)

fruta_agregar = input("Ingrese fruta a agregar")
verdura_agregar = input("Ingrese verdura a agregar")
frutas2 , verduras2 = modifica_fruta_verdura(fruta_agregar, verdura_agregar)
print(frutas, verduras, frutas2, verduras2)