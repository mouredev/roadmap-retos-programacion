/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 *
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 *
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

public class Gerthai08 {
    public static void main (String[] arg){

        //Operadores Aritméticos
        int suma1 = 100 + 200;
        int resta1 = suma1 - 100;
        double suma2 = resta1 * 3;
        ++suma2;
        --suma1;
        int porcentaje = 100 % 10;
        double divicion = 10 / 5;

        //Operadores Logicos
        System.out.println(suma1 > 100 && 100 < suma2);
        System.out.println(suma1 > 100 || 100 < suma2);
        System.out.println(!(suma1 > 100 || 100 < suma2));

        //Operadores de Comparación
        int x = 5;
        int y = 6;
        System.out.println(x > y);

        //Operadores de Asignación
        x = 5;
        x += 5;
        x -=5;
        x /= 5;
        x %= 5;
        x &= 5;
        x |= 5;
        x ^= 5;
        x >>= 5;
        x <<= 5;





    }
}
