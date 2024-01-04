public class BertoMP {
    public static void main(String[] args) {
        // OPERADORES ARITMÉTICOS
        System.out.println("OPERADORES ARITMÉTICOS");
        int firstNumber = 7;
        int secondNumber = 2;
        int result;

        // Operador suma (+)
        result = firstNumber + secondNumber;
        System.out.println("El resultado de sumar " + firstNumber + " y " + secondNumber + " es: " + result);

        // Operador resta (-)
        result = firstNumber - secondNumber;
        System.out.println("El resultado de restar " + firstNumber + " y " + secondNumber + " es: " + result);

        // Operador multiplicación (*)
        result = firstNumber * secondNumber;
        System.out.println("El resultado de multiplicar " + firstNumber + " y " + secondNumber + " es: " + result);

        // Operador división (/)
        result = firstNumber / secondNumber;
        System.out.println("El resultado de dividir " + firstNumber + " y " + secondNumber + " es: " + result);

        // Operador módulo (%)
        result = firstNumber % secondNumber;
        System.out.println("El resto de la división entre " + firstNumber + " y " + secondNumber + " es: " + result);

        // OPERADORES LÓGICOS
        System.out.println("\nOPERADORES LÓGICOS");
        boolean firstBool = true;
        boolean secondBool = false;

        // Operador lógico AND (&&)
        boolean logicAnd = firstBool && secondBool;
        System.out.println("AND lógico: " + logicAnd); // Imprime false.

        // Operador lógico OR (||)
        boolean logicOr = firstBool || secondBool;
        System.out.println("OR lógico: " + logicOr); // Imprime true.

        // Operador lógico NOT (!)
        boolean logicNot = !firstBool;
        System.out.println("NOT lógico: " + logicNot); // Imprime false.

        // OPERADORES DE COMPARACIÓN
        System.out.println("\nOPERADORES DE COMPARACIÓN");
        // Operador de igualdad (==)
        boolean equal = (firstNumber == secondNumber);
        System.out.println("¿Es igual el número " + firstNumber + " y el número " + secondNumber + "? -> " + equal);

        // Operador de diferencia (!=)
        boolean diff = (firstNumber != secondNumber);
        System.out.println("¿Es distinto el número " + firstNumber + " del número " + secondNumber + "? ->" + diff);

        // Operador de mayor que (>)
        boolean greaterThan = (firstNumber > secondNumber);
        System.out.println("¿Es " + firstNumber + " mayor que " + secondNumber + "? -> " + greaterThan);

        // Operador de menor que (<)
        boolean lessThan = (firstNumber < secondNumber);
        System.out.println("¿Es " + firstNumber + " menor que " + secondNumber + "? -> " + lessThan);

        // Operador de mayor o igual que (>=)
        boolean greaterOrEqual = (firstNumber >= secondNumber);
        System.out.println("¿Es " + firstNumber + " mayor o igual que " + secondNumber + "? -> " + greaterOrEqual);

        // Operador de menor o igual que (<=)
        boolean lessOrEqual = (firstNumber <= secondNumber);
        System.out.println("¿Es " + firstNumber + " menor o igual que " + secondNumber + "? -> " + lessOrEqual);

        // OPERADORES DE ASIGNACIÓN
        System.out.println("\nOPERADORES DE ASIGNACIÓN");
        int number = 10;

        // Operador de asignación simple (=): Asigna el valor a la variable.
        int assignedValue = number;
        System.out.println("Valor asignado: " + assignedValue);

        // Operador de asignación y suma (+=): Añade un valor a la variable existente.
        number += 5; // Equivalente a: number = number + 5;
        System.out.println("Después de +=: " + number);

        // Operador de asignación y resta (-=): Resta un valor de la variable existente.
        number -= 3; // Equivalente a: number = number - 3;
        System.out.println("Después de -=: " + number);

        // Operador de asignación y multiplicación (*=): Multiplica la variable existente por un valor.
        number *= 2; // Equivalente a: number = number * 2;
        System.out.println("Después de *=: " + number);

        // Operador de asignación y división (/=): Divide la variable existente por un valor.
        number /= 4; // Equivalente a: number = number / 4;
        System.out.println("Después de /=: " + number);

        // Operador de asignación y módulo (%=): Obtiene el resto de la división de la variable existente por un valor.
        number %= 4; // Equivalente a: number = number % 4;
        System.out.println("Después de %=: " + number);

        // OPERADORES DE IDENTIDAD
        System.out.println("\nOPERADORES DE IDENTIDAD");
        String firstString = "Hola"; // Crea una cadena en la memoria de Java
        String secondString = "Hola"; // Utiliza la misma cadena que 'str1' (mismo objeto en la memoria)
        String thirdString = new String("Hola"); // Crea una nueva cadena (objeto distinto en la memoria)

        // Operador de identidad (==): Compara si dos referencias apuntan al mismo objeto en la memoria.
        boolean sameObject = (firstString == secondString);

        // Operador de identidad (!=): Compara si dos referencias no apuntan al mismo objeto en la memoria.
        boolean differentObjects = (firstString != thirdString);
        System.out.println("¿El primero y el tercer strings no apuntan al mismo objeto? -> " + differentObjects);

        // OPERADORES PERTENENCIA
        System.out.println("\nOPERADORES DE PERTENENCIA");
        boolean instanceOfString = firstString instanceof String;
        System.out.println("¿Es la variable firstString una instancia de la clase String? -> " + instanceOfString);

        // OPERADORES BITS
        System.out.println("\nOPERADORES DE BITS");
        int firstBit = 5; // Representación binaria: 0000 0101
        int secondBit = 3; // Representación binaria: 0000 0011

        // Operador AND a nivel de bits (&)
        int resultadoAND = firstBit & secondBit;
        System.out.println("Resultado AND: " + resultadoAND);
        // Imprime: Resultado AND: 1 (representación binaria: 0000 0001)

        // Operador OR a nivel de bits (|)
        int resultadoOR = firstBit | secondBit;
        System.out.println("Resultado OR: " + resultadoOR);
        // Imprime: Resultado OR: 7 (representación binaria: 0000 0111)

        // Operador XOR a nivel de bits (^)
        int resultadoXOR = firstBit ^ secondBit;
        System.out.println("Resultado XOR: " + resultadoXOR);
        // Imprime: Resultado XOR: 6 (representación binaria: 0000 0110)

        // Operador de desplazamiento a la derecha (>>)
        int resultadoDesplazamientoDerecha = firstBit >> 1;
        System.out.println("Resultado desplazamiento a la derecha: " + resultadoDesplazamientoDerecha);
        // Imprime: Resultado desplazamiento a la derecha: 2 (representación binaria: 0000 0010)

        // Operador de desplazamiento a la izquierda (<<)
        int resultadoDesplazamientoIzquierda = firstBit << 1;
        System.out.println("Resultado desplazamiento a la izquierda: " + resultadoDesplazamientoIzquierda);
        // Imprime: Resultado desplazamiento a la izquierda: 10 (representación binaria: 0000 1010)

        // ESTRUCTURAS DE CONTROL CONDICIONAL
        System.out.println("\nESTRUCTURAS DE CONTROL CONDICIONAL");
        // if-else
        System.out.println("if-else");
        int num = 10;

        if (num > 0) {
            System.out.println("El número es positivo.");
        } else {
            System.out.println("El número es cero o negativo.");
        }

        // Operador ternario
        System.out.println("\nOperador ternario");
        System.out.println((num > 0) ? "El número es positivo." : "El número es cero o negativo.");

        // switch-case
        System.out.println("\nSwitch-Case");
        int opcion = 2;
        String resultado;

        switch (opcion) {
            case 1 -> System.out.println("Opción 1");
            case 2 -> System.out.println("Opcion 2");
            default:
                System.out.println("Opcion por defecto");
        }

        // ESTRUCTURAS DE CONTROL ITERATIVAS
        System.out.println("\nESTRUCTURAS DE CONTROL ITERATIVAS");
        // while
        System.out.println("Bucle while");
        int contador = 0;
        while (contador < 5) {
            System.out.println("Iteración: " + contador);
            contador++;
        }

        // do-while
        System.out.println("\nBucle do-while");
        contador = 0;
        do {
            System.out.println("Iteración: " + contador);
            contador++;
        } while (contador < 5);

        // for
        System.out.println("\nBucle for");
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteración: " + i);
        }

        // for-each
        System.out.println("\nBucle for-each");
        int[] arrayInt = {1, 2, 3, 4};
        for (int numberInArray : arrayInt) {
            System.out.println("Número: " + numberInArray);
        }

        // MANEJO DE EXCEPCIONES
        System.out.println("\nMANEJO DE EXCEPCIONES");
        try {
            int valor = arrayInt[10];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("¡Error! Índice fuera del rango del arreglo.");
        } finally {
            System.out.println("Bloque finally siempre se ejecuta.");
        }

        // DIFICULTAD EXTRA
        System.out.println("\nEJERCICIO EXTRA");
        /*  Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y
         *  que no son ni el 16 ni múltiplos de 3.*/
        for (int i = 10; i <= 55; i++) {
            if ((i % 2 == 0) && (i != 16) && (i % 3 != 0)) {
                System.out.println("Iteración: " + i);
            }
        }
    }
}
