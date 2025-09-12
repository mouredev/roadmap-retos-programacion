import java.util.Scanner;

public class Peeanoot {

    public static void main(String[] args) {
        // Operadores Aritméticos
        int a = 10, b = 5;
        int suma = a + b;
        int resta = a - b;
        int multiplicacion = a * b;
        int division = a / b;
        int modulo = a % b;

        System.out.println("Operadores Aritméticos:");
        System.out.println("Suma: " + suma);
        System.out.println("Resta: " + resta);
        System.out.println("Multiplicación: " + multiplicacion);
        System.out.println("División: " + division);
        System.out.println("Módulo: " + modulo);

        // Operadores Lógicos
        boolean condicion1 = true, condicion2 = false;
        boolean andLogico = condicion1 && condicion2;
        boolean orLogico = condicion1 || condicion2;
        boolean notLogico = !condicion1;

        System.out.println("\nOperadores Lógicos:");
        System.out.println("AND Lógico: " + andLogico);
        System.out.println("OR Lógico: " + orLogico);
        System.out.println("NOT Lógico: " + notLogico);

        // Operadores de Comparación
        int num1 = 10, num2 = 20;
        boolean igual = (num1 == num2);
        boolean noIgual = (num1 != num2);
        boolean mayorQue = (num1 > num2);
        boolean menorQue = (num1 < num2);

        System.out.println("\nOperadores de Comparación:");
        System.out.println("Igual: " + igual);
        System.out.println("No Igual: " + noIgual);
        System.out.println("Mayor Que: " + mayorQue);
        System.out.println("Menor Que: " + menorQue);

        // Operadores de Asignación
        int x = 5;
        x += 3;
        System.out.println("\nOperadores de Asignación:");
        System.out.println("Valor de x después de la asignación: " + x);

        // Operadores de Identidad
        String cadena1 = "Hola";
        String cadena2 = "Hola";
        boolean sonIguales = (cadena1 == cadena2);

        System.out.println("\nOperadores de Identidad:");
        System.out.println("Son Iguales (Identidad): " + sonIguales);

        // Operadores de Pertenencia
        int[] arreglo = {1, 2, 3, 4, 5};
        boolean contieneTres = contains(arreglo, 3);

        System.out.println("\nOperadores de Pertenencia:");
        System.out.println("Contiene el número 3 (Pertenencia): " + contieneTres);

        // Operadores de Bits
        int numeroBits = 5; // Representación binaria: 101
        int operacionAND = numeroBits & 3; // Resultado: 1 (1 en binario)

        System.out.println("\nOperadores de Bits:");
        System.out.println("Operación AND Bit a Bit: " + operacionAND);

        // Estructuras de Control Condicionales
        int edad = 18;
        if (edad >= 18) {
            System.out.println("\nEstructuras de Control Condicionales:");
            System.out.println("Es mayor de edad.");
        } else {
            System.out.println("\nEstructuras de Control Condicionales:");
            System.out.println("Es menor de edad.");
        }

        // Estructuras de Control Iterativas
        System.out.println("\nEstructuras de Control Iterativas:");
        for (int i = 1; i <= 3; i++) {
            System.out.println("Iteración " + i);
        }

        // Estructuras de Control de Excepciones
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("\nEstructuras de Control de Excepciones:");
            System.out.print("Ingrese un número entero: ");
            int numeroIngresado = scanner.nextInt();
            System.out.println("Número ingresado: " + numeroIngresado);
        } catch (Exception e) {
            System.out.println("Error: Ingrese un número válido.");
        } finally {
            scanner.close();
        }

        // Imprimir números entre 10 y 55 (pares, no 16 ni múltiplos de 3)
        System.out.println("\nNúmeros entre 10 y 55 (pares, no 16 ni múltiplos de 3):");
        for (int num = 10; num <= 55; num++) {
            if (num % 2 == 0 && num != 16 && num % 3 != 0) {
                System.out.print(num + " ");
            }
        }
    }

    // Método para verificar la pertenencia en un array
    private static boolean contains(int[] array, int target) {
        for (int element : array) {
            if (element == target) {
                return true;
            }
        }
        return false;
    }
}

