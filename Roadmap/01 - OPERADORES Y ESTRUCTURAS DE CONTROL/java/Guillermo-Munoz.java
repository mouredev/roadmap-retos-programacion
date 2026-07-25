public class GuillermoMunoz {
    
//Usuario GitHub: Guillermo-Muñoz

public static void main(String[] args) {

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

int a = 10;
int b = 5;
// Operadores Aritméticos
System.out.println("Operadores Aritméticos:");
System.out.println("Suma: " + (a + b)); 
System.out.println("Resta: " + (a - b));
System.out.println("Multiplicación: " + (a * b ));
System.out.println("Division: " + (a / b));
System.out.println("Modulo: " + (a % b ));;

// Operadores de asignación
System.out.println("\nOperadores de Asignación:");
System.out.println("Asignación: " + (a = b));
System.out.println("Suma y asignación: " + (a += b));
System.out.println("Resta y asignación: " + (a -= b));
System.out.println("Multiplicación y asignación: " + (a *= b));     
System.out.println("División y asignación: " + (a /= b));
System.out.println("Módulo y asignación: " + (a %= b));

// Operadores de comparación
System.out.println("\nOperadores de Comparación:");
System.out.println("Igual a: " + (a == b));
System.out.println("Distinto de: " + (a != b));
System.out.println("Mayor que: " + (a > b));
System.out.println("Menor que: " + (a < b));
System.out.println("Mayor o igual que: " + (a >= b));
System.out.println("Menor o igual que: " + (a <= b));

// Operadores lógicos
System.out.println("\nOperadores Lógicos:");
System.out.println("AND lógico: " + ((a > b) && (a != b)));
System.out.println("OR lógico: " + ((a > b) || (a == b)));
System.out.println("NOT lógico: " + !(a == b));

// Estructuras de control
System.out.println("\nEstructuras de Control:");

// Condicionales
 
   // Estructura if-else
    if (a > b) {
        System.out.println("a es mayor que b");
    }else if(a == b){
        System.out.println("a es igual a b");
    } 
    else {
        System.out.println("a no es mayor que b" );
    }

    // Estructura switch-case
    int c = 10;
    switch (c) {
        case 5:
            System.out.println("c es 5");
            break;
        case 10:
            System.out.println("c es 10");
            break;
        default:
            System.out.println("c no es ni 5 ni 10");
    }

    // Estructuras while, do-while y for
    int d = 0;
    while (d < 5) {
        System.out.println("While: " + d);
        d++;
    }

    int e = 0;
    do {
        System.out.println("Do-While: " + e);
        e++;
    } while (e < 5);

    for (int i = 0; i < 5; i++) {
        System.out.println("For: " + i);

    }
    // Ejercicio extra

    System.out.println("Ejercicio extra: Crea un programa que imprima por consola todos los números comprendidos\r\n" + //
                " entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.");
    for( int f = 10 ; f <=55; f++){
        if (f % 2 == 0 && 
            f % 3 != 0 && 
            f != 16){
            System.out.println("Numero: " + f);
        }
    }



}



}
