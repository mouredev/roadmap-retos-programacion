"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""
# Listas 
my_list = ["pera","uva","manzana", 1, 2, 3, False, True]
print(type(my_list))
print(my_list)

#! Accedder a los elementos
print(my_list[0]) # pera
print(my_list[-1]) # True
print(my_list[1:3]) # ['uva', 'manzana']
print(my_list[-5:]) # [1, 2, 3, False, True]

### Verificar si un elemento está en la lista
if "uva" in my_list:
    print("La uva está en la lista")

#! Modificar elementos
my_list[1:3] = "piña", "limon" # Reemplaza uva Y manzana
print(my_list)

#! Agregar Elementos
#* Agregar un elemento
my_list.insert(1,"sandia")
my_list.append("elemento agregado al final")
print(my_list)

#* Agregar una lista a otra lista
my_other_list = ["rosas", "girasoles"]
my_list.extend(my_other_list)
print(my_list)

#! Eliminar elementos
#* Eliminar un elemento usano el elemento
my_list.remove("elemento agregado al final")

#* Eliminar un elemento usando el índice
my_list.pop(8)
del my_list[7]
print(my_list)

#* Eliminar todos los elemmentos de la lista
my_list.clear()
print(my_list)

#! Ordenar Listas
lista_numeros = [6, 1, 5, 3, 4, 2]
print(lista_numeros)

lista_frutas = ["pera","uva","manzana", "limon", "sandia"]
print(lista_frutas)

#* Orenar numericos
lista_numeros.sort()
print(lista_numeros)

#* Ordenar numericos inversamente
lista_numeros.sort(reverse=True)
print(lista_numeros)

#* Ordenar Alfabéticamente
lista_frutas.sort()
print(lista_frutas)

#* Ordenar Alfabéticamente inversamente
lista_frutas.sort(reverse=True)
print(lista_frutas)

#* Ordenar por otros criterios (longitud)
lista_frutas.sort(key = lambda x: len(x))
print(lista_frutas)

# Tuplas
tupla_animales = ("perro", "gato", "raton")
print(type(tupla_animales))
print(tupla_animales)

### Acceder a elementos
print(tupla_animales[0]) # perro
print(tupla_animales[-1]) # raton
print(tupla_animales[:2]) # ('perro', 'gato')
print(tupla_animales[-2:]) # ('gato', 'raton')

#! Verificar si existe un dato en una tupla
if "perro" in tupla_animales:
    print("El perro está en la tupla")

#! Modificar tuplas
"""
Las tuplas son inmutables, por lo que no se pueden modificar,
pero si se pueden copiar a iterable (como las listas), modificar y reasignar
! Esto se puede aplicar para 
* modificar un elemmento
* eliminar elemmentos
* agregar elemmentos
* concatenar tuplas
"""
# Sets
set_mezclado = {"cebolla", "tomate", "ajo", 1, 2, 3, False, True}
print(type(set_mezclado))
print(set_mezclado)

#! Acceder a elementos
"""
No se puede acceder a elementos de un set por índice o llave
aunque se puede verificar si un elemento se encuentra entro de un set o no
"""

if "tomate" in set_mezclado:
    print("El tomate está en el set")
    
#! Agregar elementos
#* Agregar un elemento
set_mezclado.add("papa")
print(set_mezclado)

#* Agregar varios elementos
especias = {"oregano", "comino", "paprika"}
set_mezclado.update(especias) #Tambien funciona .union()
print(set_mezclado)

#! Eliminar elementos
set_mezclado.remove(True)
set_mezclado.pop() #Pop no perite indice, elimina el primer elemento
print(set_mezclado)

set_mezclado.clear()
print(set_mezclado)

# Diccionarios
diccionario_ingredientes = {
    "tomate":{
        "cantidad": 2,
        "categoria": "verdura",
        "color": "rojo",
    },
    "papa":{
        "cantidad": 1,
        "categoria": "verdura",
        "color": "amarillo",
    },
    "coco":{
        "cantidad": 3,
        "categoria": "fruta",
        "color": "blanco",
    }
}
print(type(diccionario_ingredientes))
print(diccionario_ingredientes)

#! Acceder a elementos
print(diccionario_ingredientes["tomate"]) # {'cantidad': 2, 'categoria': 'verdura', 'color': 'rojo'}
print(diccionario_ingredientes["tomate"]["cantidad"]) # 2
element = diccionario_ingredientes.get("coco")
print(element) # {'cantidad': 3, 'categoria': 'fruta', 'color': 'blanco'}
print(element.keys()) # dict_keys(['cantidad', 'categoria', 'color'])
print(element.values()) # dict_values([3, 'fruta', 'blanco'])

#! Modificar elementos
element["cantidad"] = 4
print(element)

element.update({"cantidad": 5, "color": "cafe"})
print(element)

#! Agregar elementos
diccionario_ingredientes["cebolla"] = {
    "cantidad": 1,
    "categoria": "verdura",
    "color": "morado",
}
print(diccionario_ingredientes)

element.update({"sabor": "dulce"})
print(element)

#! Eliminar elementos
diccionario_ingredientes.pop("papa")
print(diccionario_ingredientes)

diccionario_ingredientes.popitem() #Elimina el último elemento
print(diccionario_ingredientes)

del diccionario_ingredientes["tomate"]
print(diccionario_ingredientes)

#! Vaciar Diccionario
element.clear() 
print(element)
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

agenda = {}
opciones = ("1", "2", "3", "4", "0")

def buscar_contacto(nombre:str):
    if nombre in agenda:
        return f"Nombre: {nombre}, Telefono: {agenda[nombre]}"
    return False

def agregar_contacto(nombre:str, telefono:int):
    if not buscar_contacto(nombre.lower()):
        agenda[nombre] = telefono
        return f"{nombre} agregado correctamente"
    return False

def modificar_contacto(nombre:str, telefono:int):
    if buscar_contacto(nombre):
        agenda[nombre] = telefono
        return f"{nombre} actualizado a {agenda[nombre]} "
    return False

def eliminar_contacto(nombre:str):
    if buscar_contacto(nombre):
        agenda.pop(1)
        return f"{nombre} eliminado"
    return False

def solicitarNombre():
    while True:
        nombre = input("Ingrese el nombre o 0 para salir: ")
        if nombre.isdigit():
            print(f"Nombre invalido {nombre}")
            continue
        elif nombre == "0":
            return False
        return nombre

def solicitarNumero():
    while True:
        telefono = input("Ingrese Telefono o 0 para salir: ")
        if telefono.isnumeric() and len(telefono) == 10:
            return telefono
        elif telefono == "0":
            return False
        print(f"Numero invalido: {telefono}")

def interfaz():
    print("Bienvenido a la agenta de contactos")
    
    # Ciclo infinito
    while True:
        # Mostrar opciones
        print(f"""
            Actualmente hay {len(agenda)} {"contacto" if len(agenda) < 2 else "contactos"}  en la agenda
            Inserte la opción deseada:
            1. Buscar contacto
            2. Agregar contacto
            3. Actualizar contacto
            4. Eliminar contacto
            0. Salir
            """)
        
        # Leer la opción y verifica si es válida
        entrada = input("Opción: ")
        if entrada not in opciones:
            print("Opción no válida")
            continue
        
        # Salir
        if entrada == "0":
            print("Gracias por usar la agenda, adios")
            break
        
        # Buscar contacto
        if entrada == "1":
            print("Buscar contacto")
            nombre = solicitarNombre()
            contacto = buscar_contacto(nombre)
            if contacto:
                print(contacto)
            else:
                print("Registro no encontrado")
        
        # Agregar contacto (Mexico, 10 Numeros)
        if entrada == "2":
            print("Agregar contacto")
            nombre = solicitarNombre()
            if nombre:
                telefono = solicitarNumero()
                if telefono:
                    print(agregar_contacto(nombre, telefono))
        
        # Actualizar contacto
        if entrada == "3":
            print("Actualizar contacto")
            nombre = solicitarNombre()
            if nombre:
                contacto = buscar_contacto(nombre)
                if not contacto:
                    print("Registro no encontrado")
                    continue
                print(contacto)
                telefono = solicitarNumero()
                if telefono:
                    print(modificar_contacto(nombre, telefono))
                    
        # Eliminar contacto
        if entrada == "4":
            print("Eliminar contacto")
            nombre = solicitarNombre()
            if nombre:
                contacto = buscar_contacto(nombre)
                if not contacto:
                    print("Registro no encontrado")
                    continue
                print(eliminar_contacto(nombre))

interfaz()