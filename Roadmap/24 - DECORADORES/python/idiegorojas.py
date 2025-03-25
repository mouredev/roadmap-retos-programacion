"""
24 - Patrones de Diseño: Decoradores
"""
# Es un patron estructural que permite agregar funcionalidad a un objeto 
# No modifica la estrucura original del objeto
# Se usa para extender el comportamiento de clases sin usar herencia


"""
Estructura basica
"""
# Componente base: La funcionalidad basica que se desea extender
# Decorador: Funcion o clase que toma un componente y le añade nuevas funcionalidades
# Uso del decorador: Se aplica a un objeto, una funcion o metodo para modificar su comportamiento


"""
Ejemplo:
"""

# Cafeteria
# Tenemos una cafetería donde vendemos café. Un café básico cuesta $2, pero los clientes pueden agregar extras como leche, azúcar o canela.

class Cafe:
    def costo(self):
        return 2 # Precio base del cafe
    
    def descripcion(self):
        return 'Cafe basico'
    
class Leche:
    def __init__(self, cafe) -> None:
        self.cafe = cafe

    def costo(self):
        return self.cafe.costo() + 0.5 
    
    def descripcion(self):
        return self.cafe.descripcion() + ' con leche'

class Azucar:
    def __init__(self, cafe) -> None:
        self.cafe = cafe

    def costo(self):
        return self.cafe.costo() + 0.2
    
    def descripcion(self):
        return self.cafe.descripcion() + ' con azucar'
    

# Cafe basico
cafe_basico = Cafe()
print(f'El cafe que pediste es: {cafe_basico.descripcion()} y tiene un costo de: ${cafe_basico.costo()}')

# Cafe con leche
cafe_leche = Leche(cafe_basico)
print(f'El cafe que pediste es: {cafe_leche.descripcion()} y tiene un costo de: ${cafe_leche.costo()}')

# Cafe con leche y azucar
cafe_leche_azucar = Azucar(cafe_leche)
print(f'El cafe que pediste es: {cafe_leche_azucar.descripcion()} y tiene un costo de: ${cafe_leche_azucar.costo()}')

"""
¿Cuándo usar el patrón decorador?
"""
# Cuando queremos extender funcionalidades sin modificar el código original.
# Para modularizar y reutilizar código fácilmente.
# Cuando necesitamos aplicar múltiples comportamientos dinámicos (Ej: logging, permisos, validaciones, caching).

"""
Extra
"""

def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La función '{function.__name__} se ha llamado {counter_function.call_count}' veces.")
        return function

    counter_function.call_count = 0
    return counter_function


@call_counter
def example_function_1():
    pass


@call_counter
def example_function_2():
    pass


example_function_1()
example_function_1()
example_function_1()
example_function_2()
example_function_1()
example_function_2()
example_function_2()