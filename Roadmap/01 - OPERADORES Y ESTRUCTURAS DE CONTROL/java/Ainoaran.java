//#Reto #01 OPERADORES Y ESTRUCTURAS DE CONTROL

public class Ainoaran {

    public static void main(String[] args) {

        //Operadores Aritméticos:

        System.out.println("Operadores Aritméticos: ");

        int a = 10, b = 5;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));
        System.out.println("Incremento: " + (++a));
        System.out.println("Decremento: " + (--b));

        System.out.println("--------------------------------------------------------------------------------");

        // Operadores Lógicos

        System.out.println("Operadores Lógicos: ");

        boolean x = true, y = false;
        // AND (&&) - Devuelve true si ambas condiciones son verdaderas.
        System.out.println("AND: " + (x && y));
        // OR (||) - Devuelve true si al menos una condición es verdadera.
        System.out.println("OR: " + (x || y));
        // NOT (!) - invierte el valor de una condición, es decir, cambia true a false y viceversa.
        System.out.println("NOT: " + (!x));

        System.out.println("--------------------------------------------------------------------------------");


        // Operadores de Comparación

        System.out.println("Operadores de comparación: ");

        System.out.println("Igualdad: " + (a == b));
        System.out.println("Diferente: " + (a != b));
        System.out.println("Mayor que: " + (a > b));
        System.out.println("Menor que: " + (a < b));
        System.out.println("Mayor o igual que: " + (a >= b));
        System.out.println("Menor o igual que: " + (a <= b));

        System.out.println("--------------------------------------------------------------------------------");

        // Operadores de Asignación:

        System.out.println("Operadores de Asignación: ");

        int c = 3;
        System.out.println("Suma y asigna: " + (c+=4));
        System.out.println("Resta y asigna: " + (c-=8));
        System.out.println("Multiplica y asigna: " + (c*=10));
        System.out.println("Divide y asigna: " + (c/=20));
        System.out.println("Módulo y asigna: " + (c%=6));

        System.out.println("--------------------------------------------------------------------------------");

        // Operadores de Identidad

        System.out.println("Operadores de Identidad: ");

        String s1 = "Hola", s2 = "こんにちは";
        System.out.println("Compara referencias: " + (s1 == s2));
        System.out.println("Compara contenido: " + s1.equals(s2));

        System.out.println("--------------------------------------------------------------------------------");

        //Operadores binarios:

        System.out.println("Operadores Binarios: ");

        int d = 6, e = 12;
        System.out.println("Valor de 6 en binario: " + Integer.toBinaryString(d));
        System.out.println("Valor de 12 en binario: " + Integer.toBinaryString(e));


        System.out.println("d AND e : " + Integer.toBinaryString(d & e));
        System.out.println("d OR e : " + Integer.toBinaryString(d | e));
        System.out.println("d XOR e : " + Integer.toBinaryString(d ^ e));
        System.out.println("Complemento de d = " + Integer.toBinaryString(~d));
        System.out.println("Complemento de e = " + Integer.toBinaryString(~e));
        System.out.println("Desplazamiento de bits de d a la izquierda de e: " + Integer.toBinaryString(d<<e));
        System.out.println("Desplazamiento de bits de d a la derecha de e: " + Integer.toBinaryString(d>>e));
        System.out.println("Desplazamiento de bits de d a la derecha de e (sin signo): " + Integer.toBinaryString(d>>>e));

        System.out.println("--------------------------------------------------------------------------------");

        //Estructuras de control:

        System.out.println("Condicionales: ");
        int f= 10, g = 5;
        if(f>g) {
            System.out.println("f es mayor que g");
        } else {
            System.out.println("g es mayor que f");
        }

        System.out.println("Bucle for:");
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }

        System.out.println("Bucle while");
        int num = 1;
        while (num <= 10) {
            System.out.println(num);
            num++;
        }

        System.out.println("--------------------------------------------------------------------------------");

        System.out.println("Ejercicio extra: ");

        /*Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }

    }
}
