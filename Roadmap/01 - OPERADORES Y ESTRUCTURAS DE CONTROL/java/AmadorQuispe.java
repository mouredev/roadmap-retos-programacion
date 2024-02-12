public class AmadorQuispe {

    public static void main(String[] args) {
        assignmentOperator();
        arithmeticOperators();
        unaryOperators();
        equalityRelationalOperators();
        conditionalOperators();
        bitwiseOperators();
        System.out.println("FLUJOS DE CONTROL");
        System.out.println("-------------------");

        // if else
        String name = "Alex";
        int age = 20;
        // con podemos imprimir por pantalla si Alex es mayor de edad (se considera
        // mayor de edad, tine mas de 18 años )
        if (age > 18) {
            System.out.println(name + " es mayor de edad");
        }
        // if else
        // en el ejemplo anterior podemos imprimir por pantall si no es mayor de edad
        if (age > 18) {
            System.out.println(name + " es mayor de edad");
        } else {
            System.out.println(name + " no es mayor de edad");
        }
        // While, ejecuta un bloque hasta que la condición sea falta
        // ejemplo: imprimimos la multiplicacion del numero 2 hasta 12
        int number = 0;
        while (number <= 12) {
            System.out.println("2 x " + number + " = " + 2 * number);
            number++;
        }
        // do while, por lo menos se ejecuta una vez, y luego comprueba la condición y
        // repita que la condición sea
        // falsa

        int j = 1;
        do {
            System.out.println(j);
            j++;
        } while (j <= 10);

        // for, utilizado cuando se quiere ejecutar un determinado de veces (se conoce
        // inicio y fin)
        // imprimir tabla de 5
        for (int i = 0; i < 10; i++) {
            System.out.println("5 x " + i + " = " + 5 * i);
        }
        // switch,permite ejecutar diferentes bloques de código según el valor de una
        // variable
        int dayWeek = 3;
        switch (dayWeek) {
            case 1:
                System.out.println("Lunes");
                break;
            case 2:
                System.out.println("Martes");
                break;
            case 3:
                System.out.println("Miércoles");
                break;
            default:
                System.out.println("Día no válido");
                break;
        }

        // break y continue, se utilizan dentro de los bucles y modifican el flujo
        // natural de los mismos.

        // continue, finaliza la iteración que en ese momento se está ejecutando

        for (int i = 1; i <= 5; i++) {
            // Saltar la iteración si el número es par
            if (i % 2 == 0) {
                System.out.println("Número par encontrado: " + i);
                continue; // Salta al siguiente valor de i sin ejecutar el código restante en el bucle
            }

            // Este código solo se ejecutará para números impares
            System.out.println("Número impar: " + i);
        }

        // Exception
        try {
            String[] students = { "Alex", "Pedro", "Juan", "Marco" };
            System.out.println(students[5]);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        /*
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }

    }

    /*
     * OPERADOR ASIGNACIÓN
     */
    private static void assignmentOperator() {
        System.out.println("OPERADOR ASIGNACIÓN");
        System.out.println("-----------------");
        // El operador asignación =, es un operador binario que asigna el valor del
        // término de la derecha al operando de la izquierda.
        int n;
        // (=) asignación
        n = 10;
        System.out.println("i = " + n);
        System.out.println("ASIGNACIÓN COMBINADO CON OPERADORES ARITMÉTICOS");
        System.out.println("-----------------------------");
        // (+=) suma en asignación.
        n += 2;//
        System.out.println("El valor de n es: " + n);
        // (-=) resta en asignación.
        n -= 2;//
        System.out.println("El valor de n es: " + n);
        // (*=) producto en asignación.
        n *= 2;//
        System.out.println("El valor de n es: " + n);
        // (/=) división en asignación.
        n /= 2;//
        System.out.println("El valor de n es: " + n);
        // (%=) módulo en asignación.
        n %= 2;//
        System.out.println("El valor de n es: " + n);
    }

    /*
     * OPERADORES ARITMÉTICOS
     */
    private static void arithmeticOperators() {
        System.out.println("OPERADORES ARITMÉTICOS");
        System.out.println("--------------------");
        // Operadores aritméticos.

        float number1 = 10;
        float number2 = 3;
        // + Operador de suma (también utilizado para la concatenación de cadenas)
        System.out.println("SUMA");
        System.out.println("La suma de :" + number1 + " y " + number2 + " es: " + (number1 + number2));
        // - Operador de resta
        System.out.println("RESTA");
        System.out.println("La resta de :" + number1 + " y " + number2 + " es: " + (number1 - number2));
        // '* Operador de multiplicación
        System.out.println("MULTIPLICACION");
        System.out.println("La multiplicación de :" + number1 + " y " + number2 + " es: " + (number1 * number2));
        // / Operador de división
        System.out.println("DIVISION");
        System.out.println("La división de :" + number1 + " y " + number2 + " es: " + (number1 / number2));
        // % Operador de resto
        System.out.println("MODULO");
        System.out.println("El resto de :" + number1 + " y " + number2 + " es: " + (number1 % number2));
    }

    /*
     * OPERADORES UNARIOS.
     */
    private static void unaryOperators() {
        System.out.println("OPERADORES UNARIOS");
        System.out.println("--------------------");

        int value = +5;

        // Operador unario más(+) ; Representa un valor positivo (sin embargo, los
        // números son positivos sin esto)
        System.out.println("El valor de 'value' es: " + value);

        // Operador de incremento (++); incrementa un valor en 1
        value++; // incrementa 1, value = 6
        System.out.println("El valor de 'value' luego de 'value++' es: " + value);

        ++value; // incrementa 1, value = 7
        System.out.println("El valor de 'value' luego de '++value' es: " + value);

        // Operador de decremento (--); decrementa un valor en 1
        value--; // decrementa 1, value = 6
        System.out.println("El valor de 'value' luego de 'value--' es: " + value);

        --value; // decrementa 1, value = 5
        System.out.println("El valor de 'value' luego de '--value' es: " + value);

        // Operador menos unario (- ); Representa un valor
        int negative = -value;
        System.out.println("El valor de  'value' es: " + negative);

        // Operador de complemento lógico (!). Invierte el valor de un booleano
        boolean isJava = true;
        System.out.println("valor inicial: " + isJava + " valor invertido: " + !isJava);

    }

    /*
     * OPERADORES RELACIONALES Y IGUALDAD
     */

    public static void equalityRelationalOperators() {
        System.out.println("OPERADORES RELACIONALES Y IGUALDAD");
        System.out.println("--------------------------");

        int value1 = 1;
        int value2 = 2;

        if (value1 == value2) // igual a : compara si son iguales
            System.out.println("value1 == value2");
        if (value1 != value2) // diferente a : compara si son diferentes
            System.out.println("value1 != value2");
        if (value1 > value2) // mayor que : compara si value1 es mayor que value2
            System.out.println("value1 > value2");
        if (value1 >= value2) // mayor o igual que : compara si value1 es mayor o igual que value2
            System.out.println("value1 >= value2");
        if (value1 < value2) // menor que : compara si value1 es menor que value2
            System.out.println("value1 < value2");
        if (value1 <= value2) // menor o igual que : compara si value1 es menor o igual que value2
            System.out.println("value1 <= value2");
    }
    /*
     * OPERADORES CONDICIONALES U OPERADORES LÓGICOS
     */

    public static void conditionalOperators() {
        System.out.println("OPERADORES CONDICIONALES");
        System.out.println("--------------------------");

        int value1 = 1;
        int value2 = 2;
        System.out.println("int value1 = " + value1);
        System.out.println("int value2 = " + value2);

        if (value1 > 0 && value2 > 0)// condicional AND: es 'true' si ambos operandos son 'true'
            System.out.println("value1 > 0 && value2 > 0");
        if (value1 > 0 || value2 == 0)// condicional OR: es 'true' si al menos un operandos es 'true'
            System.out.println("value1 > 0 || value2 == 0");
        // TERNARIO
        // Si el resultado de evaluar la expresión lógica es verdadero, devuelve el
        // valor de la primera expresión,
        // y en caso contrario, devuelve el valor de la segunda expresión
        String result = value1 < value2 ? "value1 si es menor a value2" : "value1 no es menor a value2";
        System.out.println("value1 < value2? :" + result);
    }

    /*
     * OPERADORES BIT A BIT
     */
    public static void bitwiseOperators() {
        System.out.println("OPERADORES BIT A BIT");
        System.out.println("--------------------------");
        int x = 5;
        int y = 3;
        // Operador & (AND bit-a-bit)
        int resultAND = x & y;
        System.out.println(resultAND); // imprimirá 1
        // Operador | (OR bit-a-bit)
        int resultOR = x | y;
        System.out.println(resultOR); // imprimirá 7
        // Operador ^ (XOR bit-a-bit)
        int resultXOR = x ^ y;
        System.out.println(resultXOR); // imprimirá 6
        // Operador ~ (complemento a uno)
        int resultCOM = ~x;
        System.out.println(resultCOM); // imprimirá -6
        // Operador << (desplazamiento a la izquierda)
        int desplazamiento = 2;
        int resultIzq = x << desplazamiento;
        System.out.println(resultIzq);
        // Operador >> (desplazamiento a la derecha)
        int resultDer = x >> desplazamiento;
        System.out.println(resultDer);
        // Operador >>> (desplazamiento a la derecha sin signo)
        int resultD = x >>> desplazamiento;
        System.out.println(resultD);
    }

}
