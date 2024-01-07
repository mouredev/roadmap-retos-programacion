import javax.xml.validation.Validator;

/**
 *  * EJERCICIO #01 - OPERADORES Y ESTRUCTURAS DE CONTROL
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
 * @version v1
 * 
 * @since 07/01/2024
 * 
 * @author Blas Barragán
 * 
 */
public class BlasBarragan {
    public static void main(String[] args) {
        
        // OPERADORES ARITMETICOS
        int valorA = 10;
        int valorB = 5;
        
        int suma = valorA + valorB;
        int resta = valorA - valorB;
        int multiplicacion = valorA * valorB;
        int division = valorA / valorB;
        int restoDeLaDivision = valorA % valorB;

        System.out.println("<=Operadores Aritmeticos=>\n");
        System.out.println("Suma: " + suma);
        System.out.println("Resta: " + resta);
        System.out.println("Multiplicación: " + multiplicacion);
        System.out.println("División: " + division);
        System.out.println("Resto de la división: " + restoDeLaDivision);

        // OPERADORES DE ASIGNACIÓN
        System.out.println("\n<=Operadores de Asignación=>\n"); // Realizan la operación antes de la asignación.
        System.out.println("ValorA = " + valorA + " Asignación = 5");
        valorA += 5;
        System.out.println("Suma: valorA = " + valorA);   
        System.out.println("ValorA = " + valorA + " Asignación = 5");
        valorA -= 5;
        System.out.println("Resta: valorA = " + valorA);  
        System.out.println("ValorA = " + valorA + " Asignación = 5");
        valorA *= 5;
        System.out.println("Multiplicación: valorA = " + valorA);
        System.out.println("ValorA = " + valorA + " Asignación = 5");
        valorA /= 5;
        System.out.println("División: valorA = " + valorA);
        System.out.println("ValorA = " + valorA + " Asignación = 5");
        valorA %= 5;
        System.out.println("Resto de la división: " + valorA);

        // OPERADORES RELACIONALES
        System.out.println("\n<=Operadores de Asignación=>\n"); // Responden true o false.
        System.out.println("Es " + valorA + " Mayor que (>) " + valorB + " ? : " + (valorA>valorB));
        System.out.println("Es " + valorA + " Menor que (<) " + valorB + " ? : " + (valorA<valorB));
        System.out.println("Es " + valorA + " Igual a (==) " + valorB + " ? : " + (valorA==valorB));
        System.out.println("Es " + valorA + " Distinto de (!=) " + valorB + " ? : " + (valorA!=valorB));
        System.out.println("Es " + valorA + " Mayor o Igual que (>) " + valorB + " ? : " + (valorA>=valorB));
        System.out.println("Es " + valorA + " Menor o Igual que (>) " + valorB + " ? : " + (valorA<=valorB));

        // OPERADORES LÓGICOS
    
        System.out.println("\n<=Operadores Lógicos=>\n"); // Responden true o false.
        boolean and = (valorA>valorB)&&(valorA<valorB);
        boolean or = (valorA==valorB)||(valorA!=valorB);
        boolean not = (!and);
        System.out.println( valorA + " es mayor que (>) " + valorB + " y (&&) " + valorA + " menor que (<) " + valorB + " ? : " + and);
        System.out.println( valorA + " es igual a (==) " + valorB + " o (||) "  + valorA + " es distinto de (!=) " + valorB + " ? : " + or);
        System.out.println("Si negamos la operacion and (&&), el resultado es: " + not);
        
         // OPERADORES DE CONCATENACIÓN
         System.out.println("\n<=Operadores Lógicos=>\n");
         System.out.println("Para concatenar valores, siempre usamos el caracter '+' como hemos hecho en las sentencias anteriores.");
                
         // OPERADORES INCREMENTALES
         System.out.println("\n<=Operadores Lógicos=>\n");

    }
}