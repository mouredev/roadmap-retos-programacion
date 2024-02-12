public class Pakiuh {
    public static void main(String[] args) {
        // Operadores aritméticos
        int a = 10;
        int b = 20;
        System.out.println("a + b = " + (a + b)); // Suma
        System.out.println("a - b = " + (a - b)); // Resta
        System.out.println("a * b = " + (a * b)); // Multiplicación
        System.out.println("b / a = " + (b / a)); // División
        System.out.println("b % a = " + (b % a)); // Módulo

        // Operadores de asignación
        int c = a;
        System.out.println("c = a: " + c); // Asignación
        c += a;
        System.out.println("c += a: " + c); // Suma y asignación
        c -= a;
        System.out.println("c -= a: " + c); // Resta y asignación

        // Operadores de comparación
        System.out.println("a == b: " + (a == b)); // Igual a
        System.out.println("a != b: " + (a != b)); // No igual a
        System.out.println("a > b: " + (a > b)); // Mayor que
        System.out.println("a < b: " + (a < b)); // Menor que
        System.out.println("b >= a: " + (b >= a)); // Mayor o igual que
        System.out.println("a <= b: " + (a <= b)); // Menor o igual que

        // Estructuras de control
        // if-else
        if (a < b) {
            System.out.println("a es menor que b");
        } else {
            System.out.println("a no es menor que b");
        }

        // for loop
        for(int i = 0; i < 5; i++) {
            System.out.println("Número: " + i);
        }

        // while loop
        int i = 0;
        while(i < 5) {
            System.out.println("Número (while): " + i);
            i++;
        }

        // do-while loop
        i = 0;
        do {
            System.out.println("Número (do-while): " + i);
            i++;
        } while(i < 5);

        // try-catch
        try {
            int sum = a + b;
            if(sum > 30) {
                throw new Exception("La suma es mayor que 30");
            }
            System.out.println("La suma es: " + sum);
        } catch(Exception e) {
            System.out.println("Ha ocurrido un error: " + e.getMessage());
        } finally {
            System.out.println("Siempre se ejecuta el bloque finally");
        }

        // Imprimir números pares entre 10 y 55 que no son 16 ni múltiplos de 3
        for(i = 10; i <= 55; i++) {
            if(i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}