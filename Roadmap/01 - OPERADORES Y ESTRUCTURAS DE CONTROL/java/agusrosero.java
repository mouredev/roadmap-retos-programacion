public class agusrosero {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        boolean c = true;
        boolean d = false;

        // aritméticos
        var suma = a + b;
        var resta = a - b;
        var multiplicacion = a * b;
        var division = a / b;
        var modulo = a % b;

        // lógicos
        var or = c || d;
        var and = c && d;
        var not = !c;

        // comparación
        var igual = a == b;
        var mayor = a > b;
        var mayorIgual = a >= b;
        var menor = a < b;
        var menorIgual = a <= b;

        // asignación
        a += b;
        a -= b;
        a /= b;
        a *= b;
        a %= b;

        // estructuras de control
        int number = 10;

        for (int i = 0; i < number; i++) {
            System.out.println(i);
        }

        if (number == 10) {
            System.out.println("Numero 10!");
        } else {
            System.out.println("No es numero 10.");
        }

        switch (number) {
            case 10:
                System.out.println("Numero 10!");
                break;
            default:
                System.out.println("Se ejecuto correctamente...");
                break;
        }

        while (number <= 10) {
            System.out.println(number++);
        }

        do {
            System.out.println("Ejecutando 10 veces...");
            number++;
        } while (number <= 20);

        // DIFICULTAD EXTRA (opcional):
        /*
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}
