# Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# lista o pila
nombres = ["Rick", "Andy", "Jinx"]
print(f"Lista o pila: {nombres}")
# tupla
numeros = (1,2,3)
print(f"Tupla: {numeros}")
# conjunto
numeros_2 = {4,5,6}
print(f"Conjunto: {numeros_2}")
# conjunto inmutable
numeros_3 = frozenset({4,5,6})
print(f"Conjunto inmutable: {numeros_3}")
# diccionario
significados = {
    "name" : "Nombre",
    "username": "Nombre de usuario"
}
print(f"Diccionario: {significados}")
# bytearray
bytearray(5)
print(f"Bytearray: {bytearray(5)}")
# rango
range(2)
print(f"Rango: {range(10)}")
# memory view
memoryview(bytes(5))
print(f"Memoryview: {memoryview(bytes(5))}")
print("")

# Utiliza operaciones de inserción, borrado, actualización y ordenación.
# lista o pila
# inserción
# agrega un elemento al final
nombres.append("Luna")
nombres.append("Candy")
print(f"Inserción: {nombres}")
# agrega multiples elementos al final
nombres.extend("Luna")
print(f"Inserción: {nombres}")
# agrega un elemento al indice
nombres.insert(0,"Snoopy")
print(f"Inserción: {nombres}")
#borrado
# especifico
nombres.remove("Luna")
print(f"Borrado: {nombres}")
# por indice o ultimo
nombres.pop(5)
print(f"Borrado: {nombres}")
nombres.pop()
print(f"Borrado: {nombres}")
#actualización
nombres[5] = "a"
print(f"Borrado: {nombres}")
#ordenación
#alfabetico
nombres.sort()
print(nombres)
#invierte
nombres.reverse()
print(nombres)

#conjuntos
# inserción
# agrega un elemento al final
numeros_2.add(7)
numeros_2.add(8)
numeros_2.add(9)
numeros_2.add(10)
numeros_2.add(11)
numeros_2.add(12)
print(numeros_2)
#eliminación
#elimina el numero mencionado
numeros_2.remove(7)
print(numeros_2)
#elimina el numero mencionado, sin error si no existe
numeros_2.discard(6)
print(numeros_2)
#elimina y devuelve un elemento aleatorio
numeros_2.pop()
numeros_2.pop()
print(numeros_2)

#diccionarios
# inserción/actualización
significados.update({
    "pass": "Contrasena",
    "name" : "Nombres",
    "username" : "Nombres de usuario",
    "password" : "qwerty",
    "email" : "@hotmail.com"

})
print(f"Diccionario actualizado: {significados}")
# eliminación directa
significados.pop("pass")
print(f"Diccionario eliminado: {significados}")
#elimino el ultimo item
significados.popitem()
print(f"Diccionario eliminado: {significados}")


"""
* Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

contactos = {}

MIN_DIGITOS = 10
MAX_DIGITOS = 11

def verificar_tel(telefono):
    telefono = telefono.strip()

    if not telefono.isdigit():
        raise ValueError("El telefono debe ser numérico")

    if len(telefono) < MIN_DIGITOS:
        raise ValueError(f"El telefono debe tener al menos {MIN_DIGITOS} dígitos")

    if len(telefono) > MAX_DIGITOS:
        raise ValueError(f"El telefono no debe tener más de {MAX_DIGITOS} dígitos")

    return telefono  # lo devuelvo validado (string)

def agenda(n):
    match n:
        case 1:
            print("1. Buscar contacto")
            nombre = input("Ingrese el nombre del contacto: ").strip()
            if nombre in contactos:
                return contactos[nombre]
            return f"Contacto {nombre} no existe"

        case 2:
            print("2. Insertar contacto")
            nombre = input("Ingrese el nombre del contacto: ").strip()
            if nombre in contactos:
                return print(f"El contacto con nombre {nombre} ya existe!")

            while True:
                telefono = input("Ingrese el teléfono del contacto: ")
                try:
                    telefono = verificar_tel(telefono)  # aquí puede hacer raise
                    break
                except ValueError as e:
                    print(e)

            contactos.update({nombre: telefono})
            return print(f"Contacto {nombre} insertado")

        case 3:
            print("3. Actualizar contacto")
            nombre = input("Ingrese el nombre del contacto que desea actualizar: ").strip()
            if nombre not in contactos:
                return print(f"El contacto con nombre {nombre} no existe!")

            while True:
                numero = input(f"Ingrese el numero del contacto {nombre} que desea actualizar: ")
                try:
                    numero = verificar_tel(numero)  # aquí puede hacer raise
                    break
                except ValueError as e:
                    print(e)

            contactos.update({nombre: numero})
            return print(f"El contacto con nombre {nombre} se actualizo!")

        case 4:
            print("4. Eliminar contacto")
            nombre = input("Ingrese el nombre del contacto: ").strip()
            if nombre in contactos:
                contactos.pop(nombre)
                return print(f"El contacto con nombre {nombre} se elimino!")
            return print(f"El contacto con nombre {nombre} no existe!")

        case 0:
            return "0. Finalizar programa"

        case _:
            return "Digite un número valido"


n = 1

while n != 0:
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("0. Finalizar programa")

    n = input("Ingrese el número de la operación que quiere realizar: ")
    try:
        n = int(n)
    except ValueError:
        print("Debe ingresar un número valido")
    else:
        print(agenda(n))




