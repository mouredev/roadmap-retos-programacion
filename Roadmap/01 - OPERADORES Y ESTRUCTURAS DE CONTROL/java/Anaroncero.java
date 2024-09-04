/*
        * EJERCICIO:
        * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        * Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia,
        * bits...
        * (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
        * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
        * que representen todos los tipos de estructuras de control que existan
        * en tu lenguaje:
        * Condicionales, iterativas, excepciones...
        * - Debes hacer print por consola del resultado de todos los ejemplos.
        *
        * DIFICULTAD EXTRA (opcional):
        * Crea un programa que imprima por consola todos los números comprendidos
        * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        *
        * Seguro que al revisar detenidamente las posibilidades has descubierto algo
        * nuevo.

*/
public class Anaroncero {
    public static void main(String[] args) {

        /* Variables */
        int num1 = 2, num2 = 4;
        int resultado = 0;

        // Operaciones Aritmeticas
        System.out.println("-----Operaciones Aritmeticas----");

        System.out.println("Suma: " + (num1 + num2));
        System.out.println("Resta: " + (num1 - num2));
        System.out.println("Multiplicacion: " + (num1 * num2));
        System.out.println("Division: " + (num1 / num2));
        System.out.println("Resto: " + (num1 % num2));

        // Operaciones Logicas
        System.out.println("-----Operaciones Logicas----");
        boolean verdadero = true;
        boolean falso = false;

        // AND y
        System.out.println("AND"); // SE TIENEN QUE CUMPLIR AMBAS CONDICIONES
        System.out.println(false && false); // falso
        System.out.println(false && true); // falso
        System.out.println(true && true); // verdadero
        System.out.println(true && false); // falso

        // OR
        System.out.println("OR"); // SE TIENE QUE CUMPLIR UNA U OTRA CONDICION O AMBAS
        System.out.println(false || false); // falso
        System.out.println(false || true); // verdadero
        System.out.println(true || true); // verdadero
        System.out.println(true || false); // verdadero

        // NOT
        System.out.println("OR"); // AL REVES
        System.out.println(!true); // (!si no es verdadero) es falso
        System.out.println(!false); // (!si no es falso) es verdadero

        // Comparacion
        System.out.println("Comparacion");
        System.out.println(num1 == num2); // si son iguales
        System.out.println(num1 != num2); // si son diferentes
        System.out.println(num1 > num2); // si es mayor que
        System.out.println(num1 > num2); // menor que
        System.out.println(num1 > num2); // si es mayor o igual que
        System.out.println(num1 > num2); // si es menor o igual que

        // Asignacion
        System.out.println("Asignacion");
        System.out.println("Asignacion: " + (num1 = num2)); // el valor del numero 2 se pone tambien en el numero 1
        System.out.println("Suma y asignacion: " + (num1 += num2)); // num1 = num1 + num2;
        System.out.println("Resta y asignacion: " + (num1 -= num2)); // num1 = num1 - num2;
        System.out.println("Multiplicación y asignación: " + (num1 *= num2)); // num1 = num1 * num2;
        System.out.println("Division y asignación: " + (num1 /= num2)); // num1 = num1 / num2;
        System.out.println("Resto y asignación: " + (num1 %= num2)); // num1 = num1 % num2;

        System.out.println("AND y asignación: " + (num1 &= num2)); // hace la operacion AND en binario de num1 y num2 y
                                                                   // se lo asigna a num1
        System.out.println("OR y asignación: " + (num1 |= num2)); // hace la operacion OR en binario de num1 y num2 y se
                                                                  // lo asigna a num1
        System.out.println("XOR y asignación: " + (num1 ^= num2)); // hace la operacion XOR en binario de num1 y num2 y
                                                                   // se lo asigna a num1
        System.out.println("Desplazamiento a la izquierda y asignación: " + (num1 <<= num2)); // hace desplazamiento a
                                                                                              // la izquierda en binario
                                                                                              // de num1 y num2 y se lo
                                                                                              // asigna a num1
        System.out.println("Desplazamiento a la derecha y asignación aritmetico: " + (num1 >>= num2)); // hace
                                                                                                       // desplazamiento
                                                                                                       // a la derecha
                                                                                                       // manteniendo
                                                                                                       // signo en
                                                                                                       // binario de
                                                                                                       // num1 y num2 y
                                                                                                       // se lo asigna a
                                                                                                       // num1
        System.out.println("Desplazamiento a la derecha logico: " + (num1 >>>= num2)); // hace desplazamiento a la
                                                                                       // derecha en binario de num1 y
                                                                                       // num2 y se lo asigna a num1

        // Operaciones BIT a BIT
        int a = 2; // En binario: 0010
        int b = 4; // En binario: 0100
        /*
         * AND: Si coinciden dos 1 retorna 1, si no retorna 0.
         
          0010 (2 en binario)
          &
          0100 (4 en binario)
          ------
          0000 (0 en decimal)
          
         * OR: Almenos 1 debe ser un 1 para retornar un 1.
          
          0010 (2 en binario)
          |
          0100 (4 en binario)
          ------
          0110 (6 en decimal)
          
         * XOR: compara y si son diferentes retorna 1.
          0010 (2 en binario)
          ^
          0100 (4 en binario)
          ------
          0110 (6 en decimal)
          
         * NOT:
          1. Invierte todos los bits del número. 1 se convierte en 0 y cada 0 se
          convierte en 1.
          (numero 2)
          ~0000 0010
          ----------
          1111 1101
          
          2. Invertimos los bits del resultado (1111 1101) para obtener el complemento
          a uno
          y le sumamos 1:
          0000 0010
          +
          ----------
          0000 0011 (3 en decimal)
         
          3.Aplicamos el signo negativo
          -3
          
         * AHORA CON EL NUMERO 4
          1. Invierte todos los bits del número. 1 se convierte en 0 y cada 0 se
          convierte en 1.
          (numero 4)
          
          ~0000 0100
          ----------
          1111 1011
          
          2. Invertimos los bits del resultado (1111 1101) para obtener el complemento
          a uno
          y le sumamos 1:
          
          0000 0100
          + 1
          ----------
          0000 0101
          
          3.Aplicamos el signo negativo
          -5
          
          
         * DESPLAZAMIENTO A LA IZQUIERDA (<<):
          Los bits se desplazan dos posiciones a la izquierda, y se rellenan con ceros
          a la derecha.
          00000101 (5 en binario)
          << 2
          -----------
          00010100 (20 en decimal)
          
          
         * DESPLAZAMIENTO A LA DERECHA ARITMETICO (>>)
          Los bits se desplazan dos posiciones a la derecha, y se rellena con ceros a
          la izquierda.
          Mantiene el signo.
          
          00010100 (20 en binario)
          >> 2
          -----------
          00000101 (5 en decimal)
          
          
         * DESPLAZAMIENTO A LA DERECHA LOGICO (>>>)
          los bits se desplazan dos posiciones a la derecha, y se rellena con ceros a
          la izquierda.
          Siempre inserta 0.
          
          11110100 (-12 en binario en complemento a dos)
          >>> 2
          -----------
          00111101 (1073741813 en decimal, para un entero de 32 bits)
          
         */

        System.out.println("2 & 4 = " + (a & b)); // AND Bit a Bit
        System.out.println("2 | 4 = " + (a | b)); // OR Bit a Bit
        System.out.println("2 ^ 4 = " + (a ^ b)); // XOR Bit a Bit
        System.out.println("~2 = " + (~a)); // NOT Bit a Bit
        System.out.println("2 << 2 = " + (a << 2)); // Desplazamiento a la Izquierda
        System.out.println("4 >> 2 = " + (b >> 2)); // Desplazamiento a la Derecha Aritmético
        System.out.println("4 >>> 2 = " + (b >>> 2)); // Desplazamiento a la Derecha Lógico


        // Estructuras de control
        System.out.println("Ternarios: ");
        int edad = 18;
        String comprobacion = edad >= 18 ? "Es mayor de edad " : "NO es mayor de edad";
        System.out.println(comprobacion);

        System.out.println("IF ELSE, SWITCH");
        System.out.println("ejemplo IF ELSE");
        if (edad >= 18) {
            System.out.println("es mayor de edad");
        } else if (edad >= 99) {
            System.out.println("esta persona problablemente este muerta");
        } else {
            System.out.println("es menor de edad");
        }


        System.out.println("Ejemplo switch");
        switch (num1) {
            case 1:
                System.out.println("num1 es un 1");
                break;
            case 2:
                System.out.println("num1 es un 2");
                break;

            default:
                System.out.println("el num1 no es 1 ni es 2 es otro numero");
        }


    
        System.out.println("Bucles");
        System.out.println("For"); /* Bucle que se repite x numero de veces */
        for (int i = 0; i < 10; i++) { // se va a repetir 10 veces desde 0-9 incrementandose
            System.out.println("i = " + i);
        }

        System.out.println("While"); /* Bucle que se repite hasta se cumpla la condicion */
        int contador = 0;
        while (contador < 10) { // se va a ejecutar mietras contador sea menor que 10
            System.out.println("i = " + contador);
            contador++; // al poner que el contador se incremente en cada interaccion el valor de
                        // contador ira cambiando y cuando llegue a 10 se rompera el bucle
        }

        System.out.println(" do while"); // Haz esto(do) hasta que(while)
        do {
            System.out.println("i = " + contador); /* incrementa la varibale en cada vuelta */
            contador++;
        } while (contador < 2); /* cuando llega al 2 se para */

        System.out.println("Break y continue se usan en for, while y do-while");
        System.out.println("Break es para romper un bucle");

        int numero_indicado = 4;
        for (int i = 0; i < 10; i++) {
            if (i == numero_indicado) {
                break; /*
                        * Cuando llega al numero indicado el buqle
                        * se rompe y no muestra la siguiente interaccion
                        */
            }
            System.out.println("i = " + i);
        }

        System.out.println("Continue es para continuar con la siguiente interaccion y dejar la actual");
        for (int i = 0; i < 10; i++) {
            if (i == numero_indicado) {
                continue; /*
                           * Cuando llega al numero indicado el buqle se rompe
                           * y continua con la siguiente interaccion
                           */
            }
            System.out.println("i = " + i);
        }



        System.out.println("Manejar excepciones try-catch");
        try {
            resultado = num1 / 0; // 0/0
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division por cero");
        }



        // ejercicio extra
        for (int i = 10; i < 55; i++) {
            // si es par
            if (i % 2 == 0) {
                // y no es 16 ni multiplo de 3
                if (i != 16 && i % 3 != 0) {
                    System.out.println(i);
                }
            }
        }
    }

}
