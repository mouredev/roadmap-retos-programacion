/** #01 - Java -> h4ckxel */

public class h4ckxel {
    public static void main(String[] args) {
    System.out.println("---EJERCIÓ---\n");
        /*
         * ARITMÉTICAS
         * Se utilizan para realizar cálculos matemáticos.
         */

        int a = 10;
        int b = 5;

        System.out.println("---Operaciones Aritméticas---\n");

        System.out.println("a:" + a);
        System.out.println("b:" + b);
        System.out.println("\nSuma: a + b = " + (a + b)); // Suma
        System.out.println("Resta: a - b = " + (a - b)); // Resta
        System.out.println("Multiplicar: a * b = " + (a * b)); // Multiplicar
        System.out.println("Exponente a ^ b" + (a ^ b));
        System.out.println("Division: a / b = " + (a / b)); // Division
        System.out.println("Modulo: a % b =" + (a % b)); // Modulo

        /*
         * ASIGNACIONES
         * Se utilizan para asignar valores a las variables.
         */

        System.out.println("\n---Operaciones Asignación---\n");
        
        int c = 10; // Asignación simple
        c += 5; // Suma y asigna
        c -= 3; // Resta y asigna
        c *= 2; // Multiplica y asigna
        c /= 4; // Divide y asigna
        c %= 3; // Calcula el modulo y asigna
        System.err.println("Asignación simple: c = 5 - 10");
        System.err.println("Suma y asigna: c += 5 - 15");
        System.err.println("Suma y asigna: c -= 3 - 12");
        System.err.println("Suma y asigna: c *= 2 - 24");
        System.err.println("Suma y asigna: c /= 4 - 6");
        System.err.println("Suma y asigna: c %= 3 - 0");
        System.out.println("Resultado de Agnación: " + c);

        /*
         * RELACIONALES
         * Se utilizan para comparar dos valores.
         */

        System.out.println("\n---Operaciones Relacional---\n");

        int x = 10;
        int y = 20;

        System.out.println("Es Igual: x == y - " + (x == y));
        System.out.println("Es Diferente: x != y - " + (x != y));
        System.out.println("Es Mayor: x > y - " + (x > y));
        System.out.println("Es Menor: x < y - " + (x < y));
        System.out.println("Es Mayor o Igual: x >= y - " + (x >= y));
        System.out.println("Es Menor o Igual: x <= y - " + (x <= y));

        /*
         * LÓGICOS
         * Se utilizan para combinar expresiones booleanas.
         */

        System.out.println("\n---Operaciones Lógicos---\n");

        boolean i = true;
        boolean k = false;

        System.out.println("Operador i && k: " + (i && k));
        System.out.println("Operador i || k: " + (i || k));
        System.out.println("Operador !k: " + (!k));

        /*
         * UNARIAS
         * Se aplican a un solo operando.
         */

        System.out.println("\n---Operaciones Unarias---\n");
        
        int d = 5;
        System.out.println("Incremento: " + d++);
        System.out.println("Decremento: " + d--);
        System.out.println("Negativo: " + (-d));
        System.out.println("Positivo: " + (+d));

        /*
         * BIT A BIT
         * Se utilizan para realizar operaciones a nivel de bits.
         */

        System.out.println("\n---Operaciones Unarias---\n");

        int e = 6;
        int f = 3;
        System.out.println("AND bir a bit: e & f - " + (e & f));
        System.out.println("OR bir a bit: e | f - " + (e | f));
        System.out.println("XOR bir a bit: e ^ f - " + (e ^ f));
        System.out.println("Complemento bir a bit: ~e - " + (~e));
        System.out.println("Desplazamiento a la izquierda: e << f - " + (e << f));
        System.out.println("Desplazamiento a la derecha: e >> f - " + (e >> f));
        System.out.println("Desplazamiento a la derecha sin singo: e >>> f - " + (e >>> f));

        
    /*
    * Estructuras de controles
    */

        /*
         * IF - ELSE If - ELSE
         */
        System.out.println("\n---Estructuras de controles---\n");

        System.out.println("\nSentiría IF-ELSE IF-ELSE");
        int num = 10;
        if (num > 0) {
            System.out.println("El número es Positivo");
        } else if (num < 0) {
            System.out.println("El número es Negativo");
        } else {
            System.out.println("El número es Cero");
        }
        
        /*
         * SWITCH
         */
        System.out.println("\nSentiría SWITCH");
        int day = 3;
        switch (day) {
            case 1:
                System.out.println("Lunes");
                break;
            case 2:
                System.out.println("Martes");
                break;
            case 3:
                System.out.println("Miércoles");
                break;
            default:
                System.out.println("Otro dia");
                break;
        }

        /*
         * FOR
         */
        System.out.println("\nBucle FOR");
        for (int j = 0; j < 5; j++) {
            System.out.println("Iteración: " + j);
        }

        /*
         * WHILE
         */
        System.out.println("\nBucle WHILE");
        int g = 0;
        while (g < 5) {
            System.out.println("Iteración: " + g);
            g++;
        }

        /*
         * DO-WHILE
         */
        System.out.println("\nBucle DO-WHILE");
        int l = 0;
        do {
            System.out.println("Iteración: " + l);
            l++;
        } while (l < 5);

        /*
         * TRY-CATCH-FINALLY
         */
        System.out.println("\nBucle TRY-CATCH-FINALLY");
        try {
            int division = 10 / 0;
            System.out.println(division);
        } catch (ArithmeticException error) {
            System.out.println("Error: Division por cero");
        } finally{
            System.out.println("Este bloque se ejecuta siempre");
        }

    /**-----DIFICULTAD EXTRA-----*/

        System.out.println("\n-----EXTRA-----\n");

        for(int m = 10; m < 55; m++){
            if ((m % 2 == 0) && (m != 16) && (m % 3 == 0)) {
                System.out.println(m);
            }
        }

    /**-----DIFICULTAD EXTRA-----*/
    }
}