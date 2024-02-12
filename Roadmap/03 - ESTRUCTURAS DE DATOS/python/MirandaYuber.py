print('######  LISTAS  ######')  # Son mutables
print()

my_list = [1, 2]
print(f'Lista: {my_list}')

my_list.append(10)
print(f'Append(Agrega elementos al final de la lista): {my_list}')

my_list.extend([11, 12, 13, 14, 15])
print(f'Extend(Agrega una lista al final de la lista): {my_list}')

print(f'Index(Obtener posición del elemento indicado): {my_list.index(11)}')

my_list.insert(2, 9)
print(f'Insert(Inserta un elemento segun el indice): {my_list}')

my_list.remove(9)
print(f'Remove(Elimina el elemento de la lista): {my_list}')

print(f'Pop(Devuelve el ultimo elemento): {my_list.pop()}')

print(f'Count(Devuelve conteo de cuantos elementos hay en la lista): {my_list.count(1)}')

my_list.sort(reverse=True)
print(f'Sort(Ordena la lista descendente): {my_list}')
my_list.sort()
print(f'Sort(Ordena la lista ascendente): {my_list}')
my_list.reverse()
print(f'Reverse(Desordena la lista sin ordenarla antes): {my_list}')
print()
print()


print('######  TUPLAS  ######')  # Son inmutables
print()

my_tuple = ('1', '2', '3')
print(f'Tupla: {my_tuple}')

print(f'Len(Obtener tamaño de la tupla): {len(my_tuple)}')

print(f'Obtener por rango de posición[index_inicial:index_final]: {my_tuple[1:]}')

print(f'Obtener por posición[index]: {my_tuple[1]}')

my_tuple2 = (1,)
print(f'Crear una tupla con un solo valor (value,): {my_tuple2}')
print()
print()


print('######  SETS  ######')  # Son como listas sin orden especifico y sin valores repetidos
print()

my_set = {4, 1, 9, 6}
print(f'Set: {my_set}')

my_set.add(2)
print(f'Add(Agrega nuevo elemento): {my_set}')

print(f'In(Revisar si existe un elemento dentro del set): {4 in my_set}')

print()
print()


print('######  STRINGS  ######')
print()

my_string = 'Yuber Miranda, Python'
print(f'String: {my_string}')

print(f'Len(Obtener tamaño del string: {len(my_string)})')

print(f'Obtener caracter por pocisión([1]): {my_string[1]}')

print(f'Obtener caracter por rango de pocisión ([1:5]): {my_string[1:5]}')

print(f'In(Buscar una cadena dentro del string): {"a" in my_string}')

print(f'Split(Guarda la cadena en un arreglo): {my_string.split()}')

new_list = my_string.split(",")
print(f'Split(Guarda la cadena en una lista indicandole el caracter): {new_list}')

print(f'Join(Unir la lista en un string): {",".join(new_list)}')

print(f'Strip(Remover espacios vacios del string): {" example@example.net".strip()}')

print(f'Strip(Remover caracteres del string): {"aeioub".strip("aei")}')
print()
print()


print('######  DICIONARIOS  ######')  # Similiar a una lista parecido a un JSON
print()

my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(f'Diccionario: {my_dictionary}')

print(f'Acceder al valor por medio de la clave(my_dictionary["tag"]): {my_dictionary["a"]}')

new_dictionary = {}
new_dictionary["x"] = 2
new_dictionary[2] = 3
new_dictionary[(1, 2)] = 4
print(f'Agregar una clave con su valor al diccionario: {new_dictionary}')

del new_dictionary[2]
print(f'Eliminar del diccionario un valor por su clave: {new_dictionary}')

print(f'Keys(Obtener las keys del diccionario): {new_dictionary.keys()}')

print(f'Values(Obtener los valores del diccionario): {new_dictionary.values()}')

print('Recorrer un diccionario con un for:')
for key, value in new_dictionary.items():
    print(key, value)

print(f'Buscar dentro de un diccionario por la clave: {"x" in new_dictionary}')

print(f'Obtener valor de un diccionario por la clave: {new_dictionary.get("x")}')

print(f'Si no existe la clave, retorna un valor por defecto: {new_dictionary.get("t", 9)}')

