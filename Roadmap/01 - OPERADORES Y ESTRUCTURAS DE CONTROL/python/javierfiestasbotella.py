'''EJERCICIO:
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
 */'''

for i in range(10,56):
    if i%2==0 and i!=16 and i%3!=0:
        print(i)

a=1
b=2
c=3

if a>b:
    print(f'{a} es mayor a {b}')
elif a<b:
        print(f'{b} es mayor a {a}')
else:
     print(f'{a} y {b} son iguales')

print(f'asi se imprime boleano si le digo que b es par de la manera\n b%2==0 me imprime: {b%2==0}')
print(f'si divido dos numeros enteros me da un numero float que representaré imprimiendo el tipo con type(b/2): {type(b/2)}')