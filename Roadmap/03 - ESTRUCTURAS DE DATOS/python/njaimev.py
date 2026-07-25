# Una estructura de dato es un "contenedor" que permite organizar, almacenar y manipular datos de manera eficiente.
# Tenemos las listas, tuplas, conjuntos, diccionaros, también pilas y colas en collections.
# Esto nos ayuda a organizar datos para optimizar la eficiencia y rendimiento.
# Reduce la complejidad en la manipulación de grande volúmenes de información.
# Facilita el acceso, búsqueda y modificación de los datos de manera efectiva.

# LISTAS (list)
# Almacena colecciones de elementos ordenados y modificables, puede ser cualquier tipo de dato.

mi_lista = [1, 35, "Gato", 7.25, True]
mi_lista2 = [1, 47, 23, 78, 12]

mi_lista.append("Edificio")                   #Inserta al final
mi_lista.pop()                                #Elimina el último elemento
mi_lista.insert(2, "Perro")                   #Inserta en una posición específica
mi_lista[4] = 15                              #Actualiza el dato en un índice específico
mi_lista[1:3] = [20, 40]                      #Reemplaza una porción
mi_lista2.sort()                              #Ordena en su lugar menor a mayor
nueva_lista = sorted(mi_lista2, reverse=True) #Crea una nueva lista ordenada mayor a menor

print(mi_lista)
print(mi_lista2)

# TUPLAS (tuple)
# Son como las listas, pero INMUTABLES (no pueden modificarse).
# Util para datos que no deben cambiar.

mi_tupla = (10, 70, 20, 50)
mi_tupla = tuple(sorted(mi_tupla))  #Ordena la tupla, pero convirtiendola en otra lista, al decirle tuple, vuelve a convertirla en tupla

print(mi_tupla)


# CONJUNTOS (set)
# Colección NO ordenada de elementos únicos (no hay duplicados).
# Utiles para operaciones de conjuntos como unión, intersección y diferencia.

mi_conjunto = {1, 8, 15, 3, 14, 15}
mi_conjunto.add(4)          #Inserta al final
mi_conjunto.add(3)          #No se inserta porque es duplicado
mi_conjunto.remove(3)       #Elimina el valor nombrado
mi_conjunto.discard(5)      #Elimina el valor nombrado, no da error si no existe
mi_conjunto.pop()           #Elimina un elemento aleatorio
lista_ordenada = sorted(mi_conjunto) #Ordena, pero convertido en lista, NO SE PUEDE ORDENAR UN SET

print(mi_conjunto)
print(lista_ordenada)

# DICCIONARIOS (dict)
# Almacena pares clave-valor, donde la clave es única y se asocia a un valor.
# Permite acceso rápido a los datos mediante la clave.

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Santiago"}
mi_diccionario["comuna"] = "Las Condes"                     #Inserta una nueva clave-valor
mi_diccionario.pop("edad")                                  #Elimina la clave mencionada
mi_diccionario.popitem()                                    #Elimina un elemento aleatorio
mi_diccionario.clear()                                      #Elimina todos los elementos
mi_diccionario["nombre"] = "Matías"                         #Actualiza el valor de la clave mencionada
mi_diccionario.update({"ciudad": "Arica", "pais": "Chile"}) #Actualiza y/o agrega datos

print(mi_diccionario)

#En diccionarios se ordena por: claves, valores o pares clave-valor

claves_ordenadas = sorted(mi_diccionario.keys())                      #Ordena las claves por orden alfabético
valores_ordenados = sorted(mi_diccionario.values())                   #Ordena los valores por orden alfabetico o menor a mayor
items_ordenados = sorted(mi_diccionario.items(), key=lambda x: x[1])  #Ordena pares clave-valor según el valor

print(claves_ordenadas)
print(valores_ordenados)
print(items_ordenados)


"""
DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""


def contactos():

    agenda = {}

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("Seleccione una opción del 1 al 5: ")

        match option:
            
            case "1":
                nombre = input("Nombre a buscar: ")
                if nombre in agenda:
                    print(f"El número de {nombre} es {agenda[nombre]}.")
                else:
                    print(f"El contacto {nombre} no existe.")

            case "2":
                nombre = input("Nombre: ")
                numero = input("Número: ")
                if numero.isdigit() and len(numero) > 0 and len(numero) <= 11:
                    agenda[nombre] = numero
                    print("Contacto agregado exitosamente.")
                else:
                    print("Introduce un numero válido (Máx. 11 dígitos)")

            case "3":
                nombre = input("Nombre del contacto a actualizar: ")
                if nombre in agenda:
                    numero = input("Nuevo número: ")
                    if numero.isdigit() and len(numero) > 0 and len(numero) <= 11:
                        agenda[nombre] = numero
                        print("Contacto actualizado.")
                    else:
                        print("Introduce un numero válido (Máx. 11 dígitos)")

                else:
                    print("Contacto {nombre} no existe.")

                
            case "4":
                nombre = input("Nombre de contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print("Contacto eliminado.")
                else:
                    print("Contacto {nombre} no existe.")

            case "5":
                print("Saliendo")
                break
            case _:
                print("Opción inválida, seleccione una opción  del 1 al 5.")

contactos()
