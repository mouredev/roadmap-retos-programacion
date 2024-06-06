"""
 EJERCICIO:
 Entiende el concepto de recursividad creando una función recursiva que imprima
 números del 100 al 0.

 DIFICULTAD EXTRA (opcional):
 Utiliza el concepto de recursividad para:
 - Calcular el factorial de un número concreto (la función recibe ese número).
 - Calcular el valor de un elemento concreto (según su posición) en la 
   sucesión de Fibonacci (la función recibe la posición).
"""


def imprime_countdown(entero=100) -> int:
    if entero == 0:
        print(entero, end="\n")
        return entero
    print(entero, end=" - ")
    return imprime_countdown(entero - 1)


print(f"""
Cuando para llegar a un resultado determinado se debe repetir el mismo proceso n cantidad de veces, entonces allí se aplica la recursividad: un proceso
que hace una tarea con la capacidad de autollamarse para procesar hasta lleagr al valor de corte.

def imprime_countdown(entero=100) -> int:
    if entero == 0:
        print(entero, end=""" + '"\\n"' + """)
        return entero
    print(entero, end=" - ")
    return imprime_countdown(entero - 1)
    
imprime_countdown() =>""")
imprime_countdown()
print(f"""
imprime_countdown(50) =>""")
imprime_countdown(50)
print(f"""
imprime_countdown(10) =>""")
imprime_countdown(10)

# Dificultad extra


def calcular_factorial(entero: int) -> int:
    if entero == 1:
        return 1
    else:
        return entero * calcular_factorial(entero - 1)


def calcular_fibonacci(entero: int) -> int:
    if entero == 0:
        return 0
    elif entero == 1:
        return 1
    else:
        return calcular_fibonacci(entero - 1) + calcular_fibonacci(entero - 2)


def cuantas_horas(segundos: int, horas=0, minutos=0):
    if segundos >= 3600:
        horas += segundos // 3600
        segundos -= horas * 3600
    elif 3600 > segundos >= 60:
        minutos += segundos // 60
        segundos -= minutos * 60
    elif segundos < 60:
        return f"{horas} horas, {minutos} minutos y {segundos} segundos."

    return cuantas_horas(segundos, horas, minutos)


print(f"""
Ejemplos de uso de recursividad: calculo de factorial, buscar pocisiones en la serie de Fibonacci o calcular cuantas horas son n segundos:
""")

print(f"El factorial de 5 es {calcular_factorial(5)}")
print(f"La décima posición en la serie de Fibonacci es {calcular_fibonacci(10)}")
print(f"9378 segundos son {cuantas_horas(9378)}")
