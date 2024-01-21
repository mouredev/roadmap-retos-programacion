public class Main {

    public static void main(String[] args) {
        operadoresAritmeticos();
        operadoresLogicos();
        operadoresComparacion();
        operadoresAsignacion();
        operadoresUnarios();
        operadoresBits();

        System.out.println("Estructuras de control");

        System.out.println("if");
        int n1 = 10;
        int n2 = 20;
        // Verifica si n1 es mayor a n2
        if (n1 > n2) {
            System.out.println("n1 es mayor a n2");
        }
        System.out.println("Estructura if-else");
        // Verifica si n1 es mayor a n2
        if (n1 > n2) {
            System.out.println("n1 es mayor a n2");
        } else {
            System.out.println("n1 es menor o igual a n2");
        }
        System.out.println("Estructura if-else if-else");
        // Verifica si n1 es mayor a n2
        if (n1 > n2) {
            System.out.println("n1 es mayor a n2");
        } else if (n1 < n2) {
            System.out.println("n1 es menor a n2");
        } else {
            System.out.println("n1 es igual a n2");
        }

        System.out.println("switch");
        int dia = 1;
        // Verifica el valor de la variable dia
        switch (dia) {
            case 1:
                System.out.println("Lunes");
                break;
            case 2:
                System.out.println("Martes");
                break;
            default:
                System.out.println("No es lunes ni martes");
                break;
        }

        System.out.println("while");
        int i = 0;
        // Mientras i sea menor a 10
        while (i < 10) {
            System.out.println("i = " + i);
            i++;
        }

        System.out.println("do-while");
        int j = 0;
        // Mientras j sea menor a 10
        do {
            System.out.println("j = " + j);
            j++;
        } while (j < 10);

        System.out.println("for");
        // Mientras i sea menor a 10
        for (int k = 0; k < 10; k++) {
            System.out.println("k = " + k);
        }

        System.out.println("for-each");
        // Crea un arreglo de números
        int[] numeros = {1, 2, 3, 4, 5};
        // Recorre el arreglo de números
        for (int numero : numeros) {
            System.out.println("numero = " + numero);
        }

        System.out.println("break");
        // Mientras i sea menor a 10
        for (int k = 0; k < 10; k++) {
            // Si k es igual a 5
            if (k == 5) {
                // Detiene el ciclo
                break;
            }
            System.out.println("k = " + k);
        }

        System.out.println("continue");
        // Mientras i sea menor a 10
        for (int k = 0; k < 10; k++) {
            // Si k es igual a 5
            if (k == 5) {
                // Continua con la siguiente iteración
                continue;
            }
            System.out.println("k = " + k);
        }

        // Control de excepciones
        System.out.println("Control de excepciones");
        try {
            // Intenta ejecutar el código
            int resultado = 10 / 0;
            System.out.println("resultado = " + resultado);
        } catch (Exception e) {
            // Si ocurre una excepción, ejecuta el código
            System.out.println("Ocurrió un error");
        } finally {
            // Siempre se ejecuta el código
            System.out.println("Se ejecuta el finally");
        }

        /**
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        for (int k = 10; k <= 55 ; k++) {
            if (k % 2 == 0 && k != 16 && k % 3 != 0) System.out.println("k = " + k);
        }
    }

    static void operadoresAritmeticos() {
        System.out.println("Operadores aritméticos");
        int n1 = 10;
        int n2 = 5;
        // Suma dos valores con el operador +
        int suma = n1 + n2;
        System.out.println("Suma: " + suma);
        // Resta dos valores con el operador -
        int resta = n1 - n2;
        System.out.println("Resta: " + resta);
        // Multiplica dos valores con el operador *
        int multiplicacion = n1 * n2;
        System.out.println("Multiplicación: " + multiplicacion);
        // Divide dos valores con el operador /
        int division = n1 / n2;
        System.out.println("División: " + division);
        // Módulo dos valores con el operador %
        int modulo = n1 % n2;
        System.out.println("Módulo: " + modulo);
    }

    static void operadoresLogicos() {
        System.out.println("Operadores lógicos");
        int n1 = 10;
        int n2 = 20;
        // Verifica si n1 y n2 son mayores a 0 con el operador && -> AND
        if (n1 > 0 && n2 > 0) {
            System.out.println("n1 y n2 son mayores a 0");
        }
        // Verifica si n1 o n2 son mayores a 0 con el operador || -> OR
        if (n1 > 0 || n2 > 0) {
            System.out.println("n1 o n2 son mayores a 0");
        }
        // Verifica si n1 es diferente a 0 con el operador != -> NOT
        if (n1 != 0) {
            System.out.println("n1 es diferente a 0");
        }
    }

    static void operadoresComparacion() {
        System.out.println("Operadores de comparación");
        int n1 = 10;
        int n2 = 20;
        // Verifica si n1 es mayor a n2 con el operador >
        if (n1 > n2) {
            System.out.println("n1 es mayor a n2");
        }
        // Verifica si n1 es menor a n2 con el operador <
        if (n1 < n2) {
            System.out.println("n1 es menor a n2");
        }
        // Verifica si n1 es mayor o igual a n2 con el operador >=
        if (n1 >= n2) {
            System.out.println("n1 es mayor o igual a n2");
        }
        // Verifica si n1 es menor o igual a n2 con el operador <=
        if (n1 <= n2) {
            System.out.println("n1 es menor o igual a n2");
        }
        // Verifica si n1 es igual a n2 con el operador ==
        if (n1 == n2) {
            System.out.println("n1 es igual a n2");
        }
        // Verifica si n1 es diferente a n2 con el operador !=
        if (n1 != n2) {
            System.out.println("n1 es diferente a n2");
        }
    }

    static void operadoresAsignacion() {
        System.out.println("Operador de asignación");
        int n;
        // Asigna un valor a n con el operador de asignación =
        n = 10;
        System.out.println("n = " + n);
        // Asigna un valor a n con el operador de asignación +=
        n += 5;
        System.out.println("n = " + n);
        // Resta un valor a n con el operador -=
        n -= 5;
        System.out.println("n = " + n);
        // Multiplica un valor a n con el operador *=
        n *= 5;
        System.out.println("n = " + n);
        // Divide un valor a n con el operador /=
        n /= 5;
        System.out.println("n = " + n);
        // Módulo un valor a n con el operador %=
        n %= 5;
        System.out.println("n = " + n);
    }

    static void operadoresUnarios() {
        System.out.println("Operadores unarios");
        // Operador unario + -> Representa un valor positivo, por defecto los valores son positivos
        int n = +10;
        System.out.println("n = " + n);
        // Operador de incremento ++ -> Incrementa en 1 el valor de la variable
        n++;
        System.out.println("n = " + n);
        // Operador de decremento -- -> Decrementa en 1 el valor de la variable
        n--;
        System.out.println("n = " + n);
        --n; // Decrementa en 1 el valor de la variable
        System.out.println("n = " + n);
        ++n; // Incrementa en 1 el valor de la variable
        System.out.println("n = " + n);
        // Operador unario - -> Representa un valor negativo
        n = -n;
        System.out.println("n = " + n);
        // Operador de negación ! -> Niega el valor de una variable booleana
        boolean b = !true;
        System.out.println("b = " + b);
    }

    static void operadoresBits() {
        System.out.println("Operadores de bits");
        int n1 = 10;
        int n2 = 20;
        // Operador de desplazamiento a la izquierda << -> Desplaza los bits de un valor a la izquierda
        int desplazamientoIzquierda = n1 << 2;
        System.out.println("Desplazamiento a la izquierda: " + desplazamientoIzquierda);
        // Operador de desplazamiento a la derecha >> -> Desplaza los bits de un valor a la derecha
        int desplazamientoDerecha = n1 >> 2;
        System.out.println("Desplazamiento a la derecha: " + desplazamientoDerecha);
        // Operador de desplazamiento a la derecha sin signo >>> -> Desplaza los bits de un valor a la derecha sin signo
        int desplazamientoDerechaSinSigno = n1 >>> 2;
        System.out.println("Desplazamiento a la derecha sin signo: " + desplazamientoDerechaSinSigno);
        // Operador AND a nivel de bits & -> Realiza la operación AND a nivel de bits
        int and = n1 & n2;
        System.out.println("AND: " + and);
        // Operador OR a nivel de bits | -> Realiza la operación OR a nivel de bits
        int or = n1 | n2;
        System.out.println("OR: " + or);
        // Operador XOR a nivel de bits ^ -> Realiza la operación XOR a nivel de bits
        int xor = n1 ^ n2;
        System.out.println("XOR: " + xor);
        // Operador de complemento a nivel de bits ~ -> Realiza la operación de complemento a nivel de bits
        int complemento = ~n1;
        System.out.println("Complemento: " + complemento);
    }
}
