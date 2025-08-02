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
    public static void main(String[] arg) {

        // ASIGNACIÓN
        int a = 5;
        int b = 10;
        System.out.println(a += 2);
        System.out.println(a -= 2);
        System.out.println(a /= 2);
        System.out.println(a *= 2);
        System.out.println(++a);
        System.out.println(--a);

        // ARITMÉTICOS
        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);

        // RELACIONALES
        System.out.println(a == b);
        System.out.println(a <= b);
        System.out.println(a >= b);
        System.out.println(a < b);
        System.out.println(a > b);
        System.out.println(a != b);


        // LÓGICOS
        System.out.println(a + a == b && b - a == a);
        System.out.println(a + a == b || b - a == a);
        System.out.println(a + a == b & b - a == a);
        System.out.println(a + a == b | b - a == a);
        System.out.println(!(a + a == b || b - a == a));

   /*
   ESTRUCTURAS SELECTIVAS
   */

        // CICLO IF

        if (a > b) {
            System.out.println("La variable A es igual a: " + a);
            System.out.println("La variable B es igual a: " + b);
            System.out.println("La variable A es mayor que B");
        }

        // CICLO ELSE IF
        else if (a == b) {
            System.out.println("Las variables A y B son iguales");
        }

        // CICLO ELSE
        else {
            System.out.println("La variable A es igual a: " + a);
            System.out.println("La variable B es igual a: " + b);
            System.out.println("La variable B es mayor que A");
        }

        // CICLO SWITCH

        switch (a) {
            case 1:
                System.out.println("La variable A es igual a 1");
                break;
            case 2:
                System.out.println("La variable A es igual a 2");
                break;
            case 3:
                System.out.println("La variable A es igual a 3");
                break;
            case 4:
                System.out.println("La variable A es igual a 4");
                break;
            case 5:
                System.out.println("La variable A es igual a 5");
                break;
            case 6:
                System.out.println("La variable A es igual a 6");
                break;
            case 7:
                System.out.println("La variable A es igual a 7");
                break;
            default:
                System.out.println("La variable A es mayor a 7");
                break;
        }


    /*
   ESTRUCTURAS REPETITIVAS
   */

        //ESTRUCTURA WHILE

        while (b == 10) {
            System.out.println("La variable B es igual a: " + b);
            --b;

        }


        //ESTRUCTURA DO-WHILE

        do {
            System.out.println("La variable A es igual a: " + a + " y es mayor que 0");
            a--;
        } while (a > 0);


        //ESTRCUTURA FOR
        for (a = 0; a < 5; a++) {
            System.out.println("La variable a es igual a: " + a + " y es menor a 5");
        }

        // EJERCICIO EXTRA
        int c = 10;
        for (c = 10; c >= 10 && c <= 55; c++) {
            if (c % 2 == 0 && c % 3 != 0 && c != 16) {
                System.out.println(c);
            }

        }

    }
}