#Listas
print("-----------Seccion de lista-------------")
print("list is a collection which is ordered and changeable. allows duplicates members")
my_list = [100,22,13,4,5]
#añadir
my_list.append("Hola")#se añade de ultimo
my_list.insert(0, 20)
print(my_list)
#remover
my_list.remove(20) #remueve la primera ocurrencia del elemento y si no esta devuele una excepcion
my_list.pop()#remueve un elemento y te devuelve su index, por default remueve el ultimo
print(my_list)
#ordenar
my_list.sort()# se puede pasar el parametro "reverse" con un valor booleano, solo funciona con INT
print(my_list)

print("-----------Seccion de tupla-------------")
print("is a collection which is ordered and unchangeable. allows duplicate member")
#las tuplas son inmutables por lo que no se pueden modificar
my_tuple = (12,1,4,50,24)
print(f"{my_tuple} las tuplas son inmutables")
#obtener la primera ocurrencia de un valor y devolver el index
my_tuple.index(4)

print("-----------Seccion de Set-------------")
print("is a collection which is unordered and unchangeable. dont allow duplicate member")
my_set = {10,2,30,5,40,5}

#añadir
my_set.add(1034)


#update uniendo otro iterable
my_set.update({100,200,300})
print(my_set)

#remover
my_set.remove(5)
print(f"This is my set without 5: {my_set}")

#limpiar todo el set
my_set.clear()
print(my_set)

print("-----------Seccion de Diccionario-------------")
print("is a collection which is ordered** and and changeable. dont allows")

my_dict = {
    "Nombre": "Hendry",
    "Edad": 23,
    "¿Casado?": True
}
print(my_dict)
#añadir un objeto al diccionario
print("Añadiendo")
my_dict["lenguajes de programacion"] = ["Python", "Javascript", "React", "HTML", "Css", "Django", "Postgress"]
print(my_dict)

#actualizar un objeto
my_dict.update({"Nombre": "Alberto"})
print(my_dict)

#obtener un objeto
r = my_dict.get("lenguajes de programacion")
print(r)
r2 = my_dict["lenguajes de programacion"]
print(r2)

#removin an iten
del my_dict["Edad"]
print(my_dict)

my_dict.pop("¿Casado?")
print(my_dict)

print("-----------------Ejercicio---------------------")

from time import sleep

contactos = {}

def mostrar_bienvenida():
    print("""
    Hola! Bienvenido a tu agenda personal de contacto. ¿En qué te puedo ayudar?
    
    1 - Buscar contacto.
    2 - Guardar un contacto.
    3 - Actualizar un contacto.
    4 - Eliminar un contacto.
    5 - Mostrar todos los contactos
    6 - Cerrar la agenda.
    """)

def buscar_contacto():
    nombre = input("Introduce el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"Contacto encontrado: {nombre}, Teléfono: {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

def guardar_contacto():
    nombre = input("Introduce el nombre del contacto a guardar: ")
    telefono = input("Introduce el número de teléfono a guardar: ")
    
    if not nombre or not isinstance(nombre, str):
        print("Por favor ingrese un nombre válido.")
        return
    
    if not telefono.isdigit() or len(telefono) != 11:
        print("Ingrese un teléfono válido (debe tener exactamente 11 dígitos).")
        return
    
    print(f"Guardando en la agenda a {nombre} con el siguiente número de teléfono: {telefono}")
    contactos[nombre] = telefono
    sleep(2)
    print("¡Guardado con éxito!")

def actualizar_contacto():
    nombre = input("Introduce el nombre del contacto a actualizar: ")
    if nombre in contactos:
        nuevo_telefono = input("Introduce el nuevo número de teléfono: ")
        if nuevo_telefono.isdigit() and len(nuevo_telefono) == 11:
            contactos[nombre] = nuevo_telefono
            print("Contacto actualizado con éxito.")
        else:
            print("Número de teléfono no válido.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado con éxito.")
    else:
        print("Contacto no encontrado.")

def cerrar_agenda():
    print("Finalizando programa...")
    sleep(2)
    print("¡Hasta luego!")
    return False

def mostrar_contactos():
    print("-----Lista de contactos-----")
    for nombre, telefono in contactos.items():
        print(f"Nombre: {nombre}")
        print(f"Telefono: {telefono}")

options = {
    1: buscar_contacto,
    2: guardar_contacto,
    3: actualizar_contacto,
    4: eliminar_contacto,
    5: mostrar_contactos,
    6: cerrar_agenda
}

if __name__ == "__main__":
    while True:
        mostrar_bienvenida()
        try:
            seleccion_usuario = int(input("Selecciona el número de tu operación, por favor: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        
        funcion_seleccionada = options.get(seleccion_usuario)

        if funcion_seleccionada:
            
            resultado = funcion_seleccionada()
            if resultado == False:  
                break
        else:
            print("Por favor, selecciona un número válido entre el 1 y el 6.")