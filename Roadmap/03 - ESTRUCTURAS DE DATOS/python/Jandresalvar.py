'''
Estructuras de datos integradas por defecto
'''

''' 
Cadenas de texto (strings):
La primera estructura es también un tipo de dato, que mediante bucles, condicionales, funciones, etc. podemos recorrer cada caracter como un elemento independiente, por ejemplo:
'''

my_string = 'Hola, Moure' 

print(my_string.casefold()) # Podemos usar metodos (funciones) para manipular strings

#my_string[0] = 'B' # Esto produce un error porque las cadenas son secuencias "inmutables" de caracteres

for letter in my_string: # Podemos recorrer una cadena mediante un bucle
    print(letter)

def imprime_nombre(string):
    if string.startswith('Hola'): # Condicionales
        return string[string.find(',') + 2 :]

print(imprime_nombre(my_string))

texto = 'Python'
nuevo_texto = texto[:2] + 'x' + texto[3:]
print(nuevo_texto)

'''
Listas (list):
Las listas son estructuras mutables y ordenadas que pueden contener cualquier tipo de dato, por ejemplo:
'''

my_list = [1, 2, 3, 4, 5] #Se puede crear una lista con [] o con la funcion list()
#Decimos que una lista es ordenada porque, aunque no lo vemos, cada elemento tiene asociado un indice que va de 0 hasta n-1, siendo n la cantidad de elementos de la lista

my_list[0] = 10 # Esto no produce errores, es perfectamente posible porque las listas son mutables
print(dir(my_list)) #accedemos a los metodos de un tipo de dato o estructura mediante la funcion dir
my_list.append(6)
my_list.insert(0, 1)
my_list.pop(1)
print(my_list)

my_list.sort(reverse = True)
print(my_list)

for num in my_list:
    print(num)

my_list2 = ("Hola", 40, 33.35, True)
my_list.insert(3, my_list2) # Listas dentro de listas 🤯
print(my_list)

for i in my_list2:
    print(i)

'''
Tuplas (tuple):
Las tuplas son muy parecidas a las listas, las diferencian principalmente tres caracteristicas, las tuplas son inmutables, no ordenadas y generalmente se usan para almacenar datos heterogeneos (no es estricto pero por convension lo es)
'''
my_tuple = 1984, 2025, "Python"
print(my_tuple[1])

a, b, c = my_tuple

my_tuple_2 = ([9, 8, 7, 6], [6, 7, 8, 9]) #Aunque una tupla es inmutable, puede contener objetos mutables

for item in my_tuple_2:
    for num in item:
        print(num)

 
'''
Conjuntos (set):
Es una colección no ordenada y sin elementos duplicados. Se puede crear un conjunto con {} o la funcion set(), pero para crear un conjunto vacio no se usa {}, pues esto creará un diccionario. Los conjuntos también soportan operaciones matemáticas como la unión, intersección, diferencia, y diferencia simétrica.
'''

jugadores = {"Cristiano", "Messi", "Iniesta", "Xavi", "Messi", "Pele"}

print(jugadores)

"Pele" in jugadores

bucle = {x for x in "Parangaricutirimicuaro" if x not in "abc"}
print(bucle)

s = {1, 3}
s.add(2)
s.remove(1) 
sorted(s)
print(s)

'''
Diccionarios (dict):
Un diccionario es muy similar a un conjunto o una lista. Sin embargo, su principal diferencia es que en lugar de usar indicer núnmericos ordenados, un diccionario utiliza como indice una "clave". Cada clave está asociada a un valor, por esto se les llama pares "clave: valor". Las claves son únicas dentro del diccionario. En escencia, los elementos de un diccionario son tuplas clave/valor.
'''
telefonos = {'Andres': 3126, 'Moure': 3468, 'Python': 3249}
telefonos['Brais'] = 9284
print(telefonos)

del telefonos['Moure']
telefonos['Snake'] = 2087
print(telefonos)

'Moure' not in telefonos
'Snake' in telefonos

tels = dict([('Andres', 3126), ('Python', 3249), ('Brais', 9284)])
print(tels)

my_dict = {x: x**2 for x in (2, 4, 6)}
print(my_dict)

d = {'b': 2, 'a': 1}
ordenado = dict(sorted(d.items()))
print(ordenado)

'''
Ejercicio Extra
'''

directorio = dict()

while True:

    print('\n--- Agenda de Contactos ---')
    print('Operaciones disponibles: añadir, borrar, buscar, actualizar, salir')

    operacion = input('\nIngresa la operación: ').lower()

    if operacion == "salir": 
        print('¡Hasta luego!')
        break

    if operacion not in ('añadir', 'borrar', 'buscar', 'actualizar'):
        print(f'Error: "{operacion}" no es una operación valida.')
        continue

    nombre = input('Nombre del contacto: ').strip()
    
    if operacion == 'buscar':
        if nombre in directorio:
            print(f'Teléfono: {directorio[nombre]}')
        else:
            print('Contacto no encontrado.')
        continue
        
    if operacion == 'borrar':
        if nombre in directorio:
            del directorio[nombre]
            print(f'Contacto "{nombre}" eliminado.')
        else:
            print('El contacto no existe.')
        continue


    telefono = input('Teléfono: ').strip()

    if not telefono.isdigit():
        print('Error: El teléfono debe contener solo números.')
        continue
    if len(telefono) != 10:
        print('Error: El teléfono debe tener 10 dígitos.')
        continue

    if operacion == 'añadir' and nombre in directorio:
        print('Error: El contacto ya existe. Usa "actualizar".')
        continue

    if operacion == 'actualizar' and nombre not in directorio:
        print('Error: Contacto no encontrado. Usa "añadir".')
        continue
    
    directorio[nombre] = telefono
    print(f'Contacto "{nombre}" {"actualizado" if operacion == "actualizar" else "añadido"}.')
