"""
* EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""
# Listas
lista = [1, 'Hola']
print(f'Lista: {lista}')
print(type(lista))
lista.append('Adios') # Añadir
print(f'Añadir {lista}')
lista.remove('Hola') # Borrar
print(f'Borrar {lista}')
print(lista[0]) # Acceso
lista[0] = "Hasta luego" # Actualización
print(f'Actualizar {lista}')
lista.sort() # Ordenación
print(f'Ordenar {lista}')

# Conjuntos
conjunto = {'1', 'Hola'}
print(f'Conjunto: {conjunto}')
print(type(conjunto))
conjunto.add('Adios') # Añadir
print(f'Añadir al conjunto {conjunto}')
conjunto.remove('Adios') # Borrar
print(f'Borrar del conjunto {conjunto}')

# Diccionarios
diccionario = { 'nombre':'Pepe', 'edad': 37}
print(f'Diccionario: {diccionario}')
print(type(diccionario))
diccionario['email'] = 'pepe37@gmail.com' # Insertar propiedad
print(f'Inserción de una propiedad {diccionario}')
diccionario['edad'] = 55 # Actualizar propiedad
print(f'Actualización de una propiedad {diccionario}')
del diccionario['edad'] # Eliminar propiedad
print(f'Eliminar una propiedad {diccionario}')

# Tuplas, son inmutables y sus elementos deben ser todos del mismo tipo para poder ordenarlas
tupla:tuple = ('1', 'Hola')
print(f'Tupla: {tupla}')
print(type(tupla))
print(tupla[0]) # Acceso
ordenada = tuple(sorted(tupla)) # Ordenación
print(f'Tupla ordenada: {ordenada}')

# DIFICULTAD EXTRA
print('*************************')
print('*                       *')
print('*   AGENDA TELEFÓNICA   *')
print('*                       *')
print('*************************')

agenda:dict = { }

def buscar(telefono:int):        
    if telefono in agenda:
        nombre = agenda[telefono]
        return nombre
    else:
        print(f"¡El teléfono {telefono} no existe!")    

def insertar():
    nombre = input('Introduce el nombre: ')
    telefono = input('Introduce el telefono ')
    if telefono.isdigit() and telefono.__len__ == 0 and telefono.__len__ > 11:
        print('El número de teléfono debe tener entre 1 y 11 dígitos')
    else:
        telefono = int(telefono)
    if telefono in agenda:
        agenda[telefono] = nombre
        print(f'Datos actualizados {agenda}')
    else:
        agenda[telefono] = nombre
        print(f'Datos insertados {agenda}')

def borrar(telefono):    
    if telefono in agenda:
        del agenda[telefono]        
    else:
        print(f'El teléfono {telefono} no existe')

def agendar():
    while True:
        ope = input('¿Que quieres hacer Buscar, Insertar, Actualizar, Eliminar, Salir [ B / I / A / E / S ] ')
        ope = ope.lower()
        match ope:
            case 'b':
                telefono = int(input('Introduce el número de teléfono: '))
                nombre = buscar(telefono)
                if nombre is None:
                    print('No existen datos en la agenda')
                else:
                    print(f'El nombre asignado al teléfono {telefono} es {nombre}')
            case 'i':                
                    insertar()
            case 'a':
                    insertar()
            case 'e':
                telefono = int(input('Introduce el telefono '))
                borrar(telefono)
            case 's':
                print('Adios!!')
                break   
            case _:
                print('¡Opción no implementada!')
agendar()