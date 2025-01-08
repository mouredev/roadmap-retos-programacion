package Number001Java;

public class ARHL2023 {
    public static void main(String[] args) {

        //Operadores Aritméticos:
        int a = 10;
        int b = 5;
        System.out.println("\nOperadores Aritméticos: ");
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));
        System.out.println("Incremento: " + (++a));
        System.out.println("Decremento: " + (--b));

        //Operadores Lógicos:
        boolean x = true;
        boolean y = false;
        System.out.println("\nOperadores Lógicos:");
        System.out.println("AND lógico: " + (x && y));
        System.out.println("OR lógico: " + (x || y));
        System.out.println("NOT lógico: " + (!x));

        //Operadores de Asignación:
        int c = 5;
        c += 3;
        System.out.println("\nOperadores de Asignación:");
        System.out.println("Asignación con suma: " + c);
        c -= 2;
        System.out.println("Asignación con resta: " + c);
        c *= 4;
        System.out.println("Asignación con multiplicación: " + c);
        c /= 2;
        System.out.println("Asignación con división: " + c);
        c %= 3;
        System.out.println("Asignación con módulo: " + c);

        //Operadores de Identidad:
        System.out.println("\nOperadores de Identidad:");
        String str = "Hola";
        Integer num = 0;
        System.out.println("¿Es una instancia de String? " + (str instanceof String));
        System.out.println("¿Es una instancia de int? " + (num instanceof Integer));

        //Operadores de Pertenencia:
        System.out.println("\nOperadores de Pertenencia:");
        int[] arr = {1, 2, 3, 4, 5};
        int val = 3;
        boolean pertenece = false;
        for (int i : arr) {
            if (i == val) {
                pertenece = true;
                break;
            }
        }
        System.out.println("¿El valor " + val + " está en el array? " + pertenece);

        //Operadores de Bits:
        System.out.println("\nOperadores de Bits:");
        int d = 5; // Representación binaria: 101
        int e = 3; // Representación binaria: 011
        System.out.println("AND a nivel de bits: " + (d & e));
        System.out.println("OR a nivel de bits: " + (d | e));
        System.out.println("XOR a nivel de bits: " + (d ^ e));
        System.out.println("Desplazamiento a la izquierda: " + (d << 1));
        System.out.println("Desplazamiento a la derecha: " + (e >> 1));
        System.out.println("Desplazamiento sin signo a la derecha: " + (e >>> 1));

        System.out.println("\n\tEjemplos de estructuras de control:");

        //Condicionales (if-else):
        System.out.println("\nCondicionales (if-else):");
        int numCondicional = 10;
        if (numCondicional > 0) {
            System.out.println("El número es positivo");
        } else if (numCondicional < 0) {
            System.out.println("El número es negativo");
        } else {
            System.out.println("El número es cero");
        }


        //Estructuras iterativas (for, while, do-while):
        System.out.println("\nEstructuras iterativas (for, while, do-while):");

        // Ciclo for
        for (int i = 1; i <= 5; i++) {
            System.out.println("Iteración #" + i);
        }

// Ciclo while
        int j = 0;
        while (j < 5) {
            System.out.println("Iteración en while #" + j);
            j++;
        }

// Ciclo do-while
        int k = 0;
        do {
            System.out.println("Iteración en do-while #" + k);
            k++;
        } while (k < 5);

        //RETO
//DIFICULTAD EXTRA (opcional):
//Crea un programa que imprima por consola todos los números comprendidos
//entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.


        System.out.println("\nReto: ");

        int inicio = 10;
        int fin = 55;

        for (int i = inicio; i <= fin; i++){
            if( (i>=inicio && i<=fin) && (i%2==0) && !(i%3==0) && (i!=16)  ){
                System.out.print(i+"-");
            }
        }

    }//main
}//class
