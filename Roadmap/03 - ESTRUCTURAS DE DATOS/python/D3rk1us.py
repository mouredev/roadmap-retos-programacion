"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
"""

# Listas

nombres= ['Maria', 'Nushi', 'Jose', 'Wei']
apellidos = [] #Lista vacía

matriz = [
    [1, 2, 4, 6, 9],
    [10, 20, 40, 80],
    [11, 22, 33, 44],
]

nombres.sort()  # Ordenar
print(nombres)

apellidos.append('Smith') # Insertar
print(apellidos)

# Tuplas

tupla1 = "Prueba", 34214, 3.2
tupla2 = tupla1, "Tres", "Cuatro", 14

# Conjuntos

frutas = {'Naranja', 'Manzana', 'Pera', 'Uva', 'Granada'}
frutas.remove('Uva')    # Borrar
print(frutas)


# Diccionarios

usuario = {'nombre': 'Marc', 'apellido': 'Spector', 'oficio': 'Agente de Inteligencia'}
usuario['nombre'] = 'Steven'  # Reemplazar
print(usuario)



# /////////////////////////////////////  DIFICULTAD EXTRA (opcional)  /////////////////////////////////////


agenda = [] # Lista para guardar los contactos.
exit = True # Variable para mantener o terminar el bucle While.

# Funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.

def agregar():

    nombre = input("Introduce el nombre del contacto: ")
    numero = input("Introduce el número del contacto: ")

    try:
        # Comprueba si es un número y si tiene menos de 11 dígitos.
        if isinstance(int(numero), int) and len(numero) <= 11:
        
            return agenda.append({'nombre': nombre, 'numero': numero})

    except:

        print("El número no debe tener letras y no debe tener más de 11 dígitos.")
        agregar()

def actualizar():

    opcion = input("Deseas actualizar el 'nombre' o 'número': ")

    if opcion == 'nombre':

        nombre_actual = input("Indica el nombre actual del contacto: ")
        cambio_nombre = input("Indica el nombre al que deseas cambiarlo: ")
         
        for contacto in agenda:

            if contacto['nombre'] == nombre_actual:
                contacto['nombre'] = cambio_nombre
                return contacto

    elif opcion == 'número':
        
        numero_actual = input("Indica el número actual del contacto: ")
        cambio_numero = input("Indica el número al que deseas cambiarlo: ")
        
        try:
            
            if isinstance(int(cambio_numero), int) and len(cambio_numero) <= 11:
                
                for contacto in agenda:

                    if contacto['numero'] == numero_actual:
                        contacto['numero'] = cambio_numero
                        return contacto

        except:

            print("El número no debe tener letras y no debe tener más de 11 dígitos.")
            actualizar()

    else:
        print("Escoger entre 'nombre' o 'número'.")
    
    return 'El contacto no ha sido creado.'

def eliminar():
    
    posicion = 0
    contacto_eliminar = input("Nombre del contacto que se va a eliminar: ")

    for contacto in agenda:

        if contacto['nombre'] == contacto_eliminar:

            break

        posicion += 1

    agenda.pop(posicion)

    return agenda

def buscar():

    nombre = input("Introduce el nombre del contacto que deseas buscar: ")

    for contacto in agenda:

        if contacto['nombre'] == nombre:
            return contacto


# Menú de la agenda y parte principal.

while exit:

    menu = input("¿Qué desea hacer? 'agregar', 'buscar', 'actualizar', 'eliminar', 'mostrar' un contacto o 'salir': ")

    if menu == 'agregar':

        agregar()

    elif menu == 'actualizar':

        print(actualizar())


    elif menu == 'eliminar':

        print(eliminar())

    elif menu == 'buscar':

        print(buscar())
    
    elif menu == 'mostrar':

        print(agenda)
    
    elif menu == 'salir':

        exit = False
    
    else:
        print("Debes escoger entre las opciones indicadas: 'añadir', 'buscar'...")