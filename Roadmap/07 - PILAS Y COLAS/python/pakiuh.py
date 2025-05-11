'''EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).
'''
#Pilas: Primer elemento que entra es el primero que sale
comunidad_del_anillo = [
    "Frodo Bolsón",
    "Samwise Gamyi",
    "Meriadoc Brandigamo",
    "Peregrin Tuk",
    "Gandalf el Gris",
    "Aragorn",
    "Legolas",
    "Gimli",
    "Boromir"
]
print(f"Inicialmente la Comunidad del Anillo eran: {comunidad_del_anillo}")
#recuperamos el úlitmo miembro introducido
primero_muere_el_ultimo = comunidad_del_anillo.pop()
print(f"Primero muere el último de la lista: {primero_muere_el_ultimo}")
print(f"y ahora la Comunidad del anillo es: {comunidad_del_anillo}")
#añadimos un elmento al final de la lista
comunidad_del_anillo.append("Faramir")
print(f"Y luego conocerán a un nuevo miembro y serán: {comunidad_del_anillo}")

#Colas: Los últimos serán los primeros, como la cola del Mercadona
jedis_caidos = [ #Lista de Jedis muertos
    "Qui-Gon Jinn",         # Episodio I – asesinado por Darth Maul
    "Coleman Trebor",       # Episodio II – asesinado por Jango Fett durante la batalla de Geonosis
    "Aayla Secura",         # Episodio III – ejecutada durante la Orden 66
    "Ki-Adi-Mundi",         # Episodio III – ejecutado durante la Orden 66
    "Plo Koon",             # Episodio III – ejecutado durante la Orden 66
    "Saesee Tiin",          # Episodio III – asesinado por Darth Sidious
    "Agen Kolar",           # Episodio III – asesinado por Darth Sidious
    "Mace Windu",           # Episodio III – asesinado (presuntamente) por Anakin y Palpatine
    "Luminara Unduli",      # (su muerte no se muestra, pero se confirma en la era del Imperio)
    "Luke Skywalker",       # Episodio VIII – se une a la Fuerza tras su proyección en Crait
    "Leia Organa",          # Episodio IX – muere ayudando a redimir a su hijo, Ben Solo
]

#Añadimos un nuevo Jedi:
jedis_caidos.append("Ben Solo (Kylo Ren)")  # Episodio IX – se sacrifica para revivir a Rey")

print(jedis_caidos)

#muere_primer_jedi_lista
primer_jedi_muerto = jedis_caidos.pop(0)
print(f"El primer jedi que muere en las películas de Star Wars es: {primer_jedi_muerto}")
print(f"Ahora los Jedis que todavía quedan vivos son: {jedis_caidos}")

'''DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.'''

#Simulación de mecanismo adelanta detrás con un navegador web
texto = "No todos los que vagan están perdidos. El viejo que olvida su nombre puede aún recordar el camino. La luz brilla más cuando la oscuridad se aproxima."

listado_de_texto_por_palabras = texto.split()
print(listado_de_texto_por_palabras)

posicion_cursor = len(listado_de_texto_por_palabras)-1

def atras():
    global posicion_cursor
    if posicion_cursor>0:
        posicion_cursor -=1
        print(listado_de_texto_por_palabras[posicion_cursor])
    else:
        print("⚠️ Ya estás al principio del texto.")

def adelante():
    global posicion_cursor
    if posicion_cursor<len(listado_de_texto_por_palabras)-1:
        posicion_cursor +=1
        print(listado_de_texto_por_palabras[posicion_cursor])
    else:
        print("⚠️ Ya estás al final del texto.")

def menu():
    while True:
        opciones = input("Pulsa 1 para adelante, 2 para atrás, 3 salir: ")
        if opciones == "1":
            adelante()
        elif opciones == "2":
            atras()
        elif opciones == "3":
            break
        else:
            print("Opción no válida")
menu()

'''Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.'''

#Tenemos un conjunto de cómics de Marvel en formato pdf que queremos imprimir y están ordenados según debería leerlo
comics_marvel = [
    "House of M",          # Wanda altera la realidad — afecta a todo el universo Marvel
    "Civil War",           # Consecuencias sociales y políticas tras House of M
    "Planet Hulk",         # Hulk es exiliado tras causar estragos en la Tierra
    "Infinity Gauntlet",   # Thanos se convierte en el mayor villano cósmico
    "Spider-Verse"         # Multiverso y diferentes versiones de Spider-Man, independiente pero ideal tras conocer el universo
]

def imprimir_comic():
    imprimiendo = comics_marvel.pop(0)
    print(f"La impresora está imprimiendo el cómic {imprimiendo} para que puedas leerlo, quedan pendientes {len(comics_marvel)} por leer")

def añadir_comic(titulo):
    comics_marvel.append(titulo)
    print(f"Tienes un nuevo cómic pendiente de leer e imprimir, el {titulo} se añade a tu cola de comics pendientes que en estos momentos es {comics_marvel}")

añadir_comic("Secret Wars")
imprimir_comic()
imprimir_comic()
añadir_comic("Spider-Geddon")