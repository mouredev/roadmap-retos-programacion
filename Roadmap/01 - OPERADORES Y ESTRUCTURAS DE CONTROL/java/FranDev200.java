public class FranDev200 {

    static void main() {

        System.out.println("===== OPERADORES =====");

        // ---------------- ARITMÉTICOS ----------------
        int a = 10, b = 3;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));
        System.out.println("Incremento: " + (++a));
        System.out.println("Decremento: " + (--b));

        // ---------------- COMPARACIÓN ----------------
        System.out.println("a == b: " + (a == b));
        System.out.println("a != b: " + (a != b));
        System.out.println("a > b: " + (a > b));
        System.out.println("a < b: " + (a < b));
        System.out.println("a >= b: " + (a >= b));
        System.out.println("a <= b: " + (a <= b));

        // ---------------- LÓGICOS ----------------
        boolean x = true, y = false;
        System.out.println("x && y: " + (x && y));
        System.out.println("x || y: " + (x || y));
        System.out.println("!x: " + (!x));

        // ---------------- ASIGNACIÓN ----------------
        int c = 5;
        c += 3;
        System.out.println("c += 3 → " + c);
        c -= 2;
        System.out.println("c -= 2 → " + c);
        c *= 2;
        System.out.println("c *= 2 → " + c);
        c /= 2;
        System.out.println("c /= 2 → " + c);

        // ---------------- IDENTIDAD ----------------
        String s1 = new String("Hola");
        String s2 = new String("Hola");
        System.out.println("s1 == s2: " + (s1 == s2));
        System.out.println("s1.equals(s2): " + s1.equals(s2));

        // ---------------- PERTENENCIA (instanceof) ----------------
        Object obj = "Texto";
        System.out.println("obj instanceof String: " + (obj instanceof String));

        System.out.println("\n===== ESTRUCTURAS DE CONTROL =====");

        // ---------------- CONDICIONALES ----------------
        int numero = 7;

        if (numero > 5) {
            System.out.println("If: El número es mayor que 5");
        } else {
            System.out.println("If: El número no es mayor que 5");
        }

        if (numero > 10) {
            System.out.println("Else if: Mayor que 10");
        } else if (numero > 5) {
            System.out.println("Else if: Mayor que 5");
        } else {
            System.out.println("Else if: Menor o igual a 5");
        }

        switch (numero) {
            case 1:
                System.out.println("Switch: número 1");
                break;
            case 7:
                System.out.println("Switch: número 7");
                break;
            default:
                System.out.println("Switch: otro número");
        }

        // ---------------- ITERATIVAS ----------------
        System.out.println("\nFor:");
        for (int i = 0; i < 3; i++) {
            System.out.println("i = " + i);
        }

        System.out.println("\nWhile:");
        int j = 0;
        while (j < 3) {
            System.out.println("j = " + j);
            j++;
        }

        System.out.println("\nDo-While:");
        int k = 0;
        do {
            System.out.println("k = " + k);
            k++;
        } while (k < 3);

        System.out.println("\nFor-each:");
        int[] array = {1, 2, 3};
        for (int valor : array) {
            System.out.println("valor = " + valor);
        }

        // ---------------- EXCEPCIONES ----------------
        System.out.println("\nExcepciones:");

        try {
            int resultado = 10 / 0;
            System.out.println(resultado);
        } catch (ArithmeticException ex) {
            System.out.println("Error: División por cero");
        } finally {
            System.out.println("Bloque finally ejecutado");
        }

        // ---------------- CONTROL DE SALTO ----------------
        System.out.println("\nBreak y Continue:");

        for (int i = 0; i < 5; i++) {
            if (i == 2) continue;
            if (i == 4) break;
            System.out.println("i = " + i);
        }

        System.out.println("** EJERCICIO EXTRA **");

        for(int i = 10; i <= 55; i++){

            if( (i%2) == 0 && (i%3) != 0 && i != 16){
                System.out.println(i);
            }

        }

    }

}
