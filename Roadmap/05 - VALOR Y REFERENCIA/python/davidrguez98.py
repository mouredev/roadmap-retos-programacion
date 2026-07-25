""" # #05 VALOR Y REFERENCIA
> #### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

```
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**. """

# Tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
""" my_int_a = 30 """
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

#Funciones de datos por valor

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia

my_list_c = [10, 20]

def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_func(my_list_c)
print(my_list_c)

#DIFICULTAD EXTRA

#Por valor
int_a = 10
int_b = 20

def value(value_a: int, value_b: int):
    value_a = int_b
    value_b = int_a
    print(value_a, value_b)

value(int_a, int_b)
print(int_a, int_b)

#Por referencia
list_a = [10, 20]
list_b = [30, 40]

def value2(value_la: list, value_lb: list):
    value_la = list_b
    value_lb = list_a
    value_la.append(50)
    value_lb.append(60)
    print(value_la, value_lb)

value2(list_a, list_b)
print(list_a, list_b)
