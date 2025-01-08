public class DanielBelenguer {
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
public static void main(String[] args) {
    int num1 = 10;
    int num2 = 5;
    
    // Operadores

    // Aritméticos:

    int resultado = num1 + num2;
    System.out.println("Suma: " + resultado);
    resultado = num1 - num2;
    System.out.println("Resta: " + resultado);
    resultado = num1 * num2;
    System.out.println("Multiplicación: " + resultado);
    resultado = num1 / num2;
    System.out.println("División: " + resultado);
    resultado = num1 % num2;
    System.out.println("Potencia: ");
    System.out.println("Módulo: " + resultado);
    resultado = num1++;
    System.out.println("Incremento: " + resultado);
    resultado = num1--;
    System.out.println("Decremento: " + resultado);
    
    // Lógicos:

    System.out.println("AND && 5==5 && 6<10: " + (5 == 5 && 6 < 10));
    System.out.println("OR || 5==1 && 6<10: " + (5 == 1 || 6 < 10));
    System.out.println("NOT ! !false" + (!false));

    // Asignación:

    num1 = 15;
    System.out.println(num1);
    num1 += 5;
    System.out.println(num1);
    num1 -= 3;
    System.out.println(num1);
    num1 *= 2;
    System.out.println(num1);
    num1 /= 2;
    System.out.println(num1);
    num1 %= 3;
    System.out.println(num1);
    num1 ^= 2;
    System.out.println(num1);

    // Comparación:

    System.out.println("Es igual 15 = 5: " + (15 == 5));
    System.out.println("Es diferente 15 != 5: " + (15 != 5));
    System.out.println("Es mayor 15 > 5: " + (15 > 5));
    System.out.println("Es menor 15 < 5: " + (15 < 5));
    System.out.println("Es mayor o igual 15 >= 5: " + (15 >= 5));
    System.out.println("Es menor o igual 15 <= 5: " + (15 <= 5));

    // Bits:
    num1 = 10;
    num2 = 5;
    System.out.println("Operador AND &: " + (num1 & num2));
    System.out.println("Operador OR |: " + (num1 | num2));
    System.out.println("Operador XOR ^: " + (num1 ^ num2));
    System.out.println("Desplazamiento a la izquierda <<: " + (num1 << num2));
    System.out.println("Desplazamiento a la derecha >>: " + (num1 >> num2));

    // Estructuras de control

    // Condicionales:

    int numeroif = 50;

    if (numeroif == 50) {
        System.out.println("Entro en el If" + numeroif);
    } else if (numeroif == 60) {
        System.out.println("Entro en el Else If" + numeroif);
    } else {
        System.out.println("Entro en el Else" + numeroif);        
    }

    // Switch:
    int numerocase = 10;
    switch (numerocase) {
        case 10:
            System.out.println("Entro en el case 10" + numerocase);
            break;
        case 20:
            System.out.println("Entro en el case 20" + numerocase);
            break;
        default:
            System.out.println("Entro en el default" + numerocase);
            break;
    }

    // Case que se almacena en una variable
    String resultadoSwitch = switch (numerocase) {
        case 10 -> "Entro en el case 10" + numerocase;
        case 20 -> "Entro en el case 20" + numerocase;
        default -> "Entro en el default" + numerocase;
    };
    System.out.println("El resultado del switch es: " + resultadoSwitch);

    // Iterativas:

    // Bucle for:
    for (int i = 0; i < 10; i++) {
        System.out.println("Iteración: " + i);
    }

    // Bucle for each:
    int[] array = {1, 2, 3, 4, 5};
    for (int i : array) {
        System.out.println("Iteración: " + i);
    }

    // Bucle while:
    int i = 0;
    while (i < 10) {
        System.out.println("Iteración: " + i);
        i++;
    }

    // Bucle do while:
    // Este bucle se ejecuta primero el bloque do y luego ejecuta la condición
    i = 0;
    do {
        System.out.println("Iteración: " + i);
        i++;
    } while (i < 10);

    // Excepciones:

    // Esta estructura de control se utiliza para capturar errores en tiempo de ejecución
    // Lo que esta comprobando que el indice que estas intentando mostrar esta fuera del rango del array
    try {
        int[] arrayExcepcion = {1, 2, 3, 4, 5};
        System.out.println(arrayExcepcion[10]);
    } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Error: " + e);
    }

    // Ejercicio extra:
    /*Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

    for (int j = 10; j <= 55; j++) {
        if (j % 2 == 0 && j != 16 && j % 3 != 0) {
            System.out.println("Número: " + j);
        }
    }
    }
}