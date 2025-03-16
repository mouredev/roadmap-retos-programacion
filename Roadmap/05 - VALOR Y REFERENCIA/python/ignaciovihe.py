"""
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
  su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
"""


"""
Asignacion
"""
# Los tipos inmutables de python siempre se asignan por valor.
# Por lo tanto siempre se creeara un nuevo objeto aunque se asigne una variable a otra,
# y el valor no cambiara aunque posteriormente cambiemos el valor de la primera.
# Los datos inmutables en python son: int, float, complex, str, tuple, bool...

my_variable = 1 #Asignamos los valores
my_other_variable = 2

print(f"my_variable = {my_variable}")
print(f"my_other_varibale = {my_other_variable}")

my_other_variable = my_variable # aunque apuntemos una variable a otra, como es un tipo inmutable solo copia el valor.

print(f"my_variable = {my_variable}")
print(f"my_other_varibale = {my_other_variable}")

my_variable = 3 #Aunque modifiquemos el valor, se mantiene el mismo.

print(f"my_variable = {my_variable}")
print(f"my_other_varibale = {my_other_variable}")

#Los tipos mutables si se pueden asignar por referencia.
# Los tipos muitables en python son: list, dict, set

my_dict = {"nombre": "Ignacio", "genero": "masculino", "edad": 40} # Asignamos dos variables por valor
your_dict = {"nombre": "Maria", "genero": "femenino", "edad": 33}

print(f"my_dict = {my_dict}")
print(f"your_dict = {your_dict}")

your_dict = my_dict #Asignamos la variable your_dict por referencia. 

print(f"my_dict = {my_dict}")
print(f"your_dict = {your_dict}")

your_dict["nombre"] = "Nacho"   #Modificamos el valor de la variable vemos como tambien cambia el de la otra.
                                #Realmente esta apuntando a la referencia de memoria. Apunta al mismo objeto.

print(f"my_dict = {my_dict}")
print(f"your_dict = {your_dict}")



"""
Funciones con parametros por valor y referencia
"""
# Realmente en python todo se para por referencia. Pero los tipos inmutables no afectac a la variable exterior
# Parametros inmutables. Con datos inmutables, cualquier modificación dentro de la función no afecta a la variable fuera de la función.

number_1 = 3

def duplicate(number: int):
    number *= 2

print(f"number_1 = {number_1}")
duplicate(number_1)
print(f"number_1 = {number_1}")

#Si queremos que una funciona modifique la variable de fuera usamos return para modificar el valor.




#Parametros mutables

my_list = [2,8,3,5,1,9,0,4,6,7]

def sort_list(unsorted_list: list):
    unsorted_list.sort()
    other_list = unsorted_list
    other_list.append("a") # Aunque lo añado en una variable diferente apuntan a la misma direccion de memoria por lo tanto se añade a

print(f"my_list = {my_list}")
sort_list(my_list)
print(f"my_list = {my_list}")   # Aunque no devuelvo un valor como es un tipo mutable se pasa por referencia 
                                # y afecta a la variable exterior.



# Si queremos que una función no modifique la variable exterior pordemos usar el metodo .copy()

my_list = [2,8,3,5,1,9,0,4,6,7]

def sort_list_copy(unsorted_list: list):
    
    unsorted_list = unsorted_list.copy() # Esto simula un tipo mutable pasado como valor. No afectara a la variable exterior.
    unsorted_list.sort()
    print(f"La lista dentro = {unsorted_list}")

print(f"La lista original fuera = {my_list}")
sort_list_copy(my_list)
print(f"La lista despues de la funcion con copia = {my_list}")

"""
DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""


def swap_values(param1, param2):
    param_aux = param1
    param1 = param2
    param2 = param_aux
    if type(param2) == list:
        param2.append("Nuevo valor")
    return param1, param2

# Por valor
win = "First"
lost = "Last"
new_win, new_lost = swap_values(win, lost)

print(f"win: {win}")
print(f"lost: {lost}")

print(f"new_win: {new_win}")
print(f"new_lost: {new_lost}")

#Por referencia

letters = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3, 4, 5]
new_letters, new_numbers = swap_values(letters, numbers)

print(f"letters: {letters}")    # Alintercambiar la referencias dentro de la funcion se hace de forma local.
print(f"numbers: {numbers}")    # Por lo tanto las variable exteriores no cambian.
                                # Pero si añado un valor si que cambia la lista.

print(f"new_letter: {new_letters}")
print(f"new_numbers: {new_numbers}")


