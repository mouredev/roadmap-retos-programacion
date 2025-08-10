# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
#### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

suma = 5 + 4;
resta = 8 -5;
multiplicacion = 3 * 4;
division = 10 / 2;
restante = 10 % 3;
potencia = 8**7;
divison_enteros = 25//4;

mayor = 30 > 18;
menor = 12 > 20;
igual = 20 == 20;
menor_igual = 10<=15;
mayor_igual = 20>=20;
no_iguales = 10 !=  12;

#operadores bit a bit
a = 10 #1010
b = 4  #0100        
and_bit = a & b #0000
or_bit = a | b  #1110
xor_bit = a ^ b #1110
not_bit = ~a    #-1011
desplazar_izquierda = a << 2 #101000
desplazar_derecha = a >> 2   #0010  

#operadores logicos
and_logico = (5 > 2) and (3 < 4);
or_logico = (5 > 2) or (3 > 4);
not_logico = not(5 > 2);        

#operadores de asignacion
x = 5;
x += 3; #x = x + 3
x -= 2; #x = x - 2          
x *= 2; #x = x * 2
x /= 2; #x = x / 2
x %= 3; #x = x % 3
x //= 2; #x = x // 2
x **= 3; #x = x ** 3

#operadores de pertenencia
pertenencia1 = 'a' in 'manzana';
pertenencia2 = 'b' not in 'manzana';        
#operadores de identidad
y = 10;
identidad1 = y is 10;
identidad2 = y is not 10;   


print("Operadores Aritméticos")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Restante: {restante}")
print(f"Potencia: {potencia}")
print(f"División de enteros: {divison_enteros}")
print("\nOperadores de Comparación")
print(f"Mayor que: {mayor}")            

