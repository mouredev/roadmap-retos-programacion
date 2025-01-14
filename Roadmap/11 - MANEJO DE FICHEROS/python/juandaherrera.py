"""
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
"""

import os

file_name = 'juandaherrera.txt'

with open(file_name, 'w') as file:
    file.write('Nombre: Juan David Herrera\n')
    file.write('Edad: 24\n')
    file.write('Lenguaje favorito: Python\n')

with open(file_name, 'r') as file:
    content = file.read()

print(content)

if os.path.exists(file_name):
    os.remove(file_name)


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""

from dataclasses import dataclass, field, fields
from typing import Union


@dataclass
class Transaction:
    id: int
    product: str
    qty: int
    price: float

    @property
    def total(self):
        return self.qty * self.price


@dataclass
class DataBase:
    transaction_list: list[Transaction] = field(default_factory=list)
    file_name: str = 'juandaherrera_bd.txt'

    def __post_init__(self):
        self.load_transactions_from_file()

    def load_transactions_from_file(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                for line in file:
                    id_str, product, qty_str, price_str = line.strip().split(', ')

                    id = int(id_str)
                    qty = int(qty_str)
                    price = float(price_str)

                    transaction = Transaction(id=id, product=product, qty=qty, price=price)
                    self.transaction_list.append(transaction)

    def save_database(self):
        with open(self.file_name, 'w') as file:
            for transaction in self.transaction_list:
                file.write(
                    f'{transaction.id}, {transaction.product}, {transaction.qty}, {transaction.price}\n'
                )

    def search_transaction(self, id) -> Union[int, None]:
        for index, transaction in enumerate(self.transaction_list):
            if transaction.id == id:
                return index

        return None

    def next_id(self) -> int:
        if len(self.transaction_list) == 0:
            return 1
        return max((transaction.id for transaction in self.transaction_list)) + 1

    def add_transaction(self, product: str, qty: int, price: float, id: int = None):
        if not id or id == '':
            id = self.next_id()
        elif self.search_transaction(int(id)):
            raise ValueError(f'La transacción con id {id} ya existe. Ingrese un id diferente')

        transaction = Transaction(int(id), product, qty, price)

        self.transaction_list.append(transaction)
        self.save_database()

    def update_transaction(self, id: int, product: str, qty: int, price: float):
        transaction_index = self.search_transaction(int(id))
        if transaction_index is None:
            raise ValueError(f'La transacción con id {id} NO existe. Ingrese un id diferente')

        self.transaction_list[transaction_index] = Transaction(id, product, qty, price)
        self.save_database()

    def delete_transaction(self, id: int):
        transaction_index = self.search_transaction(int(id))
        if not transaction_index:
            raise ValueError(f'La transacción con id {id} NO existe. Ingrese un id diferente')

        del self.transaction_list[transaction_index]
        self.save_database()


database = DataBase()

print('-' * 30)
print('Opciones')
print(
    '1. Agregar transacción',
    '2. Editar transacción',
    '3. Eliminar transacción',
    '4. Ver transacción',
    '5. Ver todas las transacciones',
    '6. Salir',
    sep='\n',
)
while True:
    print('-' * 30)
    option = input('Ingrese la opción: ')

    match option:
        case '1':
            try:
                id = input('id: ')
                product = input('product: ')
                qty = int(input('qty: '))
                price = float(input('price: '))

                database.add_transaction(id=id, product=product, qty=qty, price=price)
            except Exception as e:
                print('Error:', e)
        case '2':
            try:
                id = input('id: ')
                product = input('product: ')
                qty = int(input('qty: '))
                price = float(input('price: '))

                database.update_transaction(id=id, product=product, qty=qty, price=price)
            except Exception as e:
                print('Error:', e)
        case '3':
            try:
                id = input('id: ')
                database.delete_transaction(id)
            except Exception as e:
                print('Error:', e)
        case '4':
            try:
                id = input('id: ')
                index = database.search_transaction(int(id))
                print(database.transaction_list[index])
            except Exception as e:
                print('Error:', e)
        case '5':
            print(database.transaction_list)
        case '6':
            if os.path.exists(database.file_name):
                os.remove(database.file_name)
            break
        case _:
            print('Intenta otra opción')
