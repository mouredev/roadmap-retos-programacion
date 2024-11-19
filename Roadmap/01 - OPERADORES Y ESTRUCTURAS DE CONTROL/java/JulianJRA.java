
public class JulianJRA {

    public static void main(String[] args) {

        // Operadores aritméticos
        int a = 10, b = 3;

        System.out.println("Suma: " + (a + b)); // 13
        System.out.println("Resta: " + (a - b)); // 7
        System.out.println("Multiplicación: " + (a * b)); // 30
        System.out.println("División: " + (a / b)); // 3 (división entera)
        System.out.println("Módulo: " + (a % b)); // 1 (resto)
        System.out.println("Incremento: " + (++a)); // 11 (preincremento)
        System.out.println("Decremento: " + (--b)); // 2 (predecremento)

        // Operadores lógicos
        boolean x = true, y = false;

        System.out.println("AND (&&): " + (x && y)); // false
        System.out.println("OR (||): " + (x || y)); // true
        System.out.println("NOT (!): " + (!x)); // false

        // Operadores de comparación
        System.out.println("Igual a: " + (a == b)); // false
        System.out.println("No igual: " + (a != b)); // true
        System.out.println("Mayor que: " + (a > b)); // true
        System.out.println("Menor que: " + (a < b)); // false
        System.out.println("Mayor o igual: " + (a >= b)); // false
        System.out.println("Menor o igual: " + (a <= b)); // false

        // Operadores de asignación
        a += 5; // a = a + 5
        System.out.println("Suma y asigna: " + a); // 15

        a -= 3; // a = a - 3
        System.out.println("Resta y asigna: " + a); // 12

        a *= 2; // a = a * 2
        System.out.println("Multiplica y asigna: " + a); // 24

        a /= 4; // a = a / 4
        System.out.println("Divide y asigna: " + a); // 6

        a %= 5; // a = a % 5
        System.out.println("Módulo y asigna: " + a); // 1

        // Operadores a nivel de bits
        int c = 5; // 0101 en binario
        int d = 3; // 0011 en binario

        System.out.println("AND (&): " + (c & d)); // 1 (0001 en binario)
        System.out.println("OR (|): " + (c | d)); // 7 (0111 en binario)
        System.out.println("XOR (^): " + (c ^ d)); // 6 (0110 en binario)
        System.out.println("NOT (~): " + (~c)); // -6 (inversión de bits)
        System.out.println("Shift izquierda (<<): " + (c << 1)); // 10 (1010 en binario)
        System.out.println("Shift derecha (>>): " + (c >> 1)); // 2 (0010 en binario)
        System.out.println("Shift derecha sin signo (>>>): " + (c >>> 1)); // 2

        // ESTRUCTURAS CONDICIONALES
        // if-else
        int edad = 20;

        if (edad >= 18) {
            System.out.println("Eres mayor de edad.");
        } else {
            System.out.println("Eres menor de edad.");
        }

        // if-elseif-else
        int calificacion = 85;

        if (calificacion >= 90) {
            System.out.println("Excelente");
        } else if (calificacion >= 70) {
            System.out.println("Aprobado");
        } else {
            System.out.println("Suspenso");
        }

        // Switch
        int dia = 3;

        switch (dia) {
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
                System.out.println("Día no válido");
        }

        // ESTRUCTURAS ITERATIVAS
        // for
        for (int i = 1; i <= 5; i++) {
            System.out.println("Iteración: " + i);
        }

        // while
        int contador = 0;

        while (contador < 3) {
            System.out.println("Contador: " + contador);
            contador++;
        }

        // do-while
        int numero = 0;

        do {
            System.out.println("Número: " + numero);
            numero++;
        } while (numero < 3);

        // for-each
        int[] numeros = { 1, 2, 3, 4, 5 };

        for (int num : numeros) {
            System.out.println("Número: " + num);
        }

        // ESTRUCTURAS DE EXCEPCIONES
        // try-catch-finally
        try {
            int resultado = 10 / 0; // Genera una excepción (división por cero)
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero no permitida.");
        } finally {
            System.out.println("Bloque 'finally' siempre se ejecuta.");
        }

        // throw y throws
        try {
            dividir(10, 0);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }

        // EJERCICIO OPCIONAL
        for(int i = 10; i < 56; i++){
            if((i%2==0) && (i!=16) && (i%3!=0)){
                System.out.println("Numero ejercicio: "+i);
            }
        }

    }

    public static void dividir(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("División por cero no permitida.");
        }
        System.out.println("Resultado:  " + (a / b));
    }

}