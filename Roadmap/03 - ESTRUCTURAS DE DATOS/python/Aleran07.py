# 03
# Estructuras soportadas por defecto en Python


### Estructuras de control

"""
Condicional if, elif and else
"""
x = 5
if x > 0:
    print("Mayor a cero")
elif x == 0:
    print("Cero")
else:
    print("menor a cero")

"""
Bubles
"""
# Bucles for
for i in range(5):
    print(i)

# Bucles while
while i > 0:
    print(i)
    i -=1

""""
Control de flujo de bucles
"""
# break, continue and pass

for i in range(11):
    if i == 3:
        continue # se salta el numero en cuestion
    elif i == 6:
        pass # no hace nada
    elif i == 9:
        break # rompe el bucle
    print(i)

"""
Manejo de errores
"""
try:
    print(10 / 0) # Error divicion por cero
except ZeroDivisionError:
    print("Error: división por cero") # Manejo de error para que permita ejecutar el codigo
finally:
    print("Esto siempre se ejecuta")

# Capturar cualquier error
try:
    num = int("hola")   # Error: no se puede convertir a int
except Exception as e:   # e guarda el error
    print("Ocurrió un error:", e)

# pruba sin error
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error: división por cero")
else: # else en si es una excepcion
    print("Todo salió bien:", x)


"""El bloque finally se ejecuta siempre, haya o no error.
Se usa mucho para cerrar archivos, conexiones, etc."""
try:
    f = open("archivo.txt")
    contenido = f.read()
except Exception as e:   # e guarda el error
    print("Ocurrió un error:", e)
finally:
    print("Se intentó abrir el archivo")


"""raise sirve para lanzar manualmente un error.
Esto es útil si quieres validar condiciones en tu programa."""

def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    return a / b

print(dividir(10, 2))  # Funciona
print(dividir(10, 0))  # Lanza ValueError


"""
Estrutura de datos
"""
# listas
numeros = [1, 2, 3, 4]
# insercion en listas
numeros.append(5) # agrega al final
numeros.insert(0, 1) # inserta 1 en posicion 0
# actualizar
numeros[4] = 7 # cambia el valor en indice 4
# eliminar
numeros = [1, 2, 3, 4]
numeros.remove(2)      # Elimina el valor 2
numeros.pop(0)         # Elimina el elemento en posición 0
del numeros[1]         # Elimina por índice
print(numeros)
# ordenar
numeros.append(5)
# numeros = [5, 2, 8, 1]
numeros.sort()           # Ordena de menor a mayor
print(numeros)           # [1, 2, 5, 8]
numeros.sort(reverse=True)  # Ordena de mayor a menor
print(numeros)              # [8, 5, 2, 1]

nueva_lista = sorted(numeros) # se puede usar esta forma para no modificar la lista original


# tuplas
coordenadas = (10, 20)

# conjuntos
frutas = {'manzana', 'pera', 'uva'}
# insercion en conjuntos
frutas.add("fresa")       # Agrega un elemento
print(frutas)
# elimina
frutas = {"manzana", "pera", "uva"}
frutas.remove("pera")     # Elimina un valor (error si no existe)
frutas.discard("fresa")   # Elimina si existe, sin error
print(frutas)



# diccionarios
personas = {'nombre': "ana",'edad': 25, 'nombre1': 'pepe', 'edad1': 23}
print(personas)
personas['nombre2'] = "pedro"
personas['edad2'] = 25    # Inserta una nueva clave con valor
print(personas)
# actualizar
personas["edad"] = 40
print(personas)
#eliminar
del personas["edad"]       # Elimina una clave
print(personas)

# ordenar diccionarios
persona = {"c": 3, "a": 1, "b": 2}
ordenado = dict(sorted(persona.items()))  # Por clave
print(ordenado)


cuadrados = [x**2 for x in range(5)]
print(cuadrados) # [0, 1, 4, 9, 16]

# funciones anonimas
cuadrado = lambda x: x**2
print(cuadrado(4))  # 16


"""Ejercicio 3"""

agenda = []

def mi_agenta():

    opciones = [1, 2, 3, 4, 5]

    def opcion_1():
        nombre = input("Ingrese el nombre del usuario: ").strip()
        celular = input("Ingrese el celular del usuario: ").strip()
        if not celular.isdigit():
            print("\nEl numero solo debe contener digitos")
            return opcion_1()
        if len(celular) > 10:
            print("\nEl numero no debe tener mas de 10 digitos")
            return opcion_1()
        agenda.append({"nombre": nombre, "celular": celular})
        print(f"\nUsuario '{nombre}' agregado correctamente.\n")
        pantalla()

    def opcion_2():
        busqueda_usuario = input("\nInserte el nombre del usuario: ").strip()
        encontrado = False
        for u in agenda:
            if u["nombre"].lower() == busqueda_usuario.lower():
                print(f"\nInformacion del usuario: nombre: {u['nombre']} Celular: ({u['celular']})\n")
                encontrado = True
                pantalla()
        if not encontrado:
            print("\nUsuario no existe\n")
            pantalla()

    def opcion_3():
        name = input("\nInserte el nombre del usuario a actualizar: ").strip()
        encontrado = False
        for u in agenda:
            if u["nombre"] == name:
                print(f"\nInformacion del usuario: nombre: {u['nombre']} Celular: ({u['celular']})\n")
                nuevo_nombre = input("Ingrese el nuevo nombre (deje vacio para no cambiar nada: )")
                nuevo_celular = input("Ingrese el nuevo celular (deje vacio para no cambiar nada: )")
                if nuevo_celular:
                    if not nuevo_celular.isdigit():
                        print("\nEl numero solo debe contener digitos")
                        return opcion_1()
                    if len(nuevo_celular) > 10:
                        print("\nEl numero no debe tener mas de 10 digitos")
                        return opcion_1()
                    u["celular"] = nuevo_celular
                if nuevo_nombre:
                    u["nombre"] = nuevo_nombre

                print("\nSe a actualizado correctamente.\n")
                pantalla()
        if not encontrado:
            print("\nUsuario no existe, no actualiza\n")
            pantalla()

    def opcion_4():
        name = input("\nInserte el nombre del usuario a eliminar: ").strip()
        for u in agenda:
            if u["nombre"] == name:
                print(f"\nInformacion del usuario: nombre: {u['nombre']} Celular: ({u['celular']})\n")
                print(f"\nSe a eliminado correctamente a {u['nombre']}\n")

                agenda.remove(u)
                pantalla()
    def opcion_5():
        print("Saliendo del programa...")
        exit()


    acciones = {
    1: opcion_1,
    2: opcion_2,
    3: opcion_3,
    4: opcion_4,
    5: opcion_5
    }

    def operacion(y): # don't used
        if y in opciones:
            print(f"Opcion elegida es: {y}")


    def pantalla():
            while True:
                try:
                    x = int(input("Que accion deseas realizar:\n1. Insertar usuario\n2. Buscar usuario\n" \
                            "3. Actualizar usuario\n4. Eliminar usuario\n5. Salir\n" \
                            "Indique una opción: "))
                    if x in opciones:
                        accion = acciones.get(x, lambda: print("Opción no válida"))
                        accion()
                        break
                    else:
                        print("\nBoludo es del 1 al 5\n")
                except ValueError:
                    print("\nSolo se permiten numeros\n")

    pantalla()

mi_agenta()