/*
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
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

import java.util.List;

public class JesusEs1312 {

        public static void main(String[] args) {
                int a = 10;
                int b = 5;
                String aString = String.valueOf(a);
                String bString = String.valueOf(b);

                // --- Operadores Aritmeticos
                System.out.println("===Operadores Aritmeticos===");
                // Suma
                System.out.println(
                                "Suma de ".concat(aString)
                                                .concat(" + ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a + b)));
                // Resta
                System.out.println(
                                "Resta de ".concat(aString)
                                                .concat(" - ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a - b)));
                // Multiplicación
                System.out.println(
                                "Multiplicación de ".concat(aString)
                                                .concat(" * ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a * b)));
                // División
                System.out.println(
                                "División de ".concat(aString)
                                                .concat(" / ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a / b)));
                // Residuo
                System.out.println(
                                "Residuo de ".concat(aString)
                                                .concat(" % ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a % b)));
                // Exponenciación
                double exponente = Math.pow(b, a);
                System.out.println("Exponenciación de b a la a: ".concat(String.valueOf(exponente)));

                // --- Operadores de Igualdad o Relación
                System.out.println("===Operadores de igualdal o Relelación===");
                // Igual a
                System.out.println(
                                aString.concat(" == ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(aString.equals(bString))));
                // Diferente de
                System.out.println(
                                aString.concat(" != ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(!aString.equals(bString))));
                // Mayor que
                System.out.println(
                                aString.concat(" > ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a > b)));
                // Menor que
                System.out.println(
                                aString.concat(" < ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a < b)));
                // Mayor o igual que
                System.out.println(
                                aString.concat(" >= ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a >= b)));
                // Menor o igual que
                System.out.println(
                                aString.concat(" <= ")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a <= b)));
                // --- Operadores Aritméticos Incrementales
                System.out.println("===Operadores Aritméticos Incrementales===");
                // Incremento
                System.out.println(
                                "Incremento de ++".concat(aString)
                                                .concat(": ")
                                                .concat(String.valueOf(++a)));
                // Decremento
                System.out.println(
                                "Decremento de --".concat(String.valueOf(a))
                                                .concat(": ")
                                                .concat(String.valueOf(--a)));

                // --- Operadores Aritméticos Combinados
                System.out.println("===Operadores Aritméticos Combinados===");
                // Suma combinada
                System.out.println(
                                "Suma combinada ".concat(aString)
                                                .concat("+=")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a += b)));
                // Resta combinada
                System.out.println(
                                "Resta combinada ".concat(aString)
                                                .concat("-=")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a -= b)));
                // Producto combinado
                System.out.println(
                                "Suma combinada ".concat(aString)
                                                .concat("*=")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a *= b)));
                // División combinada
                System.out.println(
                                "Suma combinada ".concat(aString)
                                                .concat("/=")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a /= b)));
                // Residuo combinada
                System.out.println(
                                "Residuo combinado ".concat(aString)
                                                .concat("%=")
                                                .concat(bString)
                                                .concat(": ")
                                                .concat(String.valueOf(a %= b)));
                a = 5;

                // --- Operadores Lógicos
                // Negación NOT
                System.out.println("===Operadores Lógicos===");
                System.out.println(
                                " !(".concat(bString)
                                                .concat("==")
                                                .concat(aString)
                                                .concat("): ")
                                                .concat(String.valueOf(!(a == b))));
                // OR
                System.out.println("(5==10) || (10 > 5): ".concat(String.valueOf((a == b) || (b > a))));

                // AND
                System.out.println("(5==10) && (10 > 5): ".concat(String.valueOf((a == b) && (b > a))));

                // --- Operador condicional o ternario
                System.out.println("===Operador condicional o ternario===");
                System.out.println("(10 > 5): ".concat(b > a ? "true" : "false"));

                // --- Operadores de Bit
                System.out.println("===Operadores de Bit===");
                // Negación
                System.out.println("Negación (~5): ".concat(String.valueOf(~a)));
                // Suma lógica binaria
                System.out.println("Suma binaria (5|10): ".concat(String.valueOf(a | b)));
                // Suma lógica exclusiva
                System.out.println("Suma exclusiva (5^10): ".concat(String.valueOf(a ^ b)));
                // Producto lógico binario
                System.out.println("Producto lógico (5&10): ".concat(String.valueOf(a & b)));
                // Desplaza a la izquierda los bits
                System.out.println("Desplaza a la izquierda los bits (10 << 5): ".concat(String.valueOf(b << a)));
                // Desplaza a la derecha los bits
                System.out.println("Desplaza a la izquierda los bits (10 >> 5): ".concat(String.valueOf(b >> a)));

                // --- Estructuras de Control
                // if, else if, else
                System.out.println("===Estructura de control if, else if y else===");
                if (b > a) {
                        System.out.println("b es mayor que a");
                } else if (a == b) {
                        System.out.println("a es igual a b");
                } else {
                        System.out.println("a es mayor que b");
                }

                // For
                System.out.println("===Estructura de control (for)===");
                String[] arrayOne = { "hola ", "mundo ", "desde ", "Java" };
                for (int i = 0; i < arrayOne.length; i++) {
                        System.out.print(arrayOne[i]);
                }
                System.out.println("");
                // while
                System.out.println("===Estructura de control (While)===");
                int i = 0;
                while (i < arrayOne.length) {
                        System.out.print(arrayOne[i]);
                        i++;
                }
                System.out.println("");
                // Do while
                System.out.println("===Estructura de control (do while)===");
                do {
                        System.out.println(arrayOne[i - 1]);
                } while (i < arrayOne.length);
                // switch
                System.out.println("===Estructura de control (switch)===");
                switch (a) {
                        case 5:
                                System.out.println("Entro en caso 5");
                                break;
                        case 10:
                                System.out.println("Entro en caso 10");
                                break;
                        default:
                                System.out.println("No entro en ningun caso " + String.valueOf(a));
                                break;
                }

                // ---Ejercicio Extra
                System.out.println("===Ejercicio Extra===");
                int[] arraySecond = new int[46];
                int k = 10;
                for (int j = 0; j < arraySecond.length; j++) {
                        arraySecond[j] = k;
                        k++;
                }

                for (int l : arraySecond) {
                        if ((l % 2 == 0) && (l % 3 != 0) && (l != 16)) {
                                System.out.println(l);
                        }
                }
        }

}