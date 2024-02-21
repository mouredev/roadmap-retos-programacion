import org.w3c.dom.ls.LSOutput;

import java.util.InputMismatchException;
import java.util.Scanner;

public class vixxtory {
    /**
     * OPERADORES EN JAVA
     * Permiten realizar diversas operaciones y manipulaciones de datos y variables como:
     * Cálculos matemáticos
     * Evaluaciones de condiciones lógicas
     * Manipulación de datos a nivel de bits.
     * **/

    public static void main(String[] args) {

        /** Los operadores aritméticos permiten realizar cálculos matemáticos.
         * Fundamental para aplicaciones financieras, científicas o de ingeniería.
         * **/

        /** OPERADORES ARITMETICOS **/
        byte suma = 10 + 10;
        byte resta = 10 - 8;
        byte multiplicacion = 10 - 8;
        byte division = 15 / 5;
        byte modulo = 10 % 2;
        System.out.println("Suma 10 + 10 " + suma);
        System.out.println("Resta 10 - 8 = " + resta);
        System.out.println("Multiplicación 10 * 10 = " + multiplicacion);
        System.out.println("División 15 / 5 = " + division);
        System.out.println("Modulo 10 % 2 = " + modulo);

        /** Los operadores de asignación permiten asignar valores a variables y actualizarlos,
         * lo que facilita la manipulación de datos y el seguimiento de estados. **/

        /** OPERADORES DE ASIGNACION **/
        System.out.println("Igualdad = ");
        //Compuestos
        System.out.println(" Suma y asignación += ");
        System.out.println(" Resta y asignación -= ");
        System.out.println(" Multiplicación y asignación *= ");
        System.out.println(" Division y asignación /= ");
        System.out.println(" Modulo y asignacion %/ ");

        /** Los operadores de comparación y lógicos son esenciales para tomar decisiones basadas en condiciones.
         *  Estos operadores permiten crear lógica condicional, fundamental para el flujo de un programa. **/

        /** OPERADORES DE COMPARACIÓN
         * Devuelven verdadero o falso
         * **/
        System.out.println(" Igual a == ");
        System.out.println(" Diferente de != ");
        System.out.println(" Mayor que > ");
        System.out.println(" Menor que < ");
        System.out.println(" Mayor o igual que >= ");
        System.out.println(" Menor o igual que <= ");

        /** OPERADORES LOGICOS
         * Evalúan una expresión de uno o dos operandos con valor de tipo boolean y devuelven otro boolean
         * **/
        System.out.println(" AND && ");
        System.out.println(" OR || ");
        System.out.println(" NOT ! ");

        /** Las operaciones sobre bits son útiles en situaciones donde se necesita manipular o extraer
         * datos específicos de un número entero representado en bits.
         * Por ejemplo, para manipular colores en gráficos o para realizar cálculos en algoritmos de criptografía.
         **/

        System.out.println(" Desplazamiento a la izquierda << ");
        System.out.println(" Desplazamiento a la derecha >> ");
        System.out.println(" AND a nivel de bits & ");
        System.out.println(" OR a nivel de bits | ");

        /** ESTRUCTURAS DE CONTROL
         * Se usan para modificar el flujo secuencial de un programa.**/

        //CONDICIONALES

        byte x = 0;

        if (x == 1) System.out.println("x es igual a 1");
        else if (x == 0) System.out.println("x es igual a 0");
        else System.out.println("x no es ni 0 ni 1");


        // SWITCH: compara una variable con una lista y ejecuta el código correspondiente al caso que coincida
        switch (x) {
            case 1:
                System.out.println("La variale tiene valor 1");
                break; //sale de un bucle o estructura de control de selección antes de que se complete
            case 2:
                System.out.println("La variale tiene valor 2");
                break;
            case 3:
                System.out.println("La variable tiene valor 3");
                break;
            default:
                System.out.println("La variable tiene un valor desconocido");
        }

        //ITERATIVAS O BUCLES
        for(int i = 1; i <= 4; i++)
        {
            if( i == 3 ) continue; //salta a la siguiente iteración de un bucle
            System.out.println(x);
            x ++;
        }

        x = 1;
        while( x <= 5){
            System.out.println("Iterado "+ x +" Veces");
            x++;
        }

        x = 1;
        do{
            System.out.println("Iterado "+ x + "veces");
            x++;
        } while(x <= 5);

        //MANEJO DE EXCEPCIONES
        Scanner scanner = new Scanner(System.in);
        int num1,num2, div;
        try{
            System.out.println("Primer número, debe ser un valor entero ");
            num1=scanner.nextInt();
            System.out.println(" Divisor, un valor entero ");
            num2=scanner.nextInt();
            div= num1/num2;
            System.out.println(division);}
        catch(InputMismatchException excepcion){

            System.err.println("Se ingresó un tipo de dato incorrecto");
        }
        catch(ArithmeticException excepcion){
            System.err.println("Se intentó dividir por cero");
        }
        finally{
            System.out.println("Ha finalizado el ejemplo");}

        //DIFICULTAD EXTRA: Crea un programa que imprima por consola todos los números comprendidos
        // * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.


        for(int num = 10; num <= 55; num++){
            if( num%2 == 0 && num != 16 && esMultiploDeTres(num))
            System.out.println(num);
        }
    }
    public static boolean esMultiploDeTres(int numero) {// Función para determinar si un número es múltiplo de 3
        int sumaDigitos = 0;
        while (numero > 0) {
            sumaDigitos += numero % 10; // Obtenemos el último dígito y lo sumamos
            numero /= 10; // Eliminamos el último dígito
        }
        // Comprobamos si la suma de los dígitos es divisible por 3
        return sumaDigitos % 3 == 0;
    }
}
