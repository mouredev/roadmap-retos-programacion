"""
EJERCICIO A REALIZAR

 Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""


import os
import textwrap

def limpiar(): #creamos la función para limpiar la pantalla para poder aplicarla las veces que necesitemos sin repetir código
    while True:

        pregunta=input("quieres que limpie la pantalla? (si - no): ")
        if pregunta=="si":
        
            if os.name=="posix":
                os.system("clear")
                break
            else:
                os.system("cls")
                break
        elif pregunta=="no":
            break

# FUNCIONES CON VARIABLES QUE SE LES PASAN "POR VALOR"
limpiar()

print("VAMOS A TRABAJAR LA ASIGNACIÓN DE VARIABLES QUE SE PASAN POR VALOR EN FUNCIONES\n")

print(textwrap.fill("En python siempre se hace referencia a un objeto, pero estos objetos pueden ser mutables o inmutables." 
              "Si pasamos una variable inmutable estamos pasando un valor ya que su modificación dentro de la función no modificará la variable." 
              "Si lo pasamos como referencia ha de ser una variable mutable\n",80))

def multiplicacion3(valor):
    a=valor
    print(f"el valor dentro de la función al multiplicarlo por 3 es {a*3}\n")

print("\nPASAMOS UN VALOR (UN ENTERO) COMO PARÁMETRO DE UNA FUNCIÓN\n")
valor=input("pasame un entero: ")
valor=int(valor)

print(f"antes de la función la variable tiene el valor {valor}\n")
print(textwrap.fill("Si pasamos un valor a la función multiplicacion3(valor), "
      "nos dará un valor diferente al multiplicarlo por 3."
      "Como pasamos un entero de parámetro, la variable no se modificara al ser inmutable, crearemos un nuevo objeto con el nuevo valor.",80))
multiplicacion3(valor)

# FUNCIONES CON VARIABLES QUE SE PASAN COMO "REFERENCIA"

def multiplicaLista3(lista):
    for i in range(len(lista)):
        lista[i]=lista[i]*3

print("VAMOS A ASIGNACIÓN DE VARIABLES QUE SE PASAN POR REFERENCIA\n")
print(textwrap.fill("Ahora vamos a trabajar la referencia. Para ello creamos una variable"
                    "que ha de ser del tipo mutable. Por ejemplo una lista. Así las modificaciones de esa lista"
                    "haran referéncia a un mismo objeto que se modificará con el nuevo valor\n"))
valor=input("\npasame una lista de valores separados por comas: ")
lista=list(map(int,valor.split(",")))
print(f"la lista de valores que has pasado es: {lista}\n")
print("Los pasamos como parámetro de una función multiplicaLista3(lista), y nos da: \n")
multiplicaLista3(lista)
print(f"Ahora nos toca mirar si se han alterado los valores de la lista: {lista}, y observamos que si\n")


# VAMOS A POR LA DIFICULTAD 
print("\nVAMOS A POR EL APARTADO DE DIFICULTAD")
limpiar()
print("DIFICULTAD EXTRA (opcional): " 
               "* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.\n"
               "* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.\n"
               "*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno\n"
               "se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las\n"
               "variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.\n"
               "*   Comprueba también que se ha conservado el valor original en las primeras.")

# definimos la funciones del ejercicio del apartado del parámetro por referencia

def programa1(lista):
    lista[0],lista[1]=lista[1],lista[0]
    return lista


print("empezamos por referencia: \n")
lista=input("pasame una lista de dos valores separados por comas: ")
lista=lista.split(",")
print(f"\nLa lista es: {lista}"+"\n")
print("usamos una función para dar la vuelta a los valores: \n")
print("def programa1(lista):\n"
      "lista[0],lista[1]=lista[1],lista[0]\n"
      "return lista\n")
print("imprimimos el return de la ejecución de la función programa1(lista): " + str(programa1(lista)))
print(f"ahora el valor de la lista original es: {lista}\n\n")

# definimos la funciones del ejercicio del apartado del parámetro por valor

def programa2(tupla):
    nueva_tupla=(tupla[1],tupla[0])
    return nueva_tupla

print("Ahora vamos a crear la función de los parámetros por valor, para eso usamos una tupla\n")
print("def programa2(tupla)\n" 
      "tupla[0],tupla[1]=tupla[0],tupla[1]\n"
      "return tupla\n")
tupla1=input("pasame una lista de dos valores separados por comas: \n")
tupla1=tuple(tupla1.split(","))
print(f"la tupla es: {tupla1}\n")
print("pasamos como parametro de la función la tupla\n")
print("el resultado es: "+str(programa2(tupla1)))
print(f"el valor original de la tupla es: {tupla1}"+"\n")
print("el valor original de la tupla no se puede modificar")