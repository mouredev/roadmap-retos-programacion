"""
 EJERCICIO:
 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
   que representen todos los tipos de estructuras de control que existan
   en tu lenguaje:
   Condicionales, iterativas, excepciones...
 - Debes hacer print por consola del resultado de todos los ejemplos.

 DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

 Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

print(f"{'='*10} OPERADORES {'='*40}", end="\n\n")

print(f""" Tipos de operadores:
\tde Asignación
\tde Cadena
\tAritméticos
\tLógicos
\tde Comparación
\tde Pertenencia
\tde Identidad
\tde Bits
""")

# operador de asignación -----------------------------------------------------------------------------------------------

saludo: str = "Hola"
nombre: str = "Mundo"

print("de ASIGNACIÓN")
print(f"El operador '=' se usa para asignar valores a variables: saludo => {saludo} y nombre => {nombre}")
print(f"También se lo usa en combinación con otros operadores que veremos más adelante", end="\n\n")

# operador de cadena ---------------------------------------------------------------------------------------------------

print("de CADENA")
imprimo: str = saludo + " " + nombre + "!!!"
print(f"El operador '+' concatena cadenas (aunque NO es la única forma) => saludo + nombre => {imprimo}", end="\n\n")

# operadores aritméticos -----------------------------------------------------------------------------------------------
numero_1: int = 10
numero_2: int = 3
suma = numero_1 + numero_2
resta = numero_1 - numero_2
producto = numero_1 * numero_2
division = numero_1 / numero_2
division_entera = numero_1 // numero_2
resto = numero_1 % numero_2
potencia = numero_1 ** numero_2

print("ARITMÉTICOS")
print(f"El operador '+' da la suma: {numero_1} + {numero_2} => {suma}")
print(f"El operador '-' da la resta: {numero_1} - {numero_2} => {resta}")
print(f"El operador '*' da la multiplicación: {numero_1} * {numero_2} => {producto}")
print(f"El operador '/' da el cociente: {numero_1} / {numero_2} => {division}")
print(f"El operador '//' da el cociente entero: {numero_1} // {numero_2} => {division_entera}")
print(f"El operador '%' da el resto: {numero_1} % {numero_2} => {resto}")
print(f"El operador '**' da la potencia: {numero_1} ** {numero_2} => {potencia}", end="\n\n")

# operadores de comparación --------------------------------------------------------------------------------------------

var_1: str = "1"
var_2: int = 1
verdadero: bool = (var_1 == "1")
falso: bool = (var_1 == 1)

print("de COMPARACIÓN")
print(f"El operador '==' devuelve verdadero si los comparandos son iguales, sino devuelve falso")
print(f"\t'{var_1}' == '1' => {verdadero}")
print(f"\t'{var_1}' == 1 => {falso}")

verdadero: bool = (var_2 > 0)
falso: bool = (var_2 > 5)

print(f"El operador '>' devuelve verdadero si el primer comparando es mayor que el segundo, sino devuelve falso")
print(f"\t{var_2} > 0 => {verdadero}")
print(f"\t{var_2} > 5 => {falso}")

verdadero: bool = (var_2 < 5)
falso: bool = (var_2 < 0)

print(f"El operador '<' devuelve verdadero si el primer comparando es menor que el segundo, sino devuelve falso")
print(f"\t{var_2} < 5 => {verdadero}")
print(f"\t{var_2} < 0 => {falso}")

verdadero: bool = (var_1 != var_2)
falso: bool = (var_2 != 1)

print(f"El operador '!=' devuelve verdadero si el primer comparando es distinto que el segundo, sino devuelve falso")
print(f"\t'{var_1}' != {var_2} => {verdadero}")
print(f"\t{var_2} != 1 => {falso}")

verdadero: bool = (var_2 >= 1)
falso: bool = (var_2 <= 0)

print(f"También se puede combinar '>=' (mayor o igual) o '<=' (menor o igual)")
print(f"\t{var_2} >= 1 => {verdadero}")
print(f"\t{var_2} <= 0 => {falso}", end="\n\n")

# operadores lógicos ---------------------------------------------------------------------------------------------------

verdadero: bool = (var_1 == "1" and var_2 == 1)
falso: bool = (var_1 == 1 and var_2 == "1")

print("LÓGICOS")
print(f"El operador 'and' evalúa que dos o más condiciones sean TODAs verdaderas:")
print(f"\tvar_1 == '{var_1}' and var_2 == {var_2} => {verdadero}")
print(f"\tvar_1 == {var_1} and var_2 == '{var_2}' => {falso}")

verdadero: bool = (var_1 == 7 or var_2 == 1)
falso: bool = (var_1 == 7 or var_2 == "J")

print("El operador 'or' evalúa que AL MENOS una de dos o más condiciones sea verdadera:")
print(f"\t{var_1} == 7 or {var_2} == {var_2} => {verdadero}")
print(f"\t{var_1} == 7 or {var_2} == 'J' => {falso}")

verdadero: bool = not falso
falso: bool = not verdadero

print(f"El operador 'not devuelve Verdadero si la condición es falsa y viceversa:")
print(f"\tnot falso => {verdadero}")
print(f"\tnot verdadero => {falso}", end="\n\n")

# más operadores de asignación  ----------------------------------------------------------------------------------------

print("Más sobre ASIGNACIÓN")

saludo = "Hola "
saludo += "Mundo!!!"

print(f"Con '+=' se asigna concatenando strings (saludo contiene 'Hola '): saludo += 'Mundo!!!' => {saludo}")

numero_1 = 10
numero_1 += 3

print(f"Con '+=' se asigna sumando (numero_1 contiene 10): numero_1 += 3 => {numero_1}")

numero_1 = 10
numero_1 -= 3

print(f"Con '-=' se asigna restando (numero_1 contiene 10): numero_1 -= 3 => {numero_1}")

numero_1 = 10
numero_1 *= 3

print(f"Con '*=' se asigna multiplicando (numero_1 contiene 10): numero_1 *= 3 => {numero_1}")

numero_1 = 10
numero_1 /= 3

print(f"Con '/=' se asigna dividiendo (numero_1 contiene 10): numero_1 /= 3 => {numero_1}")

numero_1 = 10
numero_1 //= 3

print(f"Con '//=' se asigna división entera (numero_1 contiene 10): numero_1 //= 3 => {numero_1}")

numero_1 = 10
numero_1 %= 3

print(f"Con '%=' se asigna el resto (numero_1 contiene 10): numero_1 %= 3 => {numero_1}")

numero_1 = 10
numero_1 **= 3

print(f"Con '**=' se asigna potencia (numero_1 contiene 10): numero_1 **= 3 => {numero_1}", end="\n\n")

# operadores de pertenencia --------------------------------------------------------------------------------------------

lista = [1, 2, 3, 4]
si_esta = 3 in lista
no_esta = 3 not in lista

print("PERTENENCIA")

print(f"Con 'in' o 'not in' valida si un determinado valor está contenido, o no, dentro de un tipo compuesto (o cadena):")
print(f"\t3 in {lista} => {si_esta}")
print(f"\t3 not in {lista} => {no_esta}")
print(f"\tl in {saludo} => {'l' in saludo}")
print(f"\tL in {saludo} => {'L' in saludo}", end="\n\n")

# operadores de identidad ----------------------------------------------------------------------------------------------

saludo_2 = saludo
saludo_identico = saludo is saludo_2

print(f"IDENTIDAD")

print("Con 'is' e 'is not' se evalúa si dos varialbes son la misma o no.")
print("Dos variables 'inmutables' (tipos primitivos y tuplas) son la misma si tienen el mismo valor.")
print("Dos variables 'mutables' (tipos compuestos excepto tupla) son la misma aún cuando una de ellas cambie.", end=" ")
print("Para que dos variables mutables sean distintas se sebe asignar una copia de una a la otra y no directamente.", end=" ")
print("Se dice que las variables 'inmutables' se pasan por 'valor' y las mutables por 'referencia'.")
print(f"\tsaludo = {saludo} / saludo_2 = {saludo_2} => saludo is saludo_2 => {saludo_identico}")

saludo_2 = saludo_2 + " :)"
saludo_identico = saludo is saludo_2

print(f"\tsaludo = {saludo} / saludo_2 = {saludo_2} => saludo is saludo_2 => {saludo_identico}")

lista_2 = lista
lista_identica = lista is lista_2

print(f"\tlista = {lista} / lista_2 = {lista_2} => lista is lista_2 => {lista_identica}")

lista_2.append(5)
lista_identica = lista is lista_2

print(f"\tlista = {lista} / lista_2 = {lista_2} => lista is lista_2 => {lista_identica}")

lista_2 = lista.copy()
lista_2.append(5)
lista_identica = lista is lista_2

print(f"\tlista = {lista} / lista_2 = {lista_2} => lista is lista_2 => {lista_identica}")

# operadodores de bits -------------------------------------------------------------------------------------------------

val_1 = 7
val_2 = 3
bit_or = val_1 | val_2
bit_xor = val_1 ^ val_2
bit_and = val_1 & val_2
bit_nor = ~val_1
bit_izquierda = val_1 << 2
bit_derecha = val_1 >> 2

print("BITS")

print(f"Los operadores operan bit a bit sobre cada una de las variables: {val_1} es '00111' y {val_2} es 00011''")
print(f"El operador '|' es un 'or': {val_1} | {val_2} => {bit_or}")
print(f"El operador '^' es un 'xor': {val_1} ^ {val_2} => {bit_xor}")
print(f"El operador '&' es un 'and': {val_1} & {val_2} => {bit_and}")
print(f"El operador '~' es un 'nor': ~{val_1} => {bit_nor}")
print(f"El operador '<<' es un 'desplazamiento a izquierda': {val_1} << 2 => {bit_izquierda}")
print(f"El operador '>>' es un 'desplazamiento a derecha': {val_1} >> 2 => {bit_derecha}", end="\n\n")


print(f"{'='*10} ESTRUCTURAS DE CONTROL {'='*40}", end="\n\n")

# control condicional --------------------------------------------------------------------------------------------------

efectivo = 100
tarjeta = 1000
gasto = 123

print(f"""Control de flujo condicional: 'if' (si algo), 'elif' (si no algo más), 'else' (si no cualquier otra cosa):
gasto = {gasto} / Límites: efectivo: {efectivo}, tarjeta: {tarjeta}, cheque: +{tarjeta} 
if gasto <= efectivo:
    print("Pago en efectivo")
elif gasto <= tarjeta:
    print("Pago con tarjeta")
else:
    print("Pago con cheque")
Pago con tarjeta
""")

edad = 21
limite = 18
control = ("Puede pasar" if edad >= limite else "No puede pasar")

print(f"""Condicional por comprehensión:
edad = {edad} / limite = {limite}
control = ("Puede pasar" if edad >= limite else "No puede pasar")
print(control) => {control}
""", end="\n\n")

musico = "Mozart"

print(f"""El control condicional 'match' (coincidir), case (ocurrencia):
musico = {musico}
match musico:
    case "Bach":
        estilo = "Barroco"
    case "Beethoven":
        estilo = "Romanticismo"
    case "Mozart":
        estilo = "Clásico"
     case _:                          # '_' indica default o else
        estilo = "Desconocido"
""")
match musico:
    case "Bach":
        estilo = "Barroco"
    case "Beethoven":
        estilo = "Romanticismo"
    case "Mozart":
        estilo = "Clásico"
    case _:
        estilo = "Desconocido"
print(f"{musico} corresponde al {estilo}", end="\n\n")

# control de flujo en bucle o iterativo --------------------------------------------------------------------------------

print("""El control 'while' se ejecuta mientras una condición dada sea verdadera:
contador = 10
while contador > 0:
    print(f"Tiempo en {contador} y contando")
    contador -= 1
print("Lanzado")
""")
contador = 10
while contador > 0:
    print(f"Tiempo en {contador} y contando")
    contador -= 1
print("Lanzado", end="\n\n")

print("""El control 'for' se ejecuta para cada uno de los elemento de un iterable:
for contador in range(10, 0, -1):
    print(f"Tiempo en {contador} y contando")
print("Lanzado")
""")
for contador in range(10, 0, -1):
    print(f"Tiempo en {contador} y contando")
print("Lanzado", end="\n\n")

# dificultad extra -----------------------------------------------------------------------------------------------------

print("""DIFICULTAD EXTRA

mi_lista = [x for x in range(10, 56) if (x % 2 == 0) and x != 16 and (x % 3 > 0)]
print(mi_lsta)
""")

mi_lista = [x for x in range(10, 56) if (x % 2 == 0) and x != 16 and (x % 3 > 0)]
print(mi_lista)
