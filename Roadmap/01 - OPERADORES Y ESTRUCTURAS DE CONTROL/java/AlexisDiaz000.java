public class AlexisDiaz000{
    public static void main(String[] args) {
        /*Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...*/

        int a = 10, b = 5;
        double x = 10.5, y = 5.5;
        //suma
        System.out.println("valores Enteros: a = 10 y b = 5 - valores decimales: x = 10.5 y y = 5.5");
        int sumaEteros = a + b;
        double sumaDecimales = x + y;
        System.out.println("Sumas Enteros: " + sumaEteros + "\nSumas Decimales: " + sumaDecimales);
        //resta
        System.out.println("Restas Enteros : " + (a - b));
        //divición
        System.out.println("divicion entre enteros y decimales a/y: " + (a / y));
        //multiplicación
        var multiplicador = a * b;
        System.out.println("multiplicación de enteros: " + multiplicador);
        // Módulo o residuo (%)
        int moduloEnteros = a % b;
        System.out.println("Módulo de enteros: " + moduloEnteros + " y modulos de decimales: " + (x % y));
        // Incremento (++)
        int incremento = a;
        incremento++;
        System.out.println("Incremento (++): " + incremento);
        // Decremento (--)
        b--;
        System.out.println("Decremento (--): " + b);

        //OPERADORES LOGICOS
        boolean and = (2 > 5) && (10 < 3);
        boolean or = (10 > 8) || (8 < 3);
        boolean not = !(10 > 15);
        System.out.println("\nOperadores Lógicos:");
        System.out.println("OPERADOR AND: " + and + ",OPERADOR OR: " + or + ", OPERADOR NOT: " + not);

        //OPERADORES DE COMPARACIÓN

        boolean mayor = 10 > 5;
        boolean menor = 10 < 5;
        boolean igual = 10 == 10;
        boolean diferente = 10 != 5;
        System.out.println("\nOperadores de Comparación:");
        System.out.println("10 > 5: " + mayor + ", 10 < 5: " + menor + ", 10 == 10: " + igual + ", 10 != 5: " + diferente);


        //OPERADORES DE ASIGNACIÓN
        int numero = 10;

        numero = 30;
        System.out.println(numero);
        numero += 10;
        System.out.println(numero);
        numero -= 10;
        System.out.println(numero);
        numero /= 2;
        System.out.println(numero);
        numero *= 10;
        System.out.println(numero);
        numero %= 2;
        if (numero == 0) {
            System.out.println("es par");
        } else {
            System.out.println(("no es par"));
        }

        // If-Else
        int edad = 18;
        if (edad >= 18) {
            System.out.println("\nEres mayor de edad");
        } else {
            System.out.println("\nEres menor de edad");
        }

        // Switch
        int opcion = 1;
        switch (opcion) {
            case 1:
                System.out.println("\nOpción 1 seleccionada");
                break;
            case 2:
                System.out.println("\nOpción 2 seleccionada");
                break;
            default:
                System.out.println("\nOpción no válida");
        }

        // Bucle While
        int contador = 3;
        System.out.println("\nBucle While:");
        while (contador > 0) {
            System.out.println("Contador: " + contador);
            contador--;
        }

        // Bucle For
        System.out.println("\nBucle For:");
        for (int i = 1; i <= 3; i++) {
            System.out.println("Iteración: " + i);
        }

        // Try-Catch (Manejo de Excepciones)
        try {
            int resultado = 10 / 0; // Error: División por cero
            System.out.println(resultado);
        } catch (ArithmeticException e) {
            System.out.println("\nError: División por cero no permitida");

        }
        //Crea un programa que imprima por consola todos los números comprendido
        // entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3

        System.out.println("Números pares entre 10 y 55, excluyendo 16 y múltiplos de 3:");

        for (int i = 10; i <= 55; i++) {
            // Verificar si el número es par, no es 16 y no es múltiplo de 3
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.print(i + " ");
            }
        }
    }

}    

