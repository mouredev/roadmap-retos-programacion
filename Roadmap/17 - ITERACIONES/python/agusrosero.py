"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""

# EJERCICIO:
# 1.
for i in range(1, 11):
    print(i)

# 2.
i = 1
j = 10
while i <= j:
    print(i)
    i += 1

# 3.


def iteracion(i=1):
    if i <= 10:
        print(i)
        iteracion(i + 1)


iteracion()

# DIFICULTAD EXTRA:
fruits_list = ["Apple", "Mango", "Peach", "Orange", "Banana"]

for fruit in fruits_list:
    print(fruit)

fruits_tuple = ("Apple", "Mango", "Peach", "Orange", "Banana")

for fruit in fruits_tuple:
    print(fruit)

fruits_set = {"Apple", "Mango", "Peach", "Orange", "Banana"}

for fruit in fruits_set:
    print(fruit)

string = "Hernan"

for char in string:
    print(char)

countries_capital = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Egypt": "Cairo",
    "Japan": "Tokyo"
}

for country in countries_capital.keys():
    print(country)
