public class EspinoLeandroo {
    public static void main(String[] args) {
        // Operadores Aritméticos
        int a = 10, b = 5;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));

        // Operadores de Comparación
        System.out.println("Igual a: " + (a == b));
        System.out.println("No igual a: " + (a != b));
        System.out.println("Mayor que: " + (a > b));
        System.out.println("Menor que: " + (a < b));
        System.out.println("Mayor o igual que: " + (a >= b));
        System.out.println("Menor o igual que: " + (a <= b));

        // Operadores Lógicos
        boolean x = true, y = false;
        System.out.println("AND lógico: " + (x && y));
        System.out.println("OR lógico: " + (x || y));
        System.out.println("NOT lógico: " + (!x));

        // Operadores de Asignación
        int c = 15;
        c += 5; // Equivalente a c = c + 5
        System.out.println("Operador de Asignación: " + c);

        // Estructuras de Control Condicionales
        if (a > b) {
            System.out.println("a es mayor que b");
        } else if (a < b) {
            System.out.println("a es menor que b");
        } else {
            System.out.println("a es igual a b");
        }

        // Estructuras de Control Iterativas
        System.out.println("Bucle For:");
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }

        System.out.println("Bucle While:");
        int contador = 0;
        while (contador < 5) {
            System.out.println(contador);
            contador++;
        }

        // Estructuras de Control de Excepciones
        try {
            int resultado = a / 0; // División por cero, lanza ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("¡Error! División por cero.");
        }

        // Opcional
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}
