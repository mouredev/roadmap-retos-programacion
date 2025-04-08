/**
 * Clase Zugarramurdi donde se implementara la solucion al ejercicio #01 - OPERADORES Y ESTRUCTURAS DE CONTROL
 * @author Zugarramurdi
 * @version 1.0
 * @date 05/04/2025
 */

public class Zugarramurdi {
    public static void main(String[] args) {

        // Definicion de variables
        int num1 = 10;
        int num2 = 2;
        int num3 = 45;
        int num4 = 5;

        // Operaciones aritmeticas asignadas a variables
        System.out.println("\nOperaciones Aritmeticas:\n");
        int suma = num1 + num2;
        int resta = num1 - num3;
        int multiplicacion = num1 * num2;
        double division = num3 / num2;
        double modulo = num3 % num2;
        System.out.println("Suma: " + num1 + " + " + num2 + " = " + suma);
        System.out.println("Resta: " + num1 + " - " + num3 + " = " + resta);
        System.out.println("Multiplicacion: " + num1 + " * " + num2 + " = " + multiplicacion);
        System.out.println("Division: " + num3 + " / " + num2 + " = " + division);
        System.out.println("Modulo: " + num3 + " % " + num2 + " = " + modulo);

        // Operaciones de incremento y decremento asignadas a variables
        System.out.println("\nOperaciones de Incremento y Decremento: \n");
        int incremento = ++num1;
        int decremento = --num2;
        --num1; // Devuelvo el valor original de num1
        ++num2; // Devuelvo el valor original de num2
        System.out.println("Incremento: 10" + " ++ = " + incremento);
        System.out.println("Decremento: 2" + " -- = " + decremento);

        // Operaciones de comparacion asignadas a variables
        System.out.println("\nOperaciones de Comparacion:\n");
        boolean mayorQue = num1 > num2;
        boolean menorQue = num2 < num1;
        boolean igualQue = num1 == num2;
        boolean diferenteDe = num1 != num2;
        System.out.println(num1+ " es mayor que " + num2 + "? " + mayorQue);
        System.out.println(num2 + " es menor que " + num1 + "? " + menorQue);
        System.out.println(num1 + " es igual que " + num2 + "? " + igualQue);
        System.out.println(num1 + " es diferente de " + num2 + "? " + diferenteDe);

        // Operadores logicos asignados a variables
        System.out.println("\nOperadores Logicos:\n");
        boolean and = (num1 > num2) && (num1 < num3);
        boolean or = (num1 > num2) || (num1 < num3);
        boolean not = (num1 != num2);
        System.out.println("AND: " + num1 + " > " + num2 + " AND " + num1 + " < " + num3 + " = " + and);
        System.out.println("OR: " + num1 + " > " + num2 + " OR " + num1 + " < " + num3 + " = " + or);
        System.out.println("NOT: " + num1 + " IS NOT " + num2 + " = " + not);

        // Operadores de asignacion
        System.out.println("\nOperadores de Asignacion:\n");
        System.out.println("Asignacion: " + num4 + "+=5 = " + (num4 += 5));
        num4-=5; // Devuelvo el valor original de num4
        System.out.println("Asignacion: " + num4 + "-=3 = " + (num4 -= 3));
        num4+=3; // Devuelvo el valor original de num4
        System.out.println("Asignacion: " + num4 + "*=2 = " + (num4 *= 2));
        num4/=2; // Devuelvo el valor original de num4
        System.out.println("Asignacion: " + num4 + "/=2 = " + (num4 /= 2));
        num4*=2; // Devuelvo el valor original de num4
        System.out.println("Asignacion: " + num4 + "%=2 = " + (num4 %= 2));
        num4+=5; // Devuelvo el valor original de num4

        // Operadores ternarios
        System.out.println("\nOperadores Ternarios:\n");
        //Sintaxis - (condicion) ? valorSiVerdadero : valorSiFalso;
        String resultado = (num1 > num2) ? "num1 es mayor que num2" : "num2 es mayor que num1";
        System.out.println("Resultado: " + resultado);

        // Operadores de bits
        System.out.println("\nOperadores de Bits:\n");
        String num1Binary = Integer.toBinaryString(num1);
        String num2Binary = Integer.toBinaryString(num2);
        System.out.println("num1: " + num1 + " (" + num1Binary + ")");
        System.out.println("num2: " + num2 + " (" + num2Binary + ")");
        System.out.println("AND: " + num1 + " & " + num2 + " = " + (num1 & num2) + " (" + Integer.toBinaryString(num1 & num2) + ")");
        System.out.println("OR: " + num1 + " | " + num2 + " = " + (num1 | num2) + " (" + Integer.toBinaryString(num1 | num2) + ")");
        System.out.println("XOR: " + num1 + " ^ " + num2 + " = " + (num1 ^ num2) + " (" + Integer.toBinaryString(num1 ^ num2) + ")");
        System.out.println("NOT: ~" + num1 + " = " + (~num1) + " (" + Integer.toBinaryString(~num1) + ")");
        System.out.println("Desplazamiento a la izquierda: " + num1 + " << 2 = " + (num1 << 2) + " (" + Integer.toBinaryString(num1 << 2) + ")");
        System.out.println("Desplazamiento a la derecha: " + num1 + " >> 2 = " + (num1 >> 2) + " (" + Integer.toBinaryString(num1 >> 2) + ")");

        // Estructuras de control
        System.out.println("\nEstructuras de Control:\n");
        // if - else if - else
        if (num1 > num2) {
            System.out.println("El número " + num1 + " es mayor que " + num2);
        } else if (num1 < num2) {
            System.out.println("El número " + num1 + " es menor que " + num2);
        } else {
            System.out.println("El número " + num1 + " es igual a " + num2);
        }
        // switch
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
            case 4:
                System.out.println("Jueves");
                break;
            case 5:
                System.out.println("Viernes");
                break;
            case 6:
                System.out.println("Sábado");
                break;
            case 7:
                System.out.println("Domingo");
                break;
            default:
                System.out.println("Día inválido");
        }
        // bucles
        System.out.println("\nBucles:\n");
        // while
        int i = 0;
        while (i < 5) {
            System.out.println("While: " + i);
            i++;
        }
        // do while
        int j = 0;
        do {
            System.out.println("Do While: " + j);
            j++;
        } while (j < 5);
        // for
        for (int k = 0; k < 5; k++) {
            System.out.println("For: " + k);
        }
        // for each
        int[] numeros = {1, 2, 3, 4, 5};
        for (int numero : numeros) {
            System.out.println("For Each: " + numero);
        }

       // Identidad
        System.out.println("\nOperador Identidad:\n");
        String cadena = "Hola Mundo";
        if (cadena instanceof String){
            System.out.println("La variable cadena es un String");
        } else {
            System.out.println("La variable cadena no es un String");
        }

        // Excepciones
        System.out.println("\nExcepciones:\n");
        try {
            int resultadoDivision = num3 / 0;
            System.out.println("Resultado de la división: " + resultadoDivision);
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero");
        } finally {
            System.out.println("Bloque finally ejecutado");
        }

        // Dificultad Extra
        System.out.println("\nDificultad Extra:\n");
        for (int l = 10; l <=55; l++){
            if (l!=16 && l%3!=0 && l%2==0){
                System.out.println(l);
            }
        }










    }
}
