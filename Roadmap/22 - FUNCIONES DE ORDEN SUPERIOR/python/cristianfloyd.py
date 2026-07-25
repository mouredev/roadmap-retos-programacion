# EJERCICIO:
# Explora el concepto de funciones de orden superior en tu lenguaje
# creando ejemplos simples (a tu elección) que muestren su funcionamiento.

from datetime import date
from typing import Any, Callable, Dict, List

OperacionesMatematicas = Callable[[int, int], int]


def sumar(a: int, b: int) -> int:
    return a + b


def multiplicar(a: int, b: int) -> int:
    return a * b


def potenciar(a: int, b: int) -> int:
    return a**b


lista_original = [1, 2, 3, 4, 5]


def aplicar_operaciones(
    lista: List[int], operaciones: List[OperacionesMatematicas]
) -> Dict[str, List[int]]:
    """
    Funcion de orden superior que aplica una 'operacion' a cada elemento de la 'lista'.

    Args:
        lista: Lista de elementos a los que se le aplicara la 'operacion'.
        operaciones: Lista de operaciones a aplicar a la 'lista'.

    Returns:
        Lista de resultados de las operaciones aplicadas a la 'lista'.
    """
    resultado = {}
    resultados_parciales = []
    for operacion in operaciones:
        for elemento in lista:
            nuevo_valor = operacion(elemento, elemento)
            resultados_parciales.append(nuevo_valor)
        resultado[operacion.__name__] = resultados_parciales.copy()
        resultados_parciales = []
    return resultado


resultado = aplicar_operaciones(lista_original, [sumar, multiplicar, potenciar])

print("=" * 50)
print("Lista original:")
print(lista_original)
print("=" * 50)
print("Resultado de las operaciones aplicadas a la lista:")
for operacion, resultados in resultado.items():
    print(f"{operacion}: {resultados}")
print("=" * 50)


# creador de potencias
def crear_potencia(exponente: int) -> Callable[[int], int]:
    def potencia(base: int) -> int:
        return base**exponente

    return potencia


potencia_2 = crear_potencia(2)
potencia_3 = crear_potencia(3)
potencia_4 = crear_potencia(4)

print("=" * 50)
print("Potencias creadas:")
n = 2
print(f"para base {n}:")
print(f"potencia de {n} elevado a la 2: {potencia_2(n)}")
print(f"potencia de {n} elevado a la 3: {potencia_3(n)}")
print(f"potencia de {n} elevado a la 4: {potencia_4(n)}")
print("=" * 50)


#
# DIFICULTAD EXTRA (opcional):
# Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
# lista de calificaciones), utiliza funciones de orden superior para
# realizar las siguientes operaciones de procesamiento y análisis:
# - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#   y promedio de sus calificaciones.
# - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#   que tienen calificaciones con un 9 o más de promedio.
# - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
# - Mayor calificación: Obtiene la calificación más alta de entre todas las
#   de los alumnos.
# - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

estudiantes = [
    {
        "nombre": "Juan",
        "fecha_nacimiento": date(1999, 5, 10),
        "calificaciones": {
            "matematicas": 9.0,
            "historia": 8.0,
            "ingles": 9.0,
            "fisica": 10.0,
            "quimica": 9.0,
        },
    },
    {
        "nombre": "María",
        "fecha_nacimiento": date(2000, 3, 15),
        "calificaciones": {
            "matematicas": 4.0,
            "historia": 7.0,
            "ingles": 6.0,
            "fisica": 5.0,
            "quimica": 8.0,
        },
    },
    {
        "nombre": "Pedro",
        "fecha_nacimiento": date(1998, 11, 20),
        "calificaciones": {
            "matematicas": 6.0,
            "historia": 9.0,
            "ingles": 4.0,
        },
    },
    {
        "nombre": "Ana",
        "fecha_nacimiento": date(2001, 7, 5),
        "calificaciones": {
            "matematicas": 7.0,
            "historia": 10.0,
            "ingles": 8.0,
        },
    },
]


def obtener_promedio(calificaciones: Dict[str, float]) -> float:
    return sum(calificaciones.values()) / len(calificaciones.values())


def obtener_mejores_estudiantes(estudiantes) -> List[str]:
    return [
        estudiante["nombre"]
        for estudiante in estudiantes
        if obtener_promedio(estudiante["calificaciones"]) >= 9
    ]


def obtener_nacimiento(estudiante: dict[str, Any | date]) -> date:
    return estudiante["fecha_nacimiento"]


# Promedio
promedios = list[dict[str, Any | float]](
    map(
        lambda estudiante: {
            "nombre": estudiante["nombre"],
            "promedio": obtener_promedio(estudiante["calificaciones"]),
        },
        estudiantes,
    )
)

# Mejores estudiantes, nota mayor a 9
mejores_estudiantes = list[dict[str, Any | float]](
    filter(lambda estudiante: estudiante["promedio"] >= 9, promedios)
)

# Nacimiento
mas_jovenes = list[dict[str, Any | date]](
    sorted(estudiantes, key=obtener_nacimiento, reverse=True)
)

# Mayor nota
mayor_nota = max(
    map(lambda estudiante: max(estudiante["calificaciones"].values()), estudiantes)
)

print("=" * 50)
print("Promedios de los estudiantes:")
for promedio in promedios:
    print(f"{promedio['nombre']}: {promedio['promedio']}")
print("=" * 50)

print("=" * 50)
print("Mejores estudiantes:")
for estudiante in mejores_estudiantes:
    print(f"{estudiante['nombre']}: promedio {estudiante['promedio']}")
print("=" * 50)

print("=" * 50)
print("Mas jovenes:")
for estudiante in mas_jovenes:
    print(f"{estudiante['nombre']}: {estudiante['fecha_nacimiento']}")
print("=" * 50)

print("=" * 50)
print("Mayor nota:")
print(mayor_nota)
print("=" * 50)
