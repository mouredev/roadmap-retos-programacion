'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
'''

#Listas: Son secuencias mutables usadas normalmente para almacenar objetos homogeneos
frutas = ['naranja', 'manzana', 'fresa', 'pera']
print(f'Esta es una lista: {frutas}')

#Inserción
frutas.insert(0, 'melocoton')
print(f'Vamos a insertar en el indice 0 melocoton {frutas}')

#Borrado
frutas.remove('fresa')
print(f'Vamos a borrar la fresa {frutas}')

#Actualización
frutas[2] = 'kiwi'
print(f'Vamos a cambiar el indice 2 por kiwi {frutas}')

#Ordenación
frutas.sort()
print(f'Vamos a ordenar alfabeticamente las frutas: {frutas}')

#Tuplas: Son secuencias inmutables, usadas normalmente para almacenar información heterogenea
letras = tuple('abc')
print(f'Esto es una tupla : {letras}') #No se puede operar sobre ella ya que es inmutable

#Rangos: Es una secuencia inmutable de numero, normalmente usada para hacer un número determinado de loops en los bucles for
rango = range(10)
print(f'Esto es un rango: {rango}')

#String: Se usan para almacenar caracteres, también son inmutables
cadena = 'Hola mundo'
print(f'Esto es un string: {cadena}')

#Diccionarios: Asocia claves con valores
personas = {
    'juan': {
        'nombre': 'Juan',
        'edad': 25,
        'ciudad': 'Valencia'},
    'javier': {
        'nombre': 'Javier',
        'edad': 26,
        'ciudad': 'Paris'
    }
}
print(f'Esto es un diccionario: {personas}')
#Inserción
personas['juan']['ocupacion'] = 'Desarrollador'
print(f'Vamos a insertarle una ocupación a juan: {personas}')
#Borrado
del personas['javier']['edad']
print(f'Vamos a borrarle la edad a javier: {personas}')
#Actualización
personas['juan']['edad'] = 26
print(f'Vamos a cambiarle la edad a Juan: {personas}')

#Conjuntos: Colección no ordenada de elementos únicos
pares = {0,2, 4, 6, 8, 10}
print(f'Esto es un conjunto {pares}')
#Inserción
pares.add(14)
print(f'Hemos añadido 14 al conjunto: {pares}')
#Borrado
pares.remove(6)
print(f'Hemos borrado el 6 del conjunto: {pares}')
#No se puede actualizar ni ordenar

#Estructuras de control de flujo
for i in range(2):
    if i==0:
        print('Esto es un if dentro de un bucle for')
    else:
        print('Esto es un else dentro de un bucle for')

i = 0
while i < 2:
    print(f'Esto es la iteración {i+1} de un bucle while')
    i += 1

#Funciones
def suma(a, b):
    print(f'Esto es una función que suma {a} y {b}: {a + b}')
suma(5,4)

#Clases y objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

juan = Persona('Juan', 26)

print(f'juan es un objeto con nombre: {juan.nombre} y edad: {juan.edad}')

#Actualización
juan.edad += 1
print(f'Juan ha cumplido {juan.edad} años')

#Inserción
juan.ocupacion = 'Desarrollador'
print(f'Juan ha adquirido la ocupación de: {juan.ocupacion}')

#Borrado
del juan.ocupacion
try:
    print(f'Juan esta trabajando de {juan.ocupacion}')
except:
    print('Juan ha perdido su ocupación')

#Ejercicio EXTRA
''' 
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
 '''

agenda = {} #Iniciamos el diccionario agenda
def add_contact():
    name = input("Ingrese el nombre del contacto a agregar: ")
    phone = input("Ingrese el número de telefono de su contacto: ")
    if (len(phone) > 11):
        print('Error, el número es muy largo')

    elif not phone.isnumeric():
        print('Error, solo puedes introducir numeros para el numero de telefono.')

    else:
        agenda[name] = {'nombre' : name, 'telefono' : phone}
        print('Se ha agregado correctamente el contacto')

    menu()

def search():
    name = input("Introduzca el nombre del contacto que desea consultar: ")
    if name in agenda:
        print(agenda[name])
    else:
        print(f'La persona {name} no se encuentra en su agenda.')

    menu()

def update_contact():
    name = input("Introduzca el nombre del contacto que desea actualizar: ")
    if name in agenda:
        agenda[name]['telefono'] = input('Ingrese el nuevo telefono de su contacto: ')
    else:
        print(f'La persona {name} no se encuentra en su agenda')

    menu()

def delete_contact():
    name = input("Introduzca el nombre del contacto que desea eliminar: ")
    if name in agenda:
        del agenda[name]
    else:
        print(f'La persona {name} no se encuentra en su agenda')

    menu()

def show_contacts():
    print(f'Estos son sus contactos: {agenda}')
    menu()

def menu():
    print('Menu de agenda contactos. Seleccione una opción: ')
    print('1 - Agregar contacto')
    print('2 - Borrar contacto')
    print('3 - Mostrar contactos')
    print('4 - Actualizar contacto')
    print('5 - Salir de la agenda')
    option = input()
    if option == '1':
        add_contact()
    elif option == '2':
        delete_contact()
    elif option == '3':
        show_contacts()
    elif option == '4':
        update_contact()

    elif option == '5':
        print('Hasta la vista')

    else:
        print('Por favor, introduzca un número del 1 al 5.')
        menu()

menu()