import static java.lang.Math.pow;
import static java.lang.Math.round;

public class LucasAG01 {

    public static void main(String[] args) {



        //OPERADORES

        System.out.println("Suma: 10 + 3 = " + (10 + 3));
        System.out.println("Resta: 10 - 3 = " + (10 - 3));
        System.out.println("Multiplicacion: 10 * 3 = " + (10 * 3));
        System.out.println("Division: 10 / 3 = " + (10 / 3));
        System.out.println("Resto: 10 % 5 = " + (10 % 5));
        System.out.println("Exponente: 12 a la 3 = " + (int) pow(12,3));
        System.out.println("Exponente: 10 ^ 3 = " + (10 ^ 3));
        System.out.println("Raiz cuadrada: √64 = "+(int)(Math.sqrt(64)));

        System.out.println("*****************************************************");

        //OPERADORES COMPARACION

        System.out.println("Igualdad: 10==10 ? " +(10==10));
        System.out.println("Desigualdad: 10!=3 ? "+(10!=3));
        System.out.println("Mayor que : 10 > 3 = " + (10 > 3));
        System.out.println("Menor que : 10 < 3 = " + (10 < 3));

        System.out.println("*****************************************************");

        //OPERADORES UNARIOS

        int c = 10;

        System.out.println("Mantiene el signo: " + (+c));
        System.out.println("Cambia el signo: " + (-c));
        System.out.println("Autoincremento e impresión: " + (++c)); //Se incrementa y se imprime
        System.out.println("Impresión y autoincremento: " + (c++)); //Se imprime y se incrementa
        System.out.println("Autodecremento e impresión: " + (--c)); //Se decrementa y se imprime
        System.out.println("Impresión y autodecremento: " + (c--)); //Se imprime y se decrementa

        System.out.println("*****************************************************");


        //OPERADORES LÓGICOS

        boolean v = true;
        boolean f = false;


        System.out.println("¿true es igual a false? : " + (v&f));
        System.out.println("¿true es igual a false? (cortocircuíto) : " + (v&&f));
        System.out.println("¿true o false son verdaderas? : " + (v|f));
        System.out.println("¿true o false son verdaderas? (cortocircuíto) : " + (v||f));
        System.out.println("Cambiamos el valor de true : " + (!v));

        System.out.println("*****************************************************");


        /*OPERADORES ASIGNACIÓN
        ipos:
         *      -- +=: Suma a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- -=: Resta a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- *=: Multiplica a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- /=: Divide a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- %=: Realiza el módulo a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- &=: Realiza un AND lógico a la variable y sobrescribe el valor de la variable con el resultado.
                -- |=: Realiza un OR lógico a la variable y sobrescribe el valor de la variable con el resultado.
        */

        int a;
        boolean t = true;

        System.out.println("Operadores de asignación: Para asignar un valor a una variable.");

        System.out.println("Asignamos valor a la variable i = " + (a = 1));
        System.out.println("Suma y asigna: " + (a+=5));
        System.out.println("Resta y asigna: " + (a-=5));
        System.out.println("Multiplica y asigna: " + (a*=5));
        System.out.println("Divide y asigna: " + (a/=5));
        System.out.println("Módulo y asigna: " + (a/=5));
        System.out.println("AND lógico y asigna: " + (t&=true));
        System.out.println("OR lógico y asigna: " + (t|=false));

        System.out.println("*****************************************************");

        /*Operadores a nivel de bits: operan con cada bit del operando, ofreciendo un control más granular sobre los datos.
                * Tipos:
         *      -- AND (&): Operador AND a nivel de bits (1 y 1 = 1).
         *      -- OR (|): Operador OR a nivel de bits (1 o 1 = 1).
         *      -- XOR (^): Operador XOR a nivel de bits (1 y 1 = 0).
         *      -- Complemento (~): Invierte el valor de cada bit.
         *      -- >> : Desplaza bits a la derecha.
         *      -- << : Desplaza bits a la izquierda.
         *      -- >>> : Desplaza bits a la derecha sin signo.
         */
        int x = 10;
        int y = 7;

        System.out.println("Operadores a nivel de bits: operan con cada bit del operando, ofreciendo un control más granular sobre los datos.");

        System.out.println();

        System.out.println("x : " + Integer.toBinaryString(x));
        System.out.println("y : " + Integer.toBinaryString(y));

        System.out.println();

        System.out.println("X AND y : " + Integer.toBinaryString(x & y));
        System.out.println("x OR y : " + Integer.toBinaryString(x | y));
        System.out.println("x XOR y : " + Integer.toBinaryString(x ^ y));
        System.out.println("Complemento de x = " + Integer.toBinaryString(~x));
        System.out.println("Complemento de y = " + Integer.toBinaryString(~y));
        System.out.println("Desplazamiento de bits de x a la izquierda de y: " + Integer.toBinaryString(x<<y));
        System.out.println("Desplazamiento de bits de x a la derecha de y: " + Integer.toBinaryString(x>>y));
        System.out.println("Desplazamiento de bits de x a la derecha de y (sin signo): " + Integer.toBinaryString(x>>>y));


        System.out.println("*****************************************************");

        /*EL EJERCICIO EXTRA
        Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        */

        for (int i = 10; i <56 ; i++) {
            if(i%2==0 && i!=16 && i%3 != 0){
                System.out.println(i);
            }
        }

        /* en el for ponemos de donde a donde vamos a analizar los numeros
        y dentro un if con las condiciones en el orden propuesto separados por &&
         */


    }

}
