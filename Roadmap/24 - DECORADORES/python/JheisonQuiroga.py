# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico."""

from abc import ABC, abstractmethod

# Creamos la interfaz o clase base
class Pokemon(ABC):
    @abstractmethod
    def get_data(self):
        pass


# Componente Concreto
class Pikachu(Pokemon):
    def get_data(self):
        return "Pikachu: Tipo eléctrico"
    

# Decorador Abstracto: Envuelve un objeto de tipo Pokemon
class PokemonDecorator(Pokemon):

    _pokemon: Pokemon

    def __init__(self, pokemon: Pokemon):
        self._pokemon = pokemon

    @property
    def pokemon(self) -> Pokemon:
        return self._pokemon
    
    def get_data(self):
        return self._pokemon.get_data()
    
# Decorador Concreto: Añade responsabilidades al objeto
class PokemonWithMoves(PokemonDecorator):
    def get_data(self):
        data = self.pokemon.get_data()
        return f"{data}, Movimientos: Impactrueno, Cola de Hierro."


"""*
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */"""

def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        print("Iniciando")
        result = func(*args, **kwargs)
        nonlocal count
        count += 1
        print(f"La función {func.__name__} ha sido llamada {count} veces.")
        print("Finalizando")
        return result
    return wrapper


@count_calls
def add_numbers(n1, n2):
    return n1 + n2


if __name__ == "__main__":
    # Creamos un Pokémon simple
    pikachu = Pikachu()
    print(pikachu.get_data())

    # Se decora el pokémon agregandole movimientos
    pikachu_with_moves = PokemonWithMoves(pikachu)
    print(pikachu_with_moves.get_data())

    # Extra

    print(add_numbers(5, 2))
    print(add_numbers(2, 2))
    print(add_numbers(3, 2))
    print(add_numbers(8, 6))
    print(add_numbers(7, 13))