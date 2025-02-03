# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

num_1 = int(input("Dame un numero: "))
num_2 = int(input("Dame otro numero: "))

operacion = int(input("Que operacion quieres realizar? \n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Division \n"))

suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2
division = num_1 / num_2

if operacion == 1:
    print(f"El resultado de la suma es: {suma}")
elif operacion == 2:
    print(f"El resultado de la resta es: {resta}")
elif operacion == 3:
    print(f"El resultado de la multiplicacion es: {multiplicacion}")
elif operacion == 4:
    print(f"El resultado de la division es: {division}")
else:
    print("No se ha realizado ninguna operacion")
    
