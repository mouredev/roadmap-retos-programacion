'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

'''

#BUILT IN DATA STRUCTURES

## 1. List
my_list = [2,3,4,-10-4]
other_list = list()
my_new_list = [x for x in my_list if x >= 0]


# Using listComp: select all columns of matrix in one line
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transpuesta = []
for i in range(len(matrix)):
    column_list = []
    for column in matrix:
        column_list.append(column[i])
    transpuesta.append(column_list)
    #print(transpuesta)
print(f"Sin usar listas de comprensión: {transpuesta}")

listcomp_transpuesta = [[column[i] for column in matrix] for i in range(len(matrix))]
print(f"Usando listas de comprensión: {listcomp_transpuesta}")


## 2. Tuples
# Son una estructura inmutable aunque puede contener datos mutables como las listas etc...
my_tuple = (1234,6789,"Alonso","Mimi",[9,10,11])
other_tuple = tuple()

# Empaquetado VS Desempaquetado de secuencias
tupla_palabras = ("word1","word2","word3")
# Proceso de desempaquetado de secuencias: IMPORTANTE--> Siempre el número de variables de la izquierda tiene que sel igual al número de la secuencia
w1, w2, w3 = tupla_palabras
print(f"Mi palabra1: es {w1.upper()}, mi palabra2: {w2.upper()} y la tercera es: {w3.upper()}")

## 3.Sets. Es una estructura de datos NO ordenada de elementos ÚNICOS 
mi_set = {"manzana","pera","pera","manzana","platano","uvas"}
print(f"Mi set SIN setComprension: {mi_set}")

setComp = {x for x in mi_set}
print(f"Mi set CON setComprension: {setComp}")

a = {x for x in "abracadabra" if x not in "abc"}
print(a)


## 4. Dict: A diferencia de estructuras como las listas o las tuplas los diccionarios NO SE INDEXAN de forma numérica sino a través de claves
my_dict = {
    "nombre":"Mimi",
    "edad": 26,
    "profesión":"Periodista"
}
# Imprimo solo las llaves del diccionario
print(list(my_dict))
# También podemos crear dict con DictComp
dict_al_cuadrado = {"Num("+str(x)+")":"Potencia("+str(x*2)+")" for x in dict_numerico}

print(" ----------------------------------- ")

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

'''
agenda = {}

def agregar_contacto():
    isContinue = True
    while isContinue:
        name = str(input("Introduce el nombre del contacto: "))
        phone = input("Introduce el número del contacto: ")

        if name not in agenda:
            if (phone.isdigit()) and (0 < len(phone) <= 11):
                agenda[name] = phone
                print("✅ Contacto agregado")
                isContinue = False
            else:
                print("💥 ERROR: Introduce datos válidos por favor ")
        else:
            print("💥 ERROR: Usuario ya existente. ")


def buscar_contacto():
    name = input("Introduce el nombre del usuario que quieres: \n")
    if name in agenda:
        print(f" ▶▶▶ El número de {name.upper()} es {agenda[name]}")
    else:
        print("💥 ERROR: Usuario no existe ")


def eliminar_contacto():
    name = input("Introduce el nombre del usuario que quieres eliminar: \n")
    if name in agenda:
        del agenda[name]
        print(f" ▶▶▶ El usuario {name.upper()} ha sido eliminado ")
    else:
        print("💥 ERROR: Usuario no existente. ")


def actualizar_contacto():
    name = input("Introduce el nombre del usuario que quieres actualizar: \n")
    phone = input("Introduce el numero del usuario que quieres actualizar: \n")
    if name in agenda:
        print(f" ▶▶▶ El usuario {name.upper()} ha sido actualizado ")
        agenda[name] = phone
    else:
        print("💥 ERROR: Usuario no existente. ")


while True:
    print(""" 
        << Agenda Nightblockchain30 >>
        
            1. Agregar un contacto
            2. Buscar un contacto
            3. Eliminar un contacto
            4. Actualizar un contacto
            5. Salir de la agenda
""")
    option = int(input("Elige una de las siguientes opciones: \n"))

    match option:
        case 1:
            agregar_contacto()
        case 2:
            buscar_contacto()
        case 3:
            eliminar_contacto()
        case 4:
            actualizar_contacto()
        case 5:
            break
        

print(f"Gracias por tu confianza! Saludos‼")
        



