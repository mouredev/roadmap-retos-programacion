# Ejemplos de la Estructuras de Datos en Python

"""
Listas: Una lista es una colección ordenada y modificable de elementos. 
Puedes acceder a los elementos de una lista mediante índices.
"""
from array import array
lista = [1, 2, 3, 4, 'cinco', 'seis', 'siete', 8.1, 9.0, 'a', 'b']


""" 
Tuplas: Similar a las listas, pero son inmutables, es decir, 
no pueden ser modificadas una vez creadas.
"""
tupla = (1, 2, 3, 'cuatro', 5.0)


"""
Conjuntos (Sets): Un conjunto es una colección no ordenada
de elementos únicos. Se utilizan para realizar operaciones 
de conjunto como unión, intersección, diferencia, etc
"""
conjunto = {1, 2, 3, 3, 4, 5, 6}


"""
Diccionarios: Un diccionario es una colección no ordenada de pares clave-valor. 
Se accede a los valores a través de las claves.
"""
diccionario = {"clave1": "Valor1", "numero": 2, "lista": [1, 2, 3]}


"""
Cadenas (Strings): No es una estructura de control como tal pero son utilizadas 
para representar texto y son inmutables
"""
cadena = "Esto es una cadena de texto"


"""
Colas y Pilas: Estas estructuras pueden implementarse utilizando listas. 
Las listas pueden actuar como: colas (FIFO - First In, First Out) 
y pilas (LIFO - Last In, First Out).
"""
# Cola
cola = [1, 2, 3]
cola.append(4)  # agrega al final
elemento = cola.pop(0)  # Elimina del principio

# pila
pila = [1, 2, 3]
pila.append(4)  # apgrea al final
pila.pop()  # Elimina del final

"""
Arrays Similar a las listas, pero más eficientes para almacenar
elementos del mismo tipo. Requieren la importación del módulo array.
"""

mi_array = array('i', [1, 2, 3])

# Dificultad Extra
agenda = {
    "Aldo": 3112343566
}
# Buscar Contactos


def search(name):
    if name in agenda:
        return name, agenda[name]
    return "No existe"

# Insertar


def instert(name, phone):
    agenda[name] = phone

# Actualizar


def update(name, phone):
    agenda[name] = phone

# Borrar


def delete(name):
    agenda.pop(name)


# Mostrar
def show():
    for name, phone in agenda.items():
        print(name, ":", phone)


while True:
    print("""
            Operación que desea
            1.- Buscar
            2.- Insertar
            3.- Actualizar
            4.- Eliminar
            5.- Mostrar 
            6.- Salir
          """)
    ctrl = True
    opc = input()
    match opc:
        case "1":
            name = input("Introduzca el nombre del contacto: \n").capitalize()
            print(search(name))
        case "2":
            while ctrl:
                name = input("Introduzca nombre del contacto: ").capitalize()
                phone = input("Introduzca número: ")
                if len(phone) < 5 or len(phone) > 10 or not phone.isdigit():
                    print("Número incorrecto, intenta de nuevo")
                else:
                    instert(name, phone)
                    ctrl = False
        case "3":
            name = input(
                "Introduzca el nombre del contacto que quiera actualizar: ").capitalize()
            if name in agenda:
                phone = input("Introduzca el nuevo telefono: ")
                update(name, phone)
            else:
                print("Usuario no encontrado")
        case "4":
            name = input(
                "Introduzca el nombre del contacto que quiera eliminar: ").capitalize()
            if name in agenda:
                delete(name)
            else:
                print("usuario no existe")
        case "5":
            show()
        case "6":
            print("Salio del programa")
            break
        case _:
            print("Selecciona una opción valida")
