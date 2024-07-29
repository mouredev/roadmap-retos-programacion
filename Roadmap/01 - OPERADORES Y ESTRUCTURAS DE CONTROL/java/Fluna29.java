package practicas;

public class Main {
    public static void main(String[] args) {
        

        //Operadores aritméticos

        int a = 10;
        int b = 5;

        System.out.println("\nOperadores aritméticos");
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));
        System.out.println("Incremento: " + (++a));
        System.out.println("Decremento: " + (--b));


        //Operadores lógicos

        boolean falso = false;
        boolean verdadero = true;

        System.out.println("\nOperadores lógicos");
        System.out.println("AND: " + (falso && verdadero));
        System.out.println("OR: " + (falso || verdadero));
        System.out.println("NOT: " + (!falso));


        //Operadores de comparación

        int comp1 = 100;
        int comp2 = 200;

        System.out.println("\nOperadores de comparación");
        System.out.println("Igual a: " + (comp1 == comp2));
        System.out.println("Diferente de: " + (comp1 != comp2));
        System.out.println("Mayor que: " + (comp1 > comp2));
        System.out.println("Menor que: " + (comp1 < comp2));
        System.out.println("Mayor o igual que: " + (comp1 >= comp2));
        System.out.println("Menor o igual que: " + (comp1 <= comp2));


        //Operadores de asignación

        int asig = 1;


        System.out.println("\nOperadores de asignación");
        System.out.println("Asignación: " + (asig = 2));
        System.out.println("Suma: " + (asig += 2));
        System.out.println("Resta: " + (asig -= 2));
        System.out.println("Multiplicación: " + (asig *= 2));
        System.out.println("División: " + (asig /= 2));
        System.out.println("Módulo: " + (asig %= 2));


        //Operadores de identidad

        System.out.println("\nOperadores de identidad");
        String txt = "Buenos dias";
        Integer num = 100;
        System.out.println("¿Es una instancia de String? " + (txt instanceof String));
        System.out.println("¿Es una instancia de Integer? " + (num instanceof Integer));


        //Operadores de pertenencia

        int[] numeros = {1, 2, 3, 4, 5};
        int num1 = 3;
        System.out.println("\nOperadores de pertenencia");
        for (int numero : numeros) {
            if (numero == num1) {
                System.out.println("El número " + num1 + " está en el array");
            }
        }


        //Operadores de Bits

        int bit1 = 60; /* 60 = 0011 1100 */
        int bit2 = 13; /* 13 = 0000 1101 */

        System.out.println("\nOperadores de Bits");
        System.out.println("AND: " + (bit1 & bit2)); /* 12 = 0000 1100 */
        System.out.println("OR: " + (bit1 | bit2)); /* 61 = 0011 1101 */
        System.out.println("XOR: " + (bit1 ^ bit2)); /* 49 = 0011 0001 */
        System.out.println("NOT: " + (~bit1)); /* -61 = 1100 0011 */
        System.out.println("Desplazamiento a la izquierda: " + (bit1 << 2)); /* 240 = 1111 0000 */
        System.out.println("Desplazamiento a la derecha: " + (bit1 >> 2)); /* 15 = 0000 1111 */
        System.out.println("Desplazamiento a la derecha sin signo: " + (bit1 >>> 2)); /* 15 = 0000 1111 */
        

        //Operador condicional ternario
        int op1 = 10;
        int op2 = 5; 

        System.out.println("\nOperador condicional ternario");
        System.out.println("El mayor es: " + ((op1 > op2) ? op1 : op2));

        //Condicionales (if-else)

        int edad = 18;

        System.out.println("\nCondicionales (if-else)");
        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }


        //Estructuras Iterativas (for, while, do-while)

        System.out.println("\nEstructuras Iterativas (for, while, do-while)");

        System.out.println("\nFor:");
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteración: " + i);
        }

        System.out.println("\nWhile:");
        int j = 0;
        while (j < 5) {
            System.out.println("Iteración: " + j);
            j++;
        }

        System.out.println("\nDo-While:");
        int k = 0;
        do {
            System.out.println("Iteración: " + k);
            k++;
        } while (k < 5);


        /**
         * DIFICULTAD EXTRA (opcional):
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        System.out.println("\nNúmeros comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3:");
        int numMin = 10;
        int numMax = 55;

        for(int i = numMin; i<=numMax; i++){
            if(i % 2 == 0 && i != 16 && i / 3 != 0){
                System.out.println(i);
            }
        }
    }
}