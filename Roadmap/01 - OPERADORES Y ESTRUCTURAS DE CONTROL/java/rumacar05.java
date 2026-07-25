public class rumacar05 {
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

    public static void main(String[] args) {
        // Operadores aritméticos
        System.out.println("Suma: 4 + 5 = " + (4 + 5));
        System.out.println("Resta: 10 - 5 = " + (10 -5));
        System.out.println("Division: 4 / 2 = " + (4 / 2));
        System.out.println("Multiplicación: 8 * 2 = " + (8 * 2));
        System.out.println("Resto: 7 % 2 " + (7 % 2));

        // Operadores de comparación
        System.out.println("Igualdad: 20 == 5 es " + (20 ==5));
        System.out.println("Desigualdad: 20 != 5 es " + (20 != 5));
        System.out.println("Mayor que: 20 > 5 es " + (20 > 5));
        System.out.println("Menor que: 20 < 5 es " + (20 < 5));
        System.out.println("Mayor o igual que: 20 >= 5 es " + (20 >= 5));
        System.out.println("Menor o igual que: 20 <= 5 es " + (20 <= 5));

        // Operadores lógicos
        System.out.println("AND &&: 20 + 2 == 22 && 4 - 2 == 2 es " + (20 + 2 == 22 && 4 - 2 == 2));
        System.out.println("OR ||: 20 + 2 == 22 || 4 - 2 == 2 es " + (20 + 2 == 22 || 4 - 2 == 2));
        System.out.println("NOT !: 20 + 2 == 22 es " + !(20 + 2 == 22));

        // Operadores de asignación
        int myNumber = 10; // Asignación
        System.out.println(myNumber);
        myNumber += 2; // Suma y asignación
        System.out.println(myNumber);
        myNumber -= 4; // Resta y asignación
        System.out.println(myNumber);
        myNumber *= 4; // Multiplicación y asignación
        System.out.println(myNumber);
        myNumber /= 2; // División y asignación
        System.out.println(myNumber);
        myNumber %= 2; // Resto y asignación
        System.out.println(myNumber);

        // Operadores de bits
        int a = 5;
        int b = 3;
        System.out.println("AND: 5 & 3 = " + (a & b));
        System.out.println("XOR: 5 ^ 3 = " + (a ^ b));
        System.out.println("OR: 5 | 3 = " + (a | b));
        System.out.println("NOT: ~5 = " + (~a));
        System.out.println("Desplazamion a la izquierda: 5 << 3 = " + (5 << 3));
        System.out.println("Desplazamion a la derecha: 5 >> 3 = " + (5 >> 3));

        // Condicionales
        myNumber = 10;

        if (myNumber == 0) {
            System.out.println("myNumber es 0");
        } else if (myNumber % 2 == 0) {
            System.out.println("myNumber es par");
        } else {
            System.out.println("myNumber no es par ni 0");
        }

        // Ternarios
        System.out.println(myNumber % 2 == 0 ? "Es un número par" : "Es un número impar");

        // Iterativos
        for (int i = 0; i <= 10; i++) {
            System.out.println(i);
        }

        int i = 0;
        while (i <= 10) {
            System.out.println(i);
            i++;
        }

        i = 0;
        do {
            System.out.println(i);
            i++;
        } while (i <= 10);


        // Excepciones
        try {
            System.out.println(10 / 0);
        } catch (Exception ex) {
            System.out.println("Se ha producido una excepción");
        } finally {
            System.out.println("Ha terminado el manejo de la excepción");
        }

        // Dificultad extra
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}
