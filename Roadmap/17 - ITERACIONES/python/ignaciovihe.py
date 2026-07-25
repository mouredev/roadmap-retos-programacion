"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
"""

#FOR

for i in range(1,11):
    print(i)


#WHILE

i=1
while i < 11:
    print(i)
    i += 1


#RECURSIVIDAD

def increment(i = 1):
    if i < 11:
        print(i)
        increment(i + 1)
        
increment()


"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

#1 For con set

languages = {"python", "javascript", "html", "css"}
for language in languages:
    print(language)


#2 For con tupla

languages = ("python", "javascript", "html", "css")
for language in languages:
    print(language)


#3 For con lista

languages = ["python", "javascript", "html", "css"]
for language in languages:
    print(language)


#4 for con dict

languages = {"1": "python", "2": "javascript", "3": "html", "4": "css"}
for language in languages:
    print(language)


#5 for con dict y values

languages = {"1": "python", "2": "javascript", "3": "html", "4": "css"}
for language in languages.values():
    print(language)


#5 for con dict y enumerate

languages = {"1": "python", "2": "javascript", "3": "html", "4": "css"}
for key, value in languages.items():
    print(f"{key}: {value}")


#6 while

languages = ["python", "javascript", "html", "css"]
while languages:
    print(languages.pop(0))


#7 For con enumerate

languages = ["python", "javascript", "html", "css"]
for index, language in enumerate(languages):
    print(f"{index} : {language}")


#8 Generador y print

print(*[i for i in range(1, 11)], sep="\n")


#9 Str

my_str = "Hello Python"
for char in my_str:
    print(char)


#10 intertools-cycle

from itertools import cycle

colors = ["red", "yellow", "green"]
cicle = cycle(colors)
for i in range(9):
    print(next(cicle))

