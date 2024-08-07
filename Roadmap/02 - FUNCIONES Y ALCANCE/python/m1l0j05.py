"""
Explicacion teorica:

En programación, una función es una secuencia de declaraciones que realizan una tarea específica, agrupada bajo un nombre. 
Las funciones son fundamentales para la organización y reutilización del código. 
En Python, una función se define con la palabra clave def, seguida de un nombre de función, paréntesis (que pueden incluir argumentos) y dos puntos. 
El cuerpo de la función sigue en líneas indentadas.

El alcance de una función se refiere a la visibilidad de las variables y otros objetos dentro de esa función. 
En Python, el alcance se maneja con las reglas LEGB, que describen la secuencia en la que se buscan los nombres:
    Local (L): Nombres asignados dentro de una función. No son visibles fuera de la función.
    Enclosing (E): Nombres en el ámbito local de todas las funciones envolventes (de "afuera hacia adentro"), si existen.
    Global (G): Nombres asignados en el nivel superior de un módulo o declarados globalmente en una función.
    Built-in (B): Nombres preasignados en Python (como print, len).
"""
# Ejemplo de la teoria:
x = "global x"  # Global scope

def test():
    y = "local y"  # Local scope
    print(y)
    print(x)  # Accede a la variable global x

test()
# print(y)  # Esto generaría un error, ya que y es local a la función test

# Ejercicios:

def my_fuction():
    print('Hello World!')

def my_fuction_inside():
    x_local = 'Hello World!'
    def inside():
        print(x_local)
    inside()

my_fuction()
my_fuction_inside()

print(f'The length of the variable is: {len(x)}' )

print(x)
#print(x_local) # Descomentar para ver el error que genera al no estar dispnible la variable de forma global.
print('The variable x is global and the x_local is local')


# Ejercicio Extra:
print('\n[+] Ejercicio extra:\n')

def fizzBuzz(word_1, word_2):
    for i in range(1, 101):
        output = ''
        if i % 3 == 0:
            output += word_1
        if i % 5 == 0:
            output += word_2
        if not output:
            output = str(i)
        print(output)

word_1 = 'Fizz'
word_2 = 'Buzz'

fizzBuzz(word_1, word_2)
