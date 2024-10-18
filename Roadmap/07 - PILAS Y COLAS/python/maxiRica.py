"""
 * EJERCICIO:
 
 Implementa los mecanismos de introducción y recuperación de elementos propios de las
 pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 o lista (dependiendo de las posibilidades de tu lenguaje).
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

limpiar()

# PILAS

print("\n\nVAMOS A CREAR UNA PILA\n\n")
print(textwrap.fill("\nEn una pila se añade al monto superior de una pila, y se saca de arriba abajo. Osea, se inserta al final y se saca también el último elemento entrado",80))
pila=input("\n\nañade una lista de objetos en la pila, separados por comas: \n\n")
pila=pila.replace(" ","").split(",")
while True:
  a=int(input("\ndime que quieres hacer, añadir (1) - retirar (2) - listar la pila (3) - salir (4): \n"))
  if a ==1:
      add=input("\ndame el nuevo objeto a añadir: \n")
      pila.append(add)
  elif a == 2:
      print(f"\nel objeto que sale es: {pila.pop()}\n")
  elif a == 3:
      for a in pila:
          print(a)
  elif a == 4:
      break
  
limpiar()

# COLAS

print("\n\nVAMOS A CREAR UNA PILA\n\n")
print(textwrap.fill("\nEn una cola el primer objeto que entra, es el primero que sale\n",80))
cola=input("\n\nAñade una lista de objetos en la cola, separados por comas: \n\n")
cola=cola.replace(" ","").split(",")
while True:
  a=int(input("\ndime que quieres hacer, añadir (1) - retirar (2) - listar la pila (3) - salir (4): \n"))
  if a ==1:
      add=input("\ndame el nuevo objeto a añadir: \n")
      cola.append(add)
  elif a == 2:
      print(f"\nel objeto que sale es:\n {cola.pop(0)}\n")
  elif a == 3:
      for a in cola:
          print("\n")
          print(a)
  elif a == 4:
      break

limpiar()

"""
DIFICULTAD EXTRA. PRIMER EJERCICIO:
 - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
   el nombre de una nueva web.
"""

print("\n\nConstrucción de la barra de navegación web\n\n")
pagina_web=[]   # establecemos la lista donde pondremos las direcciones web
posicion=-1     # generamos un indice para movernos dentro de la lista (se trabaja en modo pila)
while True:
    print(textwrap.fill("Para navegar escribe la dirección web. Si quieres volver a la web anterior escribe \"anterior\", si quieres avanzar a la sigüiente \"siguiente\", o \"exit\" para parar el programa",80))
    print("\n\n")
    clave=input("ESCRIBE LA WEB: ")

    if clave == "exit":
        break
    if clave=="anterior":       # establecemos un marco para no salirnos por delante
        if posicion>0:  
            posicion-=1
            print(f"\nla página web anterior es: {pagina_web[posicion]}\n\n")
        else:    
            print("\n\nNo hay página web anterior\n\n")
    elif clave=="siguiente":    # Establecemos un límite para no salirnos por la cola
        if posicion<(len(pagina_web)-1):
            posicion+=1
            print(f"\nla página web siguiente es: {pagina_web[posicion]}\n\n")
    else:
        if posicion != len(pagina_web)-1:
            pagina_web=pagina_web[:posicion+1]

        pagina_web.append(clave)
        posicion += 1
    print(f"\n\nTE ENCUENTRAS EN LA PÁGINA WEB: {pagina_web[posicion]}\n\n")

"""
DIFICULTAD EXTRA. SEGUNDO EJERCICIO:

 - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
   impresora compartida que recibe documentos y los imprime cuando así se le indica.
   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
   interpretan como nombres de documentos.
"""

print("\n\nCONSTRUCCIÓN DE UNA COLA DE IMPRESIÓN\n\n")
cola_impresora=[]
indice_cola=0
while True:
    in_dades=(input("\n\nintroduce texto a imprimir, o \"imprime\" para imprimir, o \"exit\" para salir: \n"))
    
    if in_dades=="exit":
        break
    elif in_dades!="imprimir":
            cola_impresora.append(in_dades)
            indice_cola+=1
    elif cola_impresora:
        print(f"\nSe imprime: {cola_impresora.pop(0)}\n")
        indice_cola-=1
    else:
        print("\nNo hay elementos a imprimir\n")
