public class Jony_English22 {

    public static void main(String[] args) {

        //Operadores Artmeticos
        System.out.println("10 + 4 = " + (10 + 4));
        System.out.println("10 - 4 = " + (10 - 4));
        System.out.println("10 * 4 = " + (10 * 4));
        System.out.println("10 / 4 = " + (10 / 4));
        System.out.println("10 % 4 = " + (10 % 4));

        //Operadores logicos
        boolean x = true;
        boolean y = false;
        System.out.println("AND Lógico: " + (x && y));
        System.out.println("OR Lógico: " + (x || y));
        System.out.println("NOT Logico: " + (!x));

        //Operador de asignación
        int num = 15;
        System.out.println(num);
        num += 5;
        System.out.println(num);
        num -= 5;
        System.out.println(num);
        num *= 2;
        System.out.println(num);
        num /= 2;
        System.out.println(num);
        num %= 3;
        System.out.println(num);

        //Operadores de comparación
        System.out.println("10 > 5 = " + (10 > 5));
        System.out.println("10 < 5 = " + (10 < 5));
        System.out.println("5 >= 3 = " + (5 >= 3));
        System.out.println("5 <= 3 = " + (5 <= 3));
        System.out.println("10 == 20 = " + (10 == 20));
        System.out.println("20 != 10 = " + (20 != 10));

        //Operadores unarios
        int valor = 3;
        System.out.println(+valor);
        System.out.println(-valor);

        //Operadores de incremento y decremento
        System.out.println(++num);
        System.out.println(--num);

        //Operadores de bits
        int a = 5;  // Representación binaria: 0101
        int b = 3;  // Representación binaria: 0011
        System.out.println("AND a nivel de bits " + (a & b));
        System.out.println("OR a nivel de bits " + (a | b));
        System.out.println("XOR a nivel de bits " + (a ^ b));
        System.out.println("NOT a nivel de bits " + (~a));
        System.out.println("Desplazamiento a la izquierda: " + (a << 2));
        System.out.println("Desplazamiento a la derecha: " + (a >> 2));
        System.out.println("Desplazamiento a la derecha sin signo: " + (a >>> 2));

        /*
          Estructuras de control
         */

        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }

        int j = 11;

        if (j > 5) {
            System.out.println("Hola Java");
        } else {
            System.out.println("Hola Mundo");
        }

        String luz = "Amarillo";

        if (luz == "Verde") {
            System.out.print("Puede Continiue");
        } else if (luz == "Amarillo") {
            System.out.println("Alto parcial");
        } else {
            System.out.println("Alto total");
        }

        int n = 2;

        switch(n) {
            case 0:
                System.out.println("n es cero.");
                break;
            case 1:
                System.out.println("n es uno.");
                break;
            case 2:
                System.out.println("n es dos.");
                break;
            case 3:
                System.out.println("n es tres.");
                break;
            default:
                System.out.println("n es mayor a tres.");
        }

        int contador = 1;
        while (contador <= 5) {
            System.out.println(contador);
            contador++;
        }

        int m = 1;
        do {
            System.out.println(m);
            m++;
        } while (m <= 3);

        try {
            System.out.println(10/ 0);
        } catch (ArithmeticException e) {
            System.out.println("Error");
        } finally {
            System.out.println("Continue con el programa");
        }

        /*
         * Dificultad Extra:
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        for (int i = 10; i <= 55; i++) {
            if ((i % 2 == 0 && i == 55) || (i != 16 && i % 3 != 0)) {
                System.out.println(i);
            }
        }
    }
}
