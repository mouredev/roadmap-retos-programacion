from functools import reduce
from datetime import datetime
"""
Ejercicio
"""

def al_cubo(num, cuadrado ):
    print(cuadrado(num)*num)

def cuadrado(num):
    return num*num

al_cubo(4, cuadrado)


# Retorno de función


def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(2))

#  Sistema

numbers = [1, 3, 4, 2, 5]

# map()


def apply_double(n):
    return n * 2


print(list(map(apply_double, numbers)))

# filter()


def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, numbers)))

# sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()


def sum_values(x, y):
    return x + y


print(reduce(sum_values, numbers))

"""
Extra
"""
# Alumno y Promedio  
lista_alumnos=[
    {"nombre": "Diego", "fecha_nac":"09/06/1981", "notas":[9,9,9.5,8]},
    {"nombre": "Pepe", "fecha_nac":"08/07/1982", "notas":[2,3,4,8]},
    {"nombre": "Carlos", "fecha_nac":"08/06/1981", "notas":[8,7.5,9,7]},
]

def promedios_nota(notas):
    return sum(notas)/ len(notas)


print(list(map(lambda alumno: {"nombre": alumno["nombre"], 
                    "promedio":promedios_nota(alumno["notas"]) },
                lista_alumnos)))

#Alumnos con promedio mayor o igaul a 9
print(
    list(
        map(
            lambda alumno:  alumno["nombre"], 
                   filter(lambda alumno: promedios_nota(alumno["notas"])>=9, lista_alumnos) 
            )
        )
    )

#Alumnos ordenados por edad 
print(
    sorted(lista_alumnos, key=lambda alumno: datetime.strptime(alumno["fecha_nac"], "%d/%m/%Y"), reverse=True) 
        
)

#Mayor nota de entre todos los alumnos

print(max(map(lambda alumno: max(alumno["notas"]), lista_alumnos )))