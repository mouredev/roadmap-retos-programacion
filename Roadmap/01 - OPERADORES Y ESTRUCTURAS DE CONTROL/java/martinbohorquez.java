/**
 * 01 - OPERADORES Y ESTRUCTURAS DE CONTROL
 *
 * @author martinbohorquez
 */
public class martinbohorquez {

    public static void main(String[] args) {
        /*
         * Operadores aritméticos: actúan sobre números enteros y en punto flotante (decimales).
         * Hay dos tipos:
         *      -- Operadores binarios.
         *      -- Operadores unarios.
         */

        /*
         * Operadores unarios: aplican a un operando.
         * Tipos:
         *      -- Mantiene el signo del operando (+)
         *      -- Cambia el signo del operando (-)
         *      -- Autoincremento (++)
         *      -- Autodecremento (--)
         */

        int a = 10;

        System.out.println("Operadores unarios: aplican a un operando.");

        System.out.println("Mantiene el signo: a => " + (+a));
        System.out.println("Cambia el signo: a => " + (-a));
        System.out.println("Autoincremento e impresión: a => " + (++a)); //Se incrementa y se imprime
        System.out.println("Impresión y autoincremento: a => " + (a++)); //Se imprime y se incrementa
        System.out.println("Autodecremento e impresión: a => " + (--a)); //Se decrementa y se imprime
        System.out.println("Impresión y autodecremento: a => " + (a--)); //Se imprime y se decrementa

        System.out.println();

        /*
         * Operadores binarios: aplican sobre dos operandos.
         * Tipos:
         *       -- Suma (+)
         *       -- Resta (-)
         *       -- Multiplicación (*)
         *       -- División (/)
         *       -- Módulo (%)
         */

        int b = 5;
        int c = 2;

        System.out.println("Operadores binarios: aplican sobre dos operandos: ");

        System.out.println("Suma: " + b + " + " +  c + " = " + (b + c));
        System.out.println("Resta: " + b + " - " +  c + " = " + (b - c));
        System.out.println("Multiplicación: " + b + " * " +  c + " = " + (b * c));
        System.out.println("División: " + b + " / " +  c + " = " + (b / c));
        System.out.println("Módulo: " + b + " % " +  c + " = " + (b % c));

        System.out.println();

        /*
         * Operadores relacionales: para hacer comparaciones.
         * Tipos:
         *      -- Mayor que (>)
         *      -- Mayor o igual que (>=)
         *      -- Menor que (<)
         *      -- Menor o igual que (<=)
         *      -- Igual que (==)
         *      -- Distinto de (!=)
         */

        int d = 20;
        int e = 50;

        System.out.println("Operadores relacionales: para hacer comparaciones.");

        System.out.println("¿20 es mayor que 50? : " + (d > e));
        System.out.println("¿20 es mayor o igual que 50? : " + (d >= e));
        System.out.println("¿20 es menor que 50? : " + (d < e));
        System.out.println("¿20 es menor o igual que 50? : " + (d <= e));
        System.out.println("¿20 es igual que 50? : " + (d == e));
        System.out.println("¿20 es distinto de 50? : " + (d != e));

        System.out.println();

        /*
         * Operadores lógicos: Operan con valores lógicos para devolver nuevos valores lógicos.
         * Tipos:
         *      -- AND (&): Evalúa si las dos expresiones son verdaderas.
         *      -- AND en curtocircuíto (&&): No evalúa la segunda expresión si la primera es falsa.
         *      -- OR (|): Evalúa si alguna de las expresiones es verdadera.
         *      -- OR en curtocircuíto (||): No evalúa la segunda expresión si la primera es verdadera.
         *      -- NOT (!): Cambia el valor de la variable lógica.
         */

        boolean v = true;
        boolean f = false;

        System.out.println("Operadores lógicos: Operan con valores lógicos para devolver nuevos valores lógicos.");

        System.out.println("¿true es igual a false? : " + (v & f));
        System.out.println("¿true es igual a false? (cortocircuíto) : " + (v && f));
        System.out.println("¿true o false son verdaderas? : " + (v | f));
        System.out.println("¿true o false son verdaderas? (cortocircuíto) : " + (v || f));
        System.out.println("Cambiamos el valor de true : " + (!v));

        System.out.println();

        /*
         * Operador sobre cadenas de caracteres (+): Para concatenar cadenas de caracteres.
         */

        String text1 = "¡Hola, ";
        String text2 = "Mundo!";

        System.out.println("Operador sobre cadenas de caracteres:");

        System.out.println(text1 + text2);

        System.out.println();

        /*
         * Operadores de asignación: Para asignar un valor a una variable.
         * Tipos:
         *      -- +=: Suma a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- -=: Resta a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- *=: Multiplica a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- /=: Divide a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- %=: Realiza el módulo a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- &=: Realiza un AND lógico a la variable y sobrescribe el valor de la variable con el resultado.
         *      -- |=: Realiza un OR lógico a la variable y sobrescribe el valor de la variable con el resultado.
         */

        int i;
        boolean t = true;

        System.out.println("Operadores de asignación: Para asignar un valor a una variable.");

        System.out.println("Asignamos valor a la variable i = " + (i = 2));
        System.out.println("Suma y asigna: " + (i += 4));
        System.out.println("Resta y asigna: " + (i -= 3));
        System.out.println("Multiplica y asigna: " + (i *= 5));
        System.out.println("Divide y asigna: " + (i /= 3));
        System.out.println("Módulo y asigna: " + (i %= 3));
        System.out.println("AND lógico y asigna: " + (t &= true));
        System.out.println("OR lógico y asigna: " + (t |= false));

        System.out.println();

        /*
         * Operadores a nivel de bits: operan con cada bit del operando, ofreciendo un control más granular sobre los datos.
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

        System.out.println("x AND y : " + Integer.toBinaryString(x & y));
        System.out.println("x OR y : " + Integer.toBinaryString(x | y));
        System.out.println("x XOR y : " + Integer.toBinaryString(x ^ y));
        System.out.println("Complemento de x = " + Integer.toBinaryString(~x));
        System.out.println("Complemento de y = " + Integer.toBinaryString(~y));
        System.out.println("Desplazamiento de bits de x a la izquierda de 2: " + Integer.toBinaryString(x << 2));
        System.out.println("Desplazamiento de bits de x a la derecha de 1: " + Integer.toBinaryString(x >> 1));
        System.out.println("Desplazamiento de bits de x a la derecha de 2 (sin signo): " + Integer.toBinaryString(x >>> 1));

        System.out.println();

        /*
         * Excepciones
         * uso del try - catch
         */
        try {
            throw new Exception("Este es un ejemplo de excepción!");
        } catch (Exception error) {
            System.out.println("Exception: " + error.getMessage());
        }

        System.out.println();

        /*
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        System.out.println("DIFICULTAD EXTRA \n");

        System.out.println("Los números son: ");

        for (int j = 10; j <= 55; j++) {
            //Compruebo si son pares, distintos de 16 y no son múltiplos de 3
            if (j % 2 == 0 && j != 16 && j % 3 != 0) {
                System.out.println(j);
            }
        }


    }
}
