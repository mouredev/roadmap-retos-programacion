# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# Estructuras de datos en Python: (listas, sets, tuplas, dicts)
# lists
lista_nueva = [20, True, "Soy Una Lista", "Este es elemento 4", 100]
print(lista_nueva)
# sets
conjunto_nuevo = {True, False, "No existen los elementos repetidos en un set", 40}
print(conjunto_nuevo)
# tuplas
tupla_nueva = (True,False,"Chau","Los elementos de una tupla deben ser inmutables", 300)
print(tupla_nueva)
# dicts
diccionario_nuevo = {"nombre": "Alvaro", "tipo de estructura": "Diccionario", "importante": True, "elementos": 4}
print(diccionario_nuevo)

# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
# -- lists:
## Insercion
lista_ejemplo = [20, 30, 40, 50]
# Anadiendo un elemento en especifico de la lista usando .append()
lista_ejemplo.append(True)
print(f"Esta es la lista con un elemento anadido usando .append(): {lista_ejemplo}")
# Anadiendo un elemento especificando el indice en donde va a estar usando .insert():
lista_ejemplo.insert(2, 3)
print(f"Esta es la lista con un elemento anadido en el indice especificado usando .insert(): {lista_ejemplo}")
# Anadiendo muchos elementos a la vez:
lista_ejemplo.extend([200, "Hola", "Mundo", False])
print(f"He anadido muchos elementos a la lista usando .extend(): {lista_ejemplo}")

## Borrado
# Eliminando el elemento del indice 3
lista_ejemplo.pop(3)
print(f"Eliminando un elemento de la lista especificando su indice usando .pop(): {lista_ejemplo}")
# Eliminando un elemento de la lista usando remove
lista_ejemplo.remove(20)
print(f"Eliminando un elemento en especifico de la lista usando .remove(): {lista_ejemplo}")
# Vaciando todos los elementos de una lista:
lista_ejemplo.clear()
print(f"Vaciando la lista con .clear(): {lista_ejemplo}")

## Actualizacion
# Invertir el orden de los elementos de la lista:
otra_lista_ejemplo = [30, 1, 2, 3, 4, 210, 30, 47]
otra_lista_ejemplo.reverse()
print(f"He revertido el orden de los elementos de esta lista usando .reverse(): {otra_lista_ejemplo}")

## Ordenacion 
# Ordenar los elementos numericos de una lista de manera predeterminada (ASC)
lista_numerica = [300, 1000, 40, 2, 6, 100, 98]
lista_numerica.sort()
print(f"Esta es la lista de numeros ordenados ASCENDENTEMENTE: {lista_numerica}")
# Ordenar los elementos numericos de la lista de manera DESC
otra_lista_numerica = [300, 20, 500, 1000, 8, 10, 1, 2]
otra_lista_numerica.sort(reverse=True)
print(f"Esta es otra lista de numeros ordenadas inversamente: {otra_lista_numerica}")

# -- tuplas:
## Los elementos de una tupla son inmutables es decir que no se pueden modificar por lo tanto, no podremos anadir, actualizar ni eliminar elementos.

# -- diccionarios:
## Anadir:
ejemplo_dict = {
    "nombre": "Luke",
    "edad": 1.6,
    "actividades": ["Jugar", "Comer", "Amar"],
}
### Especificando con indice, no podremos anadir una clave para el indice en este caso:
ejemplo_dict[3] = True
print(f"Hemos anadido un elemento en un diccionario especificando su indice: {ejemplo_dict}")
### Si la clave no existe podemos anadirla con su nuevo valor:
ejemplo_dict["es perro?"] = True
print(f"Hemos anadido clave y valor especificando su clave y su valor: {ejemplo_dict}")
### Anadir varios clave y valor usando .update():
ejemplo_dict.update({"clave 5": "valor 5", "clave 6": "valor 6"})
print(f"Hemos anadido varios clave y valor en el diccionario usando el metodo .update(): {ejemplo_dict}")
### Anadir varios clave y valor usando .setdefault() si la clave no existe:
ejemplo_dict.setdefault("nueva_clave", "nuevo_valor")
print(f"Hemos anadido un nuevo valor especificando su clave usando .setdefault(): {ejemplo_dict}")

## Actualizar:
### Usando la notacion de corchetes especificando una clave:
ejemplo_dict["clave 5"] = 5
print(f"He actualizado el valor de una clave usando la notacion de corchetes: {ejemplo_dict}")
### Usando el metodo .update():
ejemplo_dict.update({"clave 5": 50, "clave 6": "Elemento 6"})
print(f"He actualizado los valores de las claves de un diccionario usando .update(): {ejemplo_dict}")

## Eliminar:
### eliminando un valor y clave de un diccionario usando `del`:
del ejemplo_dict["clave 5"]
print(f"He eliminado la clave y valor de la clave 5 usando la palabra reservada de Python `del`: {ejemplo_dict}")
### Usando el metodo .pop():
### - Especificando su clave:
ejemplo_dict.pop("clave 6")
print(f"He eliminado la clave y el valor de la clave 6 usando .pop(): {ejemplo_dict}")
### Usando el metodo .popitem():
ultimo_elemento_del_dict = ejemplo_dict.popitem()
print(f"He eliminado el ultimo elemento del diccionario usando .popitem(): {ejemplo_dict}")
### Eliminando todos los elementos del diccionario:
ejemplo_dict.clear()
print(f"He eliminando todos los elementos del diccionario usando .clear(): {ejemplo_dict}")

## - sets:
nuevo_conjunto = {1, 2, 3}
print(f"Este es el conjunto inicial: {nuevo_conjunto}")
### Anadir elementos:
## Anadir un solo elemento usando .add():
nuevo_conjunto.add(4)
print(f"Anadiendo un nuevo elemento al conjunto usando .add(): {nuevo_conjunto}")
## Anadir varios elementos usando .update():
nuevo_conjunto.update({4,5,6})
print(f"Anadiendo elementos a un conjunto usando el metodo .update (no puede haber elementos repetidos): {nuevo_conjunto}")
## .union()
conjunto_a_anadir = {7,8,9}
nuevo_conjunto = nuevo_conjunto.union(conjunto_a_anadir)
print(f"He anadido un nuevo conjunto al conjunto principal usando .union(): {nuevo_conjunto}")
### Eliminar elementos:
## Usando .remove():
nuevo_conjunto.remove(3)
print(f"Eliminando un elemento del conjunto especificando el elemento: {nuevo_conjunto}")
## Usando .discard():
nuevo_conjunto.discard(4)
print(f"Eliminando un elemento usando .discard(): {nuevo_conjunto}")
## Usando .pop():
nuevo_conjunto.pop()
print(f"Eliminando el ultimo elemento del conjunto usando .pop(): {nuevo_conjunto}")
### Actualizar elementos:
## Para actualizar un elemento de un conjunto, debemos primero eliminar ese elemento y luego anadirlo (no se puede actualizar en una posicion en especifico)
## Primero eliminamos:
nuevo_conjunto.remove(5)
print(f"Eliminando el elemento 5: {nuevo_conjunto}")
## .update()
nuevo_conjunto.update({5})
print(f"El elemento 5 se elimino y luego se anadio: {nuevo_conjunto}")

# DIFICULTAD EXTRA (opcional):
contactos = []

# Creando una funcion para verificar si existe un contacto duplicado
def contacto_duplicado(nombre):
    global contactos
    for contacto in contactos:
        if contacto['nombre'] == nombre:
            return True
    return False

# Creando una funcion para anadir un contacto a la lista de contactos
def anadir_contacto(nombre, numero):
    # Verificando si el contacto ya existe en la lista:
    if not contacto_duplicado(nombre):
        # Verificando si el numero tiene solo digitos numericos y si tiene 11 digitos como maximo
        try:
            numero = int(numero)
        except:
            print(f"El numero tiene que tener solo digitos numericos")
            return
        else:
            numero = str(numero)
            if len(numero) > 11:
                print("El numero de contacto debe tener 11 digitos como maximo")
                return
            tieneDigitos = numero.isnumeric()
            # Si todo esta bien anadelo a la lista de contactos
            if (tieneDigitos == True):
                global contactos
                contactos.append({
                    "nombre": nombre,
                    "numero": numero
                })
            return contactos
    else:
        print(f"El contacto ya existe no puede haber duplicados")
        return

# Funcion para buscar contacto existente
def buscar_contacto(nombre_del_contacto):
    global contactos
    # Verificando si el contacto no existe. Si existe imprime en consola el contacto
    for contacto in contactos:
        if contacto['nombre'] == nombre_del_contacto:
            print(contacto)
            return
    print("No hemos encontrado el contacto")
    return

# Funcion que actualiza el contacto existente:
def actualizar_contacto(nombre_del_contacto, valor):
    try:
        valor = int(valor)
    except:
        print(f"El numero tiene que tener solo digitos numericos")
        return
    else:
        valor = str(valor)
        if len(valor) > 11:
            print("El numero de contacto debe tener 11 digitos como maximo")
            return
        global contactos
        for contacto in contactos:
            if contacto["nombre"] == nombre_del_contacto:
                contacto["numero"] = valor
                return {"Message": "Contacto actualizado", contacto["nombre"] : contacto["numero"]}
        print("No hemos encontrado el contacto")
        return

# Funcion que elimina el contacto
def eliminar_contacto(nombre_del_contacto):
    try:
        global contactos
        for contacto in contactos:
            if contacto["nombre"] == nombre_del_contacto:
                contactos.remove(contacto)
                print("Contacto Eliminado")
                return contactos
        print("No hemos encontrado el contacto a eliminar")
        return
    except Exception as Error:
        print(f"Cometiste el siguiente error: {Error}")

# Funcion que nos permite ver los contactos
def ver_contactos():
    global contactos
    print(contactos)


while(True):
    actividad = input("Que deseas hacer con tu lista de contactos? (Ver, Anadir, Actualizar, Buscar y Eliminar) o escribe 'cancelar' para detener el programa: ").lower()
    if actividad == "ver":
        ver_contactos()
    elif actividad == "anadir":
        nombre_del_contacto = input("Cual es el nombre de tu contacto que deseas anadir?: ").lower()
        numero_del_contacto = input("Cual es el numero de tu contacto que deseas anadir?: ")
        anadir_contacto(nombre_del_contacto, numero_del_contacto)
    elif actividad == "actualizar":
        nombre_del_contacto = input("Cual es el nombre de contacto que deseas actualizar?: ").lower()
        numero_del_contacto = input("Cual es el numero nuevo para actualizar el contacto?: ")
        actualizar_contacto(nombre_del_contacto, numero_del_contacto)
    elif actividad == "buscar":
        nombre_del_contacto = input("Que contacto deseas buscar? (poner nombre del contacto): ").lower()
        buscar_contacto(nombre_del_contacto)
    elif actividad == "eliminar":
        nombre_del_contacto = input("Que contacto deseas eliminar?: ").lower()
        eliminar_contacto(nombre_del_contacto)
    elif actividad == "cancelar":
        break