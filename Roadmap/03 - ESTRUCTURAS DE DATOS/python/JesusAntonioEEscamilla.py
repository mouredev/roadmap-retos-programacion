# #03 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
#---LISTA---
# Creando Lista
print("LISTA")
lista = ["Antonio", "Fatima", "Maria", "Lizette"]
print(lista)
# INSERCIÓN
print("INSERCIÓN")
lista.append("Rosa")
print(lista)
# ELIMINACIÓN
print("ELIMINACIÓN")
del lista[2]
print(lista)
# ACTUALIZACIÓN
print("ACTUALIZACIÓN")
lista[0] = "Jesus"
print(lista)
# ORDENAMIENTO
print("ORDENAMIENTO")
lista.sort()
print(lista)


#---DIRECTORIO---
# Creando Directorio
print("DIRECTORIO")
diccionario = {
    "Papas": 3,
    "Tortas": 5,
    "Queso": 2,
    "Pan": 1,
}
print(diccionario)
# INSERCIÓN
print("INSERCIÓN")
diccionario["Pepsi"] = 4
print(diccionario)
# ELIMINACIÓN
print("ELIMINACIÓN")
del diccionario["Papas"]
print(diccionario)
# ACTUALIZACIÓN
print("ACTUALIZACIÓN")
diccionario["Tortas"] = 6
print(diccionario)
# ORDENAMIENTO
print("ORDENAMIENTO")
mi_dicc = dict(sorted(diccionario.items()))
print(mi_dicc)


#---SETS---
# Creando Set
print("SET")
conjunto = {"A", "B", "C"}
print(conjunto)
# INSERCIÓN
print("INSERCIÓN")
conjunto.add("D")
print(conjunto)
# ELIMINACIÓN
print("ELIMINACIÓN")
conjunto.remove("B")
print(conjunto)
# ACTUALIZACIÓN
print("ACTUALIZACIÓN")
print("No se puede eliminar directamente pero hay otra forma")
conjunto.remove("C")
conjunto.add("E")
print(conjunto)
# ORDENAMIENTO
print("ORDENAMIENTO")
print("No Existe una forma de ordenamiento")



"""
EXTRA
"""
def mostrar_menu():
    print('\nAgenda de Contactos')
    print('1. Insertar Contacto')
    print('2. Buscar Contacto')
    print('3. Actualizar Contacto')
    print('4. Eliminar Contacto')
    print('5. Mostrar Contacto')
    print('6. Salir')

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) <= 11

def insertar_contacto(agenda):
    nombre = input('Ingrese el nombre del contacto: ')
    telefono = input('Ingrese el teléfono del contacto: ')
    if validar_telefono(telefono):
        agenda[nombre] = telefono
        print(f'Contacto {nombre} añadido con éxito')
    else:
        print('Numero de telefono no valido. Debe ser numérico y tener un máximo de 10 dígitos')

def buscar_contacto(agenda):
    nombre = input('Ingrese el numero de contacto a buscar: ')
    if nombre in agenda:
        print(f'Nombre: {nombre}, Teléfono: {agenda[nombre]}')
    else:
        print('No se encontró el contacto')

def actualizar_contacto(agenda):
    nombre = input('Ingrese el numero de contacto a actualizar: ')
    if nombre in agenda:
        nuevo_contacto = input('Ingrese el nuevo numero de teléfono: ')
        if validar_telefono(nuevo_contacto):
            agenda[nombre] = nuevo_contacto
            print(f'Contacto {nombre} actualizado con éxito')
        else:
            print('Numero de telefono no valido. Debe ser numérico y tener un máximo de 10 dígitos')
    else:
        print('Contacto no encontrado')

def eliminar_contacto(agenda):
    nombre = input('Ingrese el numero de contacto a eliminar: ')
    if nombre in agenda:
        del agenda[nombre]
        print(f'Contacto {nombre} eliminado con éxito')
    else:
        print('No se encontró el contacto')

def mostrar_todos_contactos(agenda):
    if agenda:
        for nombre, telefono in agenda.items():
            print(f'Nombre: {nombre}, Teléfono: {telefono}')
    else:
        print('No hay contactos en la agenda')

def main():
    agenda = {}
    while True:
        mostrar_menu()
        option = input('Seleccione una Opción: ')
        
        if option == '1':
            insertar_contacto(agenda)
        elif option == '2':
            buscar_contacto(agenda)
        elif option == '3':
            actualizar_contacto(agenda)
        elif option == '4':
            eliminar_contacto(agenda)
        elif option == '5':
            mostrar_todos_contactos(agenda)
        elif option == '6':
            print('Saliendo del Programa...')
            break
        else:
            print('Opción no valida. Intente de nuevo')
main()