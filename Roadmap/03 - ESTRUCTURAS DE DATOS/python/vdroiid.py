from collections import deque
"""
    Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
    Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""
#--------------Listas--------------#
lista = []
# Agrega un ítem al final de la lista
lista.append(1)
lista.append(4)
# Agrega un ítem en una posición dada
lista.insert(0, 2)
# Quita el ítem que se especifique en el parámetro 
lista.remove(4)
# Quita el elemento en la posición especificada o, sin argumento, el último
lista.pop()
# Elimina todos los elementos de la lista. Equivale a del lista[:]
lista.clear()
for i in range(5):
    lista.append(i)
# Hace que la lista se ordene alrevés
lista.reverse()
# Para actualizar los datos de la lista se puede hacer mediante el índice
lista[0]=5
# Quita el primer ítem de la lista. HAy que importar deque: from collections import deque
lista = deque(lista)
lista.popleft()
# Quita el ítem especificando su índice
del lista[0]

# --------------Tuplas--------------#
# Se puede definir una tupla así:
t = 321, 675, 'Hola'
t[2] # Selecciona el último ítem
# Aunque la tupla es inmutable es, posible agregarle una lista y, por ende, crecer la lista
tupla = t, [1,2,3,4]
# Agregamos un nuevo elemento a la lista
tupla[1].append(5)
# Esto define una tupla vacía
empty = ()
# Esto crea una tupla con un ítem
singleton = ('Hola',)
# Esto empaqueta los variables dentro de una tupla
letra = 'A'
numero = 1
simbolo = '$'
tupla_nueva = letra, numero, simbolo
# print(tupla_nueva)
# print(singleton)
#--------------Conjuntos--------------#
# Esto crea un conjunto vacío
conjunto = set()
# Esto crea un conjunto de datos
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# Separa las letras y crear un conjunto. Además, elimina cualquier reptido que haya
unicos = set("sisisinonono")
#--------------Diccionarios--------------#
# De est manera se declara un diccionario vació:
diccionario = {}
# De esta menar se puede ingresar datos
diccionario['nombre'] = 'vdroid'
# Se actualiza de la la siguiente manera
diccionario['nombre'] = 'vdroiid'
# Es decir, si existe la clave, actualiza el valor, de lo contarrio lo agrega en el diccionario
diccionario['apellido'] = "Perez"
# De esta menera se puede ordenar el diccionario mediente los claves
sorted(diccionario.keys())
# De esta manera se puede eliminar un elemento en el diccionario
del diccionario['nombre']
# Además se puede eliminar específicamente el último elementp de la lista:
diccionario.popitem()
# print(diccionario)
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""
"""
Nota. Es posible que haya nombres de contactos repetitivos, pero no es el caso del número de teléfono
"""

# Datos de inicio, para probar
lista_contacto = ['Vdroid', '1234567898']

def buscar(nombre, telefono):
    if nombre in lista_contacto and telefono in lista_contacto:
        indice = 0
        # 'c' es el dato que contiene el 'indice' de la lista 
        for indice, c in enumerate(lista_contacto):
            t = indice+1
            if c == nombre and lista_contacto[t] == telefono:
                name = c
                phone = lista_contacto[t]
    else: return 0
    return name, phone

def insertar(nombre, telefono):
    if nombre not in lista_contacto or telefono not in lista_contacto:
        lista_contacto.append(nombre)
        lista_contacto.append(telefono)
        return "Contacto registrado correcamente."
    else: 
        return "El contacto ya existe o no cumple con los requisitos. Velve a intentarlo."
def actualizar(nombre, telefono, new_name, new_phone):
    indice = 0
    # 'c' es el dato que contiene el 'indice' de la lista 
    for indice, c in enumerate(lista_contacto):            
        t = indice+1
        if c == nombre and lista_contacto[t] == telefono:
            lista_contacto[indice] = new_name
            lista_contacto[t] = new_phone
            return "Se actualizó correctamente el contacto."
    else: return "No se pudo actualizar el contato. Vuelve a intentarlo."

def eliminar(nombre, telefono):
    # 'c' es el dato que contiene el 'indice' de la lista 
    for indice, c in enumerate(lista_contacto):
        t = indice+1
        if c == nombre and lista_contacto[t] == telefono:
            del lista_contacto[indice]
            del lista_contacto[indice]
            return "Se eliminó correctamente el contacto."
    return "Algo salió mal, vuelve a intentarlo."

def entrada():
    while True:
        # Funcionamiento principal
        print("""
        1. Buscar contacto
        2. Insertar contacto nuevo
        3. Actualizar contacto
        4. Eliminar un contacto
        5. Salid del programa
        """)
        opcion = input("¿En qué te puedo ayudar? Elige una opción (escribe el número):")
        salida = int(opcion)

        if salida >= 0 and salida <= 6:
            salida = int(opcion)
            break
    return salida
        
def main():
    while True:
        numero = entrada()
        # Para ver lista completa es posible poner la opción 6

        if numero <= 6:
            # 1. Buscar contacto
            if numero == 1:
                nombre_a = input("Para que podamos buscar el contacto, porporciona el nombre de este, por favor:\n")
                telefono_a = input("Para que podamos buscar el contacto específico del usario, porporciona el número telefónico:\n")
                a = buscar(nombre_a, telefono_a)
                if  a != 0:
                    print("\nDatos de contacto:")
                    print("Nombre de contacto: {}".format(a[0]), "Número de teléfono: {}".format(a[1]), sep="\n")
                else: print("Lo siento, el nombre y número telefónico no se encuentran registrado")
            # 2. Insertar contacto nuevo
            elif numero == 2:
               
                # Convertirá en mayúscula la primera letra y omitirán los espacios en el inicio
                nombre_b = input("Escribe el nombre del contacto: ").strip().capitalize()
                telefono_b = input("Escribe el número telefónico: ")
                if len(telefono_b) == 10 and telefono_b.isdigit():
                    b = insertar(nombre_b, telefono_b)
                    if b != 0:
                        print(b)
                    else: print(b)
                else:
                    print("Error al ingresar datos, el número de contacto debe ser exactamente 10 dígitos y de tipo numérico. Vuelve a intentarlo.")
            # 3. Actualizar contacto
            elif numero == 3:
                nombre_c = input("Escribe el nombre del contacto actual: ")
                telefono_c = input("Ahora el número telefónico: ")
                if nombre_c in lista_contacto and telefono_c in lista_contacto:
                    new_name = input("Escribe el nuevo nombre del contacto: ")
                    new_phone = input("Ahora el nuevo número de telefóno: ")
                    if len(telefono_c) == 10 and telefono_c.isdigit():
                        c = actualizar(nombre_c, telefono_c, new_name, new_phone)
                        print(c)
                    else:
                        print("No es posible registrar el contacto si no cumple con la regla general de un contacto. Vuelve a intentarlo.")
                else:
                    print("Posiblemente no se ha registrado el contato que proporcionaste. Vuelve a intentarlo.")
            # 4. Eliminar un contacto
            elif numero == 4:
                nombre_d = input("Escribe el nombre del contacto que desea eliminar: ")
                telefono_d = input("Ahora el número telefónico: ")
                if nombre_d in lista_contacto and telefono_d in lista_contacto:
                    if len(telefono_d) == 10 and telefono_d.isdigit():
                        d = eliminar(nombre_d, telefono_d)
                        print(d)
                    else:
                        print("No es posible registrar el contacto si no cumple con la regla general de un contacto. Vuelve a intentarlo.")
                else:
                    print("Posiblemente no existe el contacto registrado. Vuelve a intentarlo.")
            # 5. Salid del programa
            elif numero == 5:
                break
            # Opción extra
            elif numero == 6:
                print(lista_contacto)
            else:
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Opción inválida. Intente de nuevo.")
    return print("Saliste del programa...")
main()