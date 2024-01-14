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

#include <stdio.h>

/* NOTA:
 * C no tiene operadores de identidad ni pertenencia ya que no existen los objetos,
 * tampoco tiene excepciones.
 */
int    main(void)
{
    /* === 1 === */
    // Operadores aritméticos
    int n1a = 27;
    int n2a = 6;
    printf("\n\tOperadores aritméticos\n");
    printf("Suma: %d + %d = %d\n", n1a, n2a, n1a + n2a); // Operador suma '+'
    printf("Resta: %d - %d = %d\n", n1a, n2a, n1a - n2a); // Operador resta '-'
    printf("Multiplicación: %d * %d = %d\n", n1a, n2a, n1a * n2a); // Operador multiplicación '*'
    printf("División: %d / %d = %d\n", n1a, n2a, n1a / n2a); // Operador división '/'
    printf("Resto: %d %% %d = %d\n", n1a, n2a, n1a % n2a); // Operador resto '%'
    printf("Post-incremento: %d++\n", n1a++); // Operador post-incremento, primero utiliza el valor y luego suma 1 al valor.
    printf("Pre-incremento: ++%d\n", ++n2a); // Operador pre-incremento, primero suma 1 al valor y luego utiliza el valor.
    printf("Post-decremento: %d--\n", n1a--); // Operador post-decremento, primero utiliza el valor y luego resta 1 al valor.
    printf("Pre-decremento: --%d\n", --n2a); // Operador pre-decremento, primero resta 1 al valor y luego utiliza el valor.

    // Operadores lógico
    int n1l = 1;
    int n2l = 0;
    printf("\n\tOperadores lógicos\n");
    printf("AND (lógico): %d && %d = %d\n", n1l, n2l, n1l && n2l); // Operador AND lógico
    printf("OR (lógico): %d || %d = %d\n", n1l, n2l, n1l || n2l); // Operador OR lógico
    printf("NOT (lógico): !%d = %d\n", n1l, !n1l); // Operador NOT lógico

    // Operadores de comparación
    int n1c = 100;
    int n2c = 105;
    printf("\n\tOperadores de comparación\n");
    printf("Menor que: %d < %d = %d\n", n1c, n2c, n1c < n2c); // Operador menor que '<'
    printf("Menor o igual que: %d <= %d = %d\n", n1c, n2c, n1c <= n2c); // Operador meno o igual que '<='
    printf("Mayor que: %d > %d = %d\n", n1c, n2c, n1c > n2c); // Operador mayor que '>'
    printf("Mayor o igual que: %d >= %d = %d\n", n1c, n2c, n1c >= n2c); // Operador mayor o igual que '>='
    printf("Igual que: %d == %d = %d\n", n1c, n2c, n1c == n2c); // Operador igual que '=='
    printf("Distinto que: %d != %d = %d\n", n1c, n2c, n1c != n2c); // Operador distinto que '!='

    // Operadores de asignación
    int x = 0;
    printf("\n\tOperador de asignación\n");
    printf("Simple: x = 2024, %d\n", x = 2024); // Operador de asignación simple '='
    printf("Suma: x += 1, %d\n", x += 1); // Operador de asignación suma '+='
    printf("Resta: x -= 1, %d\n", x -= 1); // Operador de asignación resta '-='
    printf("Multiplicación: x *= 1, %d\n", x *= 1); // Operador de asignación multiplicación '*='
    printf("División: x /= 1, %d\n", x /= 1); // Operador de asignación división '/='
    printf("Resto: x %%= 3, %d\n", x %= 3); // Operador de asignación resto '%='
    printf("AND (binario): x &= 15, %d\n", x &= 15); // Operador de asignación AND binario '&='
    printf("OR (binario): x |= 1, %d\n", x |= 1); // Operador de asignación OR binario '|='
    printf("XOR: x ^= 4, %d\n", x ^= 4); // Operador de asignación XOR '^='
    printf("Desplazamiento a la derecha: x >>= 1, %d\n", x >>= 1); // Operador de asignación desplazamiento a la derecha '>>='
    printf("Desplazamiento a la izquierda: x <<= 2, %d\n", x <<= 2); // Operador de asignación desplazamiento a la izquierda '<<='

    // Operación de bits
    int	n1b = 0b1010; // 10 en binario (1 * 2³ + 1 * 2¹ = 8 + 2 = 10)
    int	n2b = 0b1111; // 15 en binario (1 * 2³ + 1 * 2² + 1 * 2¹ + 1 * 2⁰ = 8 + 4 + 2 + 1 = 15)
    printf("\n\tOperadores de bits\n");
    printf("AND (binario): %d & %d = %d\n", n1b, n2b, n1b & n2b); // Operador AND binario. 00001010 & 00001111 pasa a ser 00001010
    printf("OR (binario): %d | %d = %d\n", n1b, n2b, n1b | n2b); // Operador OR binario. 00001010 | 00001111 pasa a ser 00001111
    printf("NOT (binario): ~%d = %d\n", n1b, ~n1b); // Operador NOT binario. ~00001010 pasa a ser 11110101
    printf("XOR: %d ^ %d = %d\n", n1b, n2b, n1b ^ n2b); // Operador XOR binario. 00001010 ^ 00001111 pasa a ser 00000101
    printf("Desplazamiento a la derecha (bits): %d >> 1 = %d\n", n1b, n1b >> 1); // Desplazamiento a la derecha. 00001010 pasa a ser 00000101, que es 5 en binario.
    printf("Desplazamiento a la izquierda (bits): %d << 1 = %d\n", n1b, n1b << 1); // Desplazamiento a la izquierda. 00001010 pasa a ser 00010010, que es 20 en binario.

    /* === 2 === */
    // Condicional if, else if, else
    /* La estructura es:
     * if (condición) { código }
     * else if (condición) { código }
     * else { código }*/
    int	temp = 0;
    printf("\n\tCondicional if, else if, else\n");
    if (temp < 2)
    {
        // Si 5 es menor que 2 se mete aquí
        printf("%d es menor que 2\n", temp);
    }
    else if (temp == 0)
    {
        // Sino si 5 es igual a 0 se mete aquí
        printf("%d es igual a 0\n", temp);
    }
    else
    {
        // Sino se mete aquí
        printf("%d no es menor que 2 ni tampoco es igual a 0\n", temp);
    }

    // Condicional switch
    /* Se suele utilizar cuando una condición puede tomar varios valores.
     * Por ejemplo, un menú puede tener 10 opciones, y tener que utilizar
     * tantos if, else if, else puede resultar tedioso.
     * La estructura es:
     * switch (variable)
     * {
     *     case <valor de la variable>:
     *          código
     *          break;
     *     default:
     *          código
     *          break;
     * }
     * 
     * NOTA: El break sirve para que no se ejecute la siguiente condición.
     */
    printf("\n\tCondicional switch\n");
    switch (temp)
    {
        case 1:
            printf("%d es 1\n", temp);
            break;
        case 2:
        case 3:
            printf("%d es 2 o 3\n", temp);
            break;
        default:
            printf("%d no es ni 1, ni 2 y tampoco es 3\n", temp);
            break;
    }

    // Bucle while
    /* Es el bucle más simple, con este se pueden hacer
     * los demás.
     * La estructura es:
     * while (condicion) { código }
     */
    printf("\n\tBucle while\n");
    temp = 10;
    while (temp-- > 0)
    {
        if (temp != 0)
            printf("%d, ", temp);
        else
            printf("%d\n", temp);
    }

    // Bucle for
    /* Es el bucle más sencillo de utilizar.
     * La estructura es:
     * for (variable; condición; modificación de la variable) { código }
     */
    printf("\n\tBucle for\n");
    for (int i = 0; i < 100; i += 10)
    {
        printf("%d ", i);
    }
    printf("\n");

    // Bucle do while
    /* Es como el while, pero la condición la verifica al final
     * por lo tanto el código se ejecuta al menos una vez.
     * La estructura es:
     * do { código } while (condición);
     */
    printf("\n\tBucle do while\n");
    temp = 200;
    do
    {
        if (temp > 100)
            temp = 10;
        printf("%d ", temp);
        temp += 11;
    } while (temp < 100);
    printf("\n");

    /* === DIFICULTAD EXTRA === */
    printf("\n\tDificultad extra\n");
    for (int i = 10; i < 56; i++) // Para i igual a 10, menor que 56, aumenta i en uno.
        if (i % 2 == 0 && i != 16 && i % 3 != 0) // Si el resto de i / 2 (i % 2) es igual a 0 (es par), no es igual a 16 y el resto de i / 3 (i % 3) no es igual a 0.
            printf("%d ", i); // Imprime i.
    printf("\n");
    /* NOTA:
     * En la sección 2, if (anidación == 1), no es necesario poner llaves,
     * siempre y cuando se ponga la tabulación adecuada, else, hay que ponerlo.
     * Por eso en el código he podido anidar dentro del for, un if y luego
     * hacer el printf, sin necesidad de utilizar llaves.
     */
    return (0);
}
