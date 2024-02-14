'''

* EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

'''



# VARIABLES POR VALOR
# Ya que los numericos son inmutables entonces no se cambiaran sus valores al asignarlo a otra variable, se creara una copia de ellas.
a = 400
b = a
b += 5
print(a)
print(b)

# VARIABLES POR REFERENCIA:
# Ya que las lista son tipos de datos asignados por referencia podran ser modificados luego de haber sido asignados a otra variable (tipo de dato mutable)
lista_a = [30, 400, 100]
lista_b = lista_a # Se comparte la referencia
## > Verificamos que no tienen el mismo id con la funcion id()
print(f"Los enteros a y b NO comparten la misma referencia al objeto, id(int_a): {id(a)} ,id(int_b): {id(lista_b)} (NO tienen el mismo id)")

lista_b.append(60)
print(lista_a, lista_b)
## > Para verificar que la lista_a y lista_b comparten la misma referencia del objeto podemos usar la funcion id()
print(f"Las listas a y b comparten la misma referencia al objeto, id(lista_a): {id(lista_a)} ,id(lista_b): {id(lista_b)} (tienen el mismo id)")



# EJEMPLOS VARIABLES POR VALOR
##  TYPE:int
num = 20

def doblar_valor(numero):
    numero*=2
    return numero

print(num)
print(doblar_valor(num))

## TYPE:str
name= "Pedro"

def rename(nombre):
    nombre += " López"
    return nombre

print(f"El nombre fuera de la funcion es:{name} y el nombre modificado por la función es:{rename(name)}")

## TYPE:bool
verdad = True
mentira = False
def doblar_valor(verdad):
    verdad *=2
    return verdad

print(f"El valor bool inicial verdadero '{verdad}' no se ha modificado pero dentro de la función si: {doblar_valor(verdad)}")
print(f"El valor bool inicial falso '{mentira}' no se ha modificado pero dentro de la función si: {doblar_valor(mentira)}")

## TYPE:tuple
variable_tupla = ("Hola", True, 59, "Mundo")
doblar_valor(variable_tupla)
print(f"Al ser una estructura de datos inmutables una vez declara no podrá ser modificada:{variable_tupla} id({id(variable_tupla)})")

# EJEMPLOS VARIABLES POR REFERENCIA
## TYPE:list
variable_lista = [2,4,-5]
doblar_valor(variable_lista) # comparten el mismo id
print(f"Como podemos observar al tener el tipo de dato list() y ser mutable el valor de la lista ha sido actualizado: id({id(variable_lista)}) valor({variable_lista})")

##TYPE: dict
variable_dict={
    "nombre":"Pedro",
    "edad":30,
    "profesion":"fontanero"
}

def agregar_sexo_masculino(variable:dict):
    variable.update({"sexo":"hombre"})
    return variable

agregar_sexo_masculino(variable_dict)
print(f"Como podemos observar al tener el tipo de dato dict() y ser mutable hemos añadido un nuevo par clave:valor --> {variable_dict}")


## TYPE:set

variable_conjunto = {True, "Moure", "❤️"}

def agregar_elemento_unico(elemento:set):
    elemento.add("Gracias por el supp!")
    return elemento

agregar_elemento_unico(variable_conjunto)
print(f"Como podemos observar al tener el tipo de dato set() y ser mutable hemos podido agregar un nuevo dato de tipo string --> {variable_conjunto}")

"""DIFICULTAD EXTRA:"""
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
variable_valor1 = 400
variable_valor2 = "'Hola, Mundo!'"
variable_referencia1 = [30, 600, 81, 20]
variable_referencia2 = {True, "'Soy Un conjunto'", 20}

def modificar_variable_valor(valor1,valor2):
    valor1,valor2 = valor2,valor1
    print(f"Valor 1: ",valor1)
    print(f"Valor 2: ",valor2)
    return valor1,valor2


def modificar_variable_referencia(referencia1,referencia2):
    referencia1,referencia2 = referencia2,referencia1
    print(f"Valor Referencia 1: ",referencia1)
    print(f"Valor Referencia 2: ",referencia2)
    return referencia1,referencia2

resultado1,resultado2 = modificar_variable_valor(variable_valor1,variable_valor2)

resultado3,resultado4 = modificar_variable_referencia(variable_referencia1,variable_referencia2)

print("<<<< RESULTADOS >>>>")
print(f"ANTES:{variable_valor1} | AHORA:{resultado1}")
print(f"ANTES:{variable_valor2} | AHORA:{resultado2}")

print(f"ANTES:{variable_referencia1} | AHORA:{resultado3}")
print(f"ANTES:{variable_referencia2} | AHORA:{resultado4}")




    
