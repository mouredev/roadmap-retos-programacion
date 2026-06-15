'''
Ejercicio:
Desarrolla un programa que lea los registros de un fichero .csv y seleccione de manera aleatoria diferentes ganadores.

Requisitos:
    1. Crea un .csv con 3 columnas: id, email y status con valor "activo" o "inactivo" (y datos ficticios).
        Ejemplo:
        1 | test@test.com | activo
        2 | test2@test.com | inactivo
        (El .csv no debe subirse como parte de la correccion)
    2. Recupera los datos desde el programa y selecciona email aleatorios.

Acciones:
    1. Accede al fichero .csv y selecciona de manera aleatoria un email ganador de una suscripcion, otro ganador de un descuento y un ultimo ganador de un libro (solo si tiene status "activo" y no esta repetido).
    2. Muestra los emails ganadores y su id.
    3. Ten en cuenta que la primera fila (con el nombre de las columnas) no debe tenerse en cuenta.
    '''

import pandas as pd
import random

# Leemos el archivo de .csv
data = pd.read_csv("archivo.csv")

# Obtenemos el email del ganador de la sub
sub_winner = random.choice(data['email'])

# Obtenemos el email del ganador del descuento
discount_winner = random.choice(data['email'])
while discount_winner == sub_winner:
    discount_winner = random.choice(data['email'])

# Creamos una lista en donde solo esten aquellas personas que tengan un estado activo
activos = data[data['status'] == 'activo']
if not activos.empty: 
    book_winner = random.choice(list(activos['email']))
    while book_winner in (sub_winner, discount_winner):
        book_winner = random.choice(list(activos['email']))

# Obtenemos los id de los ganadores.
sub_winner_id = data.loc[data['email'] == sub_winner, 'id'].values[0]
discount_id = data.loc[data['email'] == discount_winner, 'id'].values[0]
book_id = data.loc[data['email'] == book_winner, 'id'].values[0]

# Mostrar resultados
print("GANADORES: ")
print(f"Suscripcion: {sub_winner} | ID: {sub_winner_id}.")
print(f"Descuento: {discount_winner} | ID: {discount_id}.")
print(f"Libro: {book_winner} | ID: {book_id}.")