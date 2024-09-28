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

public class Alextc35 {
        public static void main(String[] args) {

                // \n <- Salto de línea
                // \t <- Tabulación

                // 1. 2. 3.

                // Operadores Aritméticos
                System.out.println("-------------------------------------------------------------");
                System.out.println("\tOPERADORES ARITMÉTICOS");
                System.out.println("-------------------------------------------------------------");

                int x = 7;
                int y = 5;

                // Suma
                int z = x + y;
                System.out.println("\nSuma de " + x + " + " + y + " = " + z);

                // Resta
                z = x - y;
                System.out.println("\nResta de " + x + " - " + y + " = " + z);

                // Multiplicación
                z = x * y;
                System.out.println("\nMultiplicación de " + x + " * " + y + " = " + z);

                // División (entera)
                z = x / y;
                System.out.println("\nDivisón entera de " + x + " / " + y + " = " + z);

                // División (real)
                double j = (double) x / y;
                System.out.println("\nDivisón real de " + x + " / " + y + " = " + j);

                // Resto
                z = x % y;
                System.out.println("\nResto de " + x + " % " + y + " = " + z);

                // Incrementos
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tINCREMENTOS");
                System.out.println("-------------------------------------------------------------");

                // x++
                System.out.println("\n\t\tx++");
                System.out.println("Sin incremento x = " + x);
                z = x++; // z tiene el valor de x sin incrementar
                System.out.println("Con incremento x = " + x + "\nz = " + z);

                // ++x
                System.out.println("\n\t\t++x");
                x = 7;
                System.out.println("Sin incremento x = " + x);
                z = ++x;
                System.out.println("Con incremento x = " + x + "\nz = " + z);

                // Decrementos
                System.out.println("-------------------------------------------------------------");
                System.out.println("\tDECREMENTOS");
                System.out.println("-------------------------------------------------------------");

                // x--
                System.out.println("\n\t\tx--");
                x = 7;
                System.out.println("Sin decremento x = " + x);
                z = x--;
                System.out.println("Con decremento x = " + x + "\nz = " + z);

                // --x
                System.out.println("\n\t\t--x");
                x = 7;
                System.out.println("Sin decremento x = " + x);
                z = --x;
                System.out.println("Con decremento x = " + x + "\nz = " + z);

                // Asignación
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tASIGNACIÓN");
                System.out.println("-------------------------------------------------------------");

                x = 20;
                System.out.println("\tx = 20");

                // x = x + 5
                x += 5;
                System.out.println("x += 5 -> x = " + x);

                // x = x - 3
                x -= 3;
                System.out.println("x -= 3 -> x = " + x);

                // x = x * 2
                x *= 2;
                System.out.println("x *= 2 -> x = " + x);

                // x = x / 4
                x /= 4;
                System.out.println("x /= 4 -> x = " + x);

                // x = x % 3
                x %= 3;
                System.out.println("x %= 3 -> x = " + x);

                // Operadores de Pertenencia (simulación)
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tOPERADOR DE PERTENENCIA");
                System.out.println("-------------------------------------------------------------\n");

                int[] array = {1, 2, 3, 4, 5};
                boolean isInArray = false;
                for (int i : array) {
                        if (i == 3) {
                                isInArray = true;
                                break;
                        }
                }
                System.out.println("¿3 está en el array?: " + isInArray);

                // Operadores a nivel de Bits
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tOPERADORES A NIVEL DE BITS");
                System.out.println("-------------------------------------------------------------");

                int bitmask = 0b0011;
                int val = 0b1111;

                // AND
                int res = val & bitmask;
                System.out.println("\n1111 AND 0011 = " + Integer.toBinaryString(res));

                // OR exclusivo
                res = val ^ bitmask;
                System.out.println("\n1111 OR exclusivo 0011 = " + Integer.toBinaryString(res));

                // OR inclusivo
                res = val | bitmask;
                System.out.println("\n1111 OR inclusivo 0011 = " + Integer.toBinaryString(res));

                System.out.println("\n-------------------------------------------------------------");
                // 0b1111
                System.out.println("\n\t1111");

                // Desplazamiento a la izquierda
                res = val << 1; // 11110
                System.out.println("\nDesplazamiento a la izquierda = " + Integer.toBinaryString(res));

                // Desplazamiento a la derecha con signo
                res = val >> 2; // 0011
                System.out.println("\nDesplazamiento a la derecha con signo = " + Integer.toBinaryString(res));

                // Desplazamiento a la derecha con el signo en el negativo
                res = (-val) >> 2; // 11111111111111111111111111111100
                System.out.println("\nDesplazamiento a la derecha con Signo (Negativo) = "
                                + Integer.toBinaryString(res));

                // Desplazamiento a la derecha sin signo
                res = val >>> 1; // 111
                System.out.println("\nDesplazamiento a la derecha sin signo = " + Integer.toBinaryString(res));

                // Inverso o Commplementario a 1
                res = ~val; // 11111111111111111111111111110000
                System.out.println("\nInverso o Complementario a 1 = " + Integer.toBinaryString(res));

                // Operadores Lógicos Condicionales
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tOPERADORES LÓGICOS CONDICIONALES");
                System.out.println("-------------------------------------------------------------\n");

                int valor1 = 1;
                int valor2 = 2;

                // AND
                if ((valor1 == 1) && (valor2 == 2)) {
                        System.out.println("(valor1 es 1) AND (valor2 es 2)");
                }

                // OR
                if ((valor1 == 1) || (valor2 == 1)) {
                        System.out.println("\n(valor1 es 1) OR (valor2 es 1)");
                }

                // NOT
                if (valor1 != 2) {
                        System.out.println("\n(valor1 es distinto de 2)");
                }

                // Operador de Identidad
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tOPERADOR DE IDENTIDAD");
                System.out.println("-------------------------------------------------------------\n");

                Integer int1 = 100;
                Integer int2 = 100;

                System.out.println("int1 == int2: " + (int1 == int2)); // Identidad (valores)
                System.out.println("num1.equals(int2): " + (int1.equals(int2))); // Comparación de contenido
                System.out.println("num1 != num2: " + (int1 != int2)); // Diferente identidad (valores)

                // Operador Ternario
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tOPERADOR TERNARIO");
                System.out.println("-------------------------------------------------------------\n");

                int result;
                boolean someCondition = false;

                System.out.println("valor1: " + valor1 
                        + "\nvalor2: " + valor2
                        + "\n\tSi es true: valor1"
                        +"\n\tSi es false: valor2");

                // La condición es falsa, por lo tanto result = valor2 = 2
                result = someCondition ? valor1 : valor2; // variable = (condición) ? valorSiVerdadero : valorSiFalso

                System.out.println("\nEs false: " + result);

                // Operadores Lógicos Relacionales
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tOPERADORES LÓGICOS RELACIONALES");
                System.out.println("-------------------------------------------------------------");

                // Igual
                if (valor1 == valor2)
                        System.out.println("\nvalor1 == valor2"); // valor1 igual a valor2

                // Distinto
                if (valor1 != valor2)
                        System.out.println("\nvalor1 != valor2"); // valor1 distinto de valor2

                // Mayor que
                if (valor1 > valor2)
                        System.out.println("\nvalor1 > valor2"); // valor1 mayor que valor2

                // Menor que
                if (valor1 < valor2)
                        System.out.println("\nvalor1 < valor2"); // valor1 menor que valor2

                // Menor o Igual que
                if (valor1 <= valor2)
                        System.out.println("\nvalor1 <= valor2"); // valor1 menor o igual que valor2

                // Mayor o Igual que
                if (valor1 >= valor2)
                        System.out.println("\nvalor1 >= valor2"); // valor1 mayor o igual que valor2

                // Casting
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tCASTING");
                System.out.println("-------------------------------------------------------------\n");

                int adiv = 5; // Divisor
                int bden = 9; // Denominador

                System.out.println(adiv + " / " + bden + " = " + (double) adiv / bden);

                System.out.println("\n-------------------------------------------------------------");
                
                // Sentencia
                int numero; // También llamado línea de código

                // Expresiones
                System.out.println("\tEXPRESIONES");
                System.out.println("-------------------------------------------------------------");

                numero = 1 + 2; // Expresión
                System.out.println("\nLa suma de 1 + 2 es: " + numero);

                numero = (1 + 2) * 3; // Expresión compuesta
                System.out.println("\nLa operación de (1 + 2) * 3 es: " + numero);

                // Bloque de Código
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tBLOQUE DE CÓDIGO");
                System.out.println("-------------------------------------------------------------");

                boolean condicion = true;

                if (condicion) {
                        System.out.println("\nLa condición es verdadera");
                } else {
                        System.out.println("\nLa condición es falsa");
                }

                // Estructura de Decisión
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tESTRUCTURA DE DECISIÓN");
                System.out.println("-------------------------------------------------------------\n");
                
                // Esctructura if-then
                System.out.println("\tESTRUCTURA IF-THEN");
                int num1 = 5, num2 = 4;
                if (num1 > num2) {
                        System.out.println("num1 es mayor que num2\n");
                }

                // Estructura if-else
                System.out.println("\tESTRUCTURA IF-ELSE");
                num1 = 25;
                num2 = 21;
                if (num1 > num2) {
                        System.out.println("El número mayor es " + num1 + "\n");
                } else {
                        System.out.println("El número mayor es " + num2 + "\n");
                }

                // Estructura if-else-if
                System.out.println("\tESTRUCTURA IF-ELSE-IF");
                float puntuacion = 5.6f;
                if (puntuacion >= 9) {
                        System.out.println("Tienes un SOBRESALIENTE\n");
                } else if (puntuacion >= 7) {
                        System.out.println("Tienes un NOTABLE\n");
                } else if (puntuacion >= 5) {
                        System.out.println("Tienes un APROBADO\n");
                } else {
                        System.out.println("Tienes un SUSPENSO\n");
                }

                // Estructura switch
                System.out.println("\tESTRUCTURA SWITCH");
                int mes = 8;
                String mesString;
                switch (mes) {
                        case 1:
                                mesString = "Enero"; // mes == 1 -> True
                                break;
                        case 2:
                                mesString = "Febrero";
                                break;
                        case 3:
                                mesString = "Marzo";
                                break;
                        case 4:
                                mesString = "Abril";
                                break;
                        case 5:
                                mesString = "Mayo";
                                break;
                        case 6:
                                mesString = "Junio";
                                break;
                        case 7:
                                mesString = "Julio";
                                break;
                        case 8:
                                mesString = "Agosto";
                                break;
                        case 9:
                                mesString = "Septiembre";
                                break;
                        case 10:
                                mesString = "Octubre";
                                break;
                        case 11:
                                mesString = "Noviembre";
                                break;
                        case 12:
                                mesString = "Diciembre";
                                break;
                        default:
                                mesString = "Mes no válido";
                                break;
                }
                System.out.println(mesString + "\n");

                // Otra estructura switch
                System.out.println("\tOTRA ESTRUCTURA SWITCH");
                mes = 2;
                int numDias = 0;
                switch (mes) {
                        case 1:
                        case 3:
                        case 5:
                        case 7:
                        case 8:
                        case 10:
                        case 12:
                                numDias = 31;
                                break;
                        case 4:
                        case 6:
                        case 9:
                        case 11:
                                numDias = 30;
                                break;
                        case 2:
                                numDias = 28;
                                break;
                        default:
                                System.out.println("Mes no válido\n");
                                break;
                }
                System.out.println("Número de días = " + numDias + "\n");

                // Bucles
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tBUCLES");
                System.out.println("-------------------------------------------------------------\n");

                // Bucle while
                System.out.println("\tBUCLE WHILE");
                int contador = 1;
                while (contador < 11) {
                        System.out.println("Contador vale: " + contador);
                        contador++;
                }

                // Bucle do-while
                System.out.println("\n\tBUCLE DO-WHILE");
                contador = 1;
                do {
                        System.out.println("Contador vale: " + contador);
                        contador++;
                } while (contador < 11);

                // Bucle for
                System.out.println("\n\tBUCLE FOR");
                for (int auxiliar = 1; auxiliar < 11; auxiliar++) {
                        System.out.println("Contador vale: " + auxiliar);
                }

                // Excepciones
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tEXCEPCIONES");
                System.out.println("-------------------------------------------------------------\n");
                
                // try-catch
                System.out.println("\tTRY-CATCH");
                try {
                        result = 10 / 0;
                } catch (ArithmeticException e) {
                        System.out.println("Error: División por cero.");
                }

                // try-finally
                System.out.println("\n\tTRY-FINALLY");
                try {
                        System.out.println("Código a probar");
                } finally {
                        System.out.println("Siempre se ejecuta `finally`");
                }

                // Opcional
                System.out.println("\n-------------------------------------------------------------");
                System.out.println("\tOPCIONAL");
                System.out.println("-------------------------------------------------------------\n");

                /* i comienza siendo 10 y el 56 pibota cortando el bucle cuando llegue a i = 55,
                /* por cada vuelta se suma +1 a i.
                 */
                for (int i = 10; i <= 55; i++) {
                        // i tiene que ser par, distinto de 16 y que no sea múltiplo de 3.
                        if ((i % 2 == 0) && (i != 16) && (i % 3 != 0)) {
                                System.out.print(i + " ");
                        }
                }
                System.out.println();
        }
}