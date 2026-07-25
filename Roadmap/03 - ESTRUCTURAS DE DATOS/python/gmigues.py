"""
#03
ESTRUCTURAS DE DATOS
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
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
 */
"""

### LISTAS ### 
lista = [1, 2,2,2,3, 4, 5, 6]
print(type(lista))

#Agregar elementos
lista.append('E')
lista.extend(['A', '@'])
print(lista)

#Eliminar elementos
lista.remove('A')
print(lista)

#Seleccionar items
print(lista[0])

print("-----------------------------")

### TUPLAS ###
mi_tupla = (1,2,2,2,2,3,4,5)
print(type(mi_tupla))

#Seleccionar items
print(mi_tupla[1])

#Contar cuantas veces aparece un elemento
print(mi_tupla.count(2))



print("-----------------------------")

# DICCIONARIOS

# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(mi_diccionario)

# Acceder a valores
print(mi_diccionario["nombre"])  

# Agregar un nuevo par clave-valor
mi_diccionario["profesión"] = "Ingeniero"

# Actualizar un valor existente
mi_diccionario["edad"] = 31

# Eliminar un par clave-valor
del mi_diccionario["ciudad"]


print(mi_diccionario)  


print("-----------------------------")

# SETS

# Crear conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Operaciones
print(type(conjunto_a))
print("Inserción", conjunto_b.add(6))
print("Eliminación", conjunto_b.remove(6))
print("Unión:", conjunto_a | conjunto_b)  # Unión
print("Intersección:", conjunto_a & conjunto_b)  # Intersección
print("Diferencia:", conjunto_a - conjunto_b)  # Diferencia
print("Diferencia simétrica:", conjunto_a ^ conjunto_b)  # Diferencia simétrica



print("-----------------------------")


### AGENDA ###

print('---BIENVENIDO A LA AGENDA ---')
agenda = {
    "Pepe": 12345678,
    "Maria": 87654321
}
operacion =""
while operacion != "5":
    operacion = input('''
                      

                ---------------------------    
                Que Operación desea hacer:
                ---------------------------

                1- Busqueda de contacto
                2- Actualizacion de contacto
                3- Ingresar nuevo contacto
                4- Eliminacion de contacto
                5- Salir
                ''')

    if operacion == "1":
        usuario = input('Ingrese el nombre del usuario: ')
        if usuario in agenda:
            print((f"Usuario {usuario}, Telefono:", agenda[usuario]))
        else:
            print("El usuario ingresado no existe en la agenda.")
            continue
    elif operacion == "2":
        usuario = input("Que usuario desea modificar?: ")
        if usuario in agenda:
            nuevo_numero = input(f'Ingrese el nuevo numero de telefono para el usuario {usuario}: ')
            if len(nuevo_numero) == 8 and nuevo_numero.isdigit():
                nuevo_numero = int(nuevo_numero)
                agenda[usuario] = nuevo_numero
                print(f"Se ha actualizado correctamente los datos del usuario {usuario}")
            else:
                print("Numero ingresado no es valido")
        else:
            print('El usuario ingresado no existe en la agenda')
    elif operacion == "3":
        nuevo_usuario = input('Ingrese el nombre del nuevo usuario: ')
        nu_tel = input("Ingrese el telefono: ")
        if len(nu_tel) == 8 and nu_tel.isdigit():
            nu_tel = int(nu_tel)
            agenda[nuevo_usuario] = nu_tel
            print(f'Se ha agregado correctamente el usuario {nuevo_usuario} a la agenda')
        else:
            print('Los datos ingresados no son correctos')
            continue
    elif operacion == "4":
        del_user = input("Ingrese el usuario que desea eliminar: ")
        if del_user in agenda:
            del agenda[del_user]
            print(f'El usuario {del_user} ha sido eliminado de la agenda.')
        else:
            print('El usuario ingresado no se encuentra en la agenda')
            continue
    elif operacion == "5":
        break
    else:
        print('La opcion igresada no es correcta.')
