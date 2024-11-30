# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio

''' * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
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

def main():
    # CREAMOS LISTA
    this_is_a_list = [1, 2, 3, 4]
    print(this_is_a_list)
    # insertar podemos usar el metodo insert en el index que deseamos (en este caso lo inserto al inicio)
    this_is_a_list.insert(0, 0)
    print(this_is_a_list)
    # actualizar podemos usar el metodo append (agrega el objeto al final de la lista)
    this_is_a_list.append(5)
    print(this_is_a_list)
    # ordenar podemos usar el metodo sort (yo lo use para odenarlo al reves con el parametro reverse=True)
    this_is_a_list.sort(reverse=True)
    print(this_is_a_list)
    # borrar el contenido de la lista (no la lista en si misma) podemos usar el metodo clear
    this_is_a_list.clear()
    print(this_is_a_list)
    
    # CREAMOS DICCIONARIO
    this_is_a_dictionary = {"key1" : 1, "key2" : 2, "key3" : 3}
    print(this_is_a_dictionary)
    # insertar, nombramos una nueva key en el diccionario, y asignamos su value correspondiente
    this_is_a_dictionary["key4"] = 4
    print(this_is_a_dictionary)
    # actualizar los objetos de un dict, incluyendo en este los objetos de un segundo dict
    this_is_another_dictionary = {"key5": 5}
    this_is_a_dictionary.update(this_is_another_dictionary)
    print(this_is_a_dictionary)
     # podemos actualizar, si accedemos al key que queremos modificar y le reasignamos un value nuevo
    this_is_a_dictionary["key4"] = "four"
    print(this_is_a_dictionary)
    # Nuevo diccionario
    new_dict = {"one":1, "three":3, "two": 2, "five": 5, "four" : 4}
    # ordenar mediante la funcion sorted y un dict comprehension (ordenando por keys)
    # Ya que las keys son str, se ordenan en orden alfabetico
    sorted_by_keys = {key: new_dict[key] for key in sorted(new_dict)}
    print(f"Sorted by keys: {sorted_by_keys}")

    # ordenar mediante la funcion sorted y un dict comprehension (ordenado por values)
    sorted_by_values = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1])}
    print(f"Sorted by values: {sorted_by_values}")

     # O bien podemos ordenar usando el modulo OrderedDict
     # Ya que las keys son str, se ordenan en orden alfabetico
    from collections import OrderedDict
    ordered_dictionary = OrderedDict(sorted(new_dict.items()))
    print(ordered_dictionary)
    # Para borrar el contenido de la lista (no la lista en si misma) podemos usar el metodo clear
    this_is_a_dictionary.clear()
    print(this_is_a_dictionary)
    new_dict.clear()
    print(new_dict)

    # CREAMOS SET (desordenado, no admite duplicados)
    this_is_a_set = {2, 1, 3}
    print(this_is_a_set)
    # insertar podemos usar el metodo add y se agrega al final
    this_is_a_set.add(4)
    print(this_is_a_set)
    # actualizar podemos usar el metodo update que actualiza el set uniendo los datos de otro set
    new_set = {6, 5}
    print(new_set)
    this_is_a_set.update(new_set)
    print(this_is_a_set)
    # ordenar podemos convertir el set a una lista y ordenar la lista
    list_from_set = sorted(this_is_a_set)
    print(list_from_set)
    # borrar el contenido del set usamos el metodo clear
    this_is_a_set.clear()
    print(this_is_a_set)

    # CREAMOS TUPLA (inmutable)
    this_is_a_tuple = (1, 2, 3, 4)
    print(this_is_a_tuple)
    # insertar y actualizar, convertimos la tupla a lista, le agregamos el miembro nuevo, y la reconvertimos a tupla
    print("Tupla convertida a lista para insertar y actualizar")
    list_from_tuple = list(this_is_a_tuple)
    list_from_tuple.append(5)
    print(f"Lista despues del append (insertamos) {list_from_tuple}")

    list_from_tuple.insert(4, 4.5)
    print(f"Lista despues del insert (actualizamos) {list_from_tuple}")

    this_is_a_tuple = tuple(list_from_tuple)
    print(this_is_a_tuple)
   
    # ordenar la tupla, la convertimos a lista, usamos sort, y la reconvertimos a tupla tuple("nombre de la lista")
    unordered_tuple = (4,2,5,3,1)
    print(f"Tupla desordenada {unordered_tuple}")
    ordered_list = list(unordered_tuple)
    ordered_list.sort()
    unordered_tuple = tuple(ordered_list)
    print(f"Tupla Ordenada {unordered_tuple}")
    # borrar la tuple usamos la palabra reservada del
    del this_is_a_tuple
    
if __name__=="__main__":
    main()

