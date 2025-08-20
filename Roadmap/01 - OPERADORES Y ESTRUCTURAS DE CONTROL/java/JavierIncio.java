import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * #01 OPERADORES Y ESTRUCTURAS DE CONTROL
 *
 * @author JavierIncio
 * @version 1.0
 *
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

public class JavierIncio {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("########## OPERADORES ARITMÉTICOS ##########");
        int numero = 5;
        System.out.println("===== Suma =====");
        int suma = numero + 5;
        System.out.println("suma = " + suma);

        System.out.println("===== Resta =====");
        int resta = numero - 5;
        System.out.println("resta = " + resta);

        System.out.println("===== Multiplicación =====");
        int mult = numero * 5;
        System.out.println("mult = " + mult);

        System.out.println("===== División =====");
        int div = numero / 5;
        System.out.println("div = " + div);

        System.out.println("===== Módulo =====");
        int mod = numero % 2;
        System.out.println("mod = " + mod);

        System.out.println("===== Incremento =====");
        System.out.println("numero = " + numero);
        System.out.println("numero++ = " + numero++);
        System.out.println("numero = " + numero);
        System.out.println("++numero = " + ++numero);
        System.out.println("numero = " + numero);

        System.out.println("===== Decremento =====");
        numero = 5;
        System.out.println("numero = " + numero);
        System.out.println("numero-- = " + numero--);
        System.out.println("numero = " + numero);
        System.out.println("--numero = " + --numero);
        System.out.println("numero = " + numero);

        System.out.println("\n########## OPERADORES ASIGNACIÓN ##########");
        System.out.println("===== '=' =====");
        System.out.println("numero = 10 -> numero = " + (numero = 10));

        System.out.println("===== '+=' =====");
        System.out.println("numero += 10 -> numero = " + (numero += 10));

        System.out.println("===== '-=' =====");
        System.out.println("numero -= 10 -> numero = " + (numero -= 10));

        System.out.println("===== '*=' =====");
        System.out.println("numero *= 10 -> numero = " + (numero *= 10));

        System.out.println("===== '/=' =====");
        System.out.println("numero /= 10 -> numero = " + (numero /= 10));

        System.out.println("===== '%=' =====");
        System.out.println("numero %= 10 -> numero = " + (numero %= 10));

        System.out.println("\n########## OPERADORES RELACIONALES ##########");
        int a = 3;
        int b = 5;

        System.out.println("===== '==' =====");
        System.out.println(a + " == " + b + " -> " + (a == b));

        System.out.println("===== '!=' =====");
        System.out.println(b + " != " + b + " -> " + (b != b));

        System.out.println("===== '<' =====");
        System.out.println(b + " < " + a + " -> " + (b < a));

        System.out.println("===== '>' =====");
        System.out.println(a + " > " + b + " -> " + (a > b));

        System.out.println("===== '<=' =====");
        System.out.println(b + " <= " + a + " -> " + (b <= a));

        System.out.println("===== '>=' =====");
        System.out.println(a + " >= " + a + " -> " + (a >= a));

        System.out.println("\n########## OPERADORES LÓGICOS ##########");
        int x = 10;
        System.out.println("x = " + x);
        System.out.println("===== '&&' =====");
        System.out.println("(x > 5 && x < 20) -> " + (x > 5 && x < 20));

        System.out.println("===== '||' =====");
        System.out.println("(x < 5 || x == 10) -> " + (x < 5 || x == 10));

        System.out.println("===== '!' =====");
        System.out.println("!(x == 10) -> " + !(x == 10));

        System.out.println("\n########## OPERADORES BITWISE ##########");
        a = 5;
        b = 3;
        System.out.println("a = " + a + " (0101)");
        System.out.println("b = " + b + " (0011)");

        System.out.println("===== AND '&' =====");
        // Devuelve 1 si ambos bits son 1. Si no, devuelve 0.
        System.out.println("a & b = " + (a & b) + " (0001)");

        System.out.println("===== OR '|' =====");
        // Devuelve 1 si alguno de los bits es 1.
        System.out.println("a | b = " + (a | b) + " (0111)");

        System.out.println("===== XOR '^' =====");
        // Devuelve 1 si los bits son diferentes. Devuelve 0 si los bits son iguales.
        System.out.println("a ^ b = " + (a ^ b) + " (0110)");

        System.out.println("===== NOT '~' =====");
        // Invierte cada bit: los 0 pasan a 1 y los 1 pasan a 0.
        // Como Java usa complemento a dos, al aplicar ~ a un número se obtiene el negativo + (-1).
        System.out.println("a = " + a + " (00000000 00000000 00000000 00000101)");
        System.out.println("~a = " + (~a) + " (11111111 11111111 11111111 11111010)");

        System.out.println("===== Desplazamiento a la izquierda '<<' =====");
        // Mueve todos los bits a la izquierda y rellena con 0 a la derecha.
        // Equivale a multiplicar por 2^n.
        System.out.println("a = " + a + " (0101)");
        System.out.println("a << 3 = " + (a << 3) + " (00101000)");

        System.out.println("===== Desplazamiento a la derecha con signo '>>' =====");
        // Mueve todos los bits a la derecha y rellena con el bit del signo por la izquierda.
        // Equivale a dividir entre 2^n.
        a = 10;
        b = -8;
        System.out.println("a = " + a + " (1010)");
        System.out.println("a >> 1 = " + (a >> 1) + " (0101)");

        System.out.println("\nb = " + b + " (11111111 11111111 11111111 11111000)");
        System.out.println("b >> 2 = " + (b >> 2) + " (11111111 11111111 11111111 11111110)");

        System.out.println("===== Desplazamiento a la derecha sin signo '>>>' =====");
        // Similar a >>, pero siempre rellena con ceros a la izquierda.
        // El signo ya no se conserva: si era negativo, pasa a un número positivo muy grande.
        a = 40;
        b = -40;
        System.out.println("a = " + a + " (00101000)");
        System.out.println("a >> 2 = " + (a >> 2) + " (1010)");
        System.out.println("a >>> 2 = " + (a >>> 2) + " (1010)");

        System.out.println("\nb = " + b + " (11111111 11111111 11111111 11011000)");
        System.out.println("b >> 2 = " + (b >> 2) + " (11111111 11111111 11111111 11110110)");
        System.out.println("b >>> 2 = " + (b >>> 2) + " (00111111 11111111 11111111 11110110)");

        System.out.println("\n########## OPERADOR COMPROBACIÓN DE TIPO ##########");
        String texto = "Cadena de texto";
        System.out.println("texto = " + texto);
        System.out.println("texto instanceof String -> " + (texto instanceof String));

        System.out.println("\n########## ESTRUCTURAS DE CONTROL ##########");
        System.out.println("===== 'if - else if - else' =====");
        String email = "username@email.com";

        System.out.println("Introduce un email: ");
        String emailInput = sc.next();

        if (emailInput.equals(email)){
            System.out.println("¡Bienvenido!");
        }else if (!emailInput.contains(String.valueOf('@'))) {
            System.out.println("Formato incorrecto: debe contener '@'");
        }else {
            System.out.println("Email incorrecto");
        }

        System.out.println("\t########## OPERADOR TERNARIO ##########");
        a = 56;
        b = 23;
        System.out.println("\ta = " + a + "\tb = " + b);
        int resultado = (a > b) ? a : b;
        System.out.println("\tImprime el número mayor = " + resultado);

        System.out.println("===== 'switch' =====");
        System.out.println("Introduce un día de la semana en formato numérico: ");
        int dia = sc.nextInt();
        switch (dia){
            case 1 -> System.out.println("Lunes");
            case 2 -> System.out.println("Martes");
            case 3 -> System.out.println("Miércoles");
            case 4 -> System.out.println("Jueves");
            case 5 -> System.out.println("Viernes");
            case 6 -> System.out.println("Sábado");
            case 7 -> System.out.println("Domingo");
            default -> System.out.println(dia + " no es un día de la semana");
        }

        System.out.println("===== 'while' =====");
        String userPass = "pass1234";
        System.out.println("Introduce contraseña: ");
        String pass = sc.next();
        while (!pass.equals(userPass)){
            System.out.println("Introduce contraseña: ");
            pass = sc.next();
        }

        System.out.println("===== 'do-while' =====");
        do {
            System.out.println("Introduce contraseña: ");
            pass = sc.next();
        }while (!pass.equals(userPass));

        System.out.println("===== 'for' =====");
        int[] numeros = {1,4,6,7,32,5,3,2,453,34};
        for (int i = 0; i < numeros.length; i++){
            System.out.print(numeros[i] + " ");
        }
        System.out.println();

        System.out.println("===== 'foreach' =====");
        for (int num : numeros){
            System.out.print(num + " ");
        }
        System.out.println();

        System.out.println("===== 'Excepciones' =====");
        int codigoPin = 1234;
        try {
            System.out.println("Introduce el pin:");
            int pin = sc.nextInt();
        } catch (InputMismatchException e) {
            System.err.println("Debes introducir un numero entero");
        } catch (Exception e) {
            System.err.println(e.getMessage());
        } finally {
            System.out.println("¡Gracias!");
        }

        System.out.println("\n########## EJERCICIO EXTRA ##########");
        final int INCIO = 10;
        final int FIN = 55;

        for (int i = INCIO; i <= FIN; i++){
            if ( (i % 2 == 0) && (i != 16) && (i % 3 != 0) ){
                System.out.print(i + " ");
            }
        }
    }
}