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
    // ### OPERADORES ###

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
        System.out.println("\n<=Operadores Incrementales=>\n");
        System.out.println("ValorA = " + (valorA = 2));
        valorA ++;
        System.out.println("ValorA incrementado en 1 usando ++: " + valorA);
        valorA --;
        System.out.println("ValorA decrementado en 1 usando --: " + valorA);         

        // OPERADOR CONDICIONAL
        System.out.println("Este condicional, es la forma abreviada de la estructura \"if-else\"");
        valorA = 5;
        String resultado = (valorA > 0) ? "Positivo" : "Negativo";
        System.out.println(resultado); // Si la condicion (valorA>0) es cierta, se asigna el valor "Positivo" a la variable resultado.

    // ### ESTRUCTURAS DE CONTROL ###
        
        // ESTRUCTURA SECUENCIAL
            // Todas las sentencias de codigo en Java se ejecutan de forma secuencial, una después de otra en el orden en que están escritas.
            valorA = 10;
            System.out.println("valorA = 10");
            valorA = valorA + 3;
            System.out.println("ValorA + 3 = " + valorA);
        
        // ESTRUCTURAS DE SELECCIÓN
            // Selección simple (if...)
            if (valorA == 13){
                System.out.println("valora vale 13 en la selección if simple");
            }
            // Selección doble (if...else...)
            if (valorA == 13){
                System.out.println("Agarramela que me crece");
            }else {
                System.out.println("valorA no es igual a 13");
            }
            // Selección múltiple (if...else if...else...) Anidamos sentencias
            if (valorA == 13){
                System.out.println("valorA es igual a 13 en la selección multiple anidando if...else");
            }else if (valorA == 5){ 
                System.out.println("jejeje");
            }else {
                System.out.println("valorA no es ni 13 ni 5");
            }
            //Selección múltiple (switch) La usamos para seleccionar 1 entre multiples opciones
            switch (valorA) { // Indicamos la variable que nos dará el valor de la opción a tratar
                case 1: // Si valorA vale 1
                    System.out.println("valorA vale 1");
                    break; // Sale del switch
                case 2: // Si valorA vale 2
                    System.out.println("valorA vale 2");
                    break;
                case 3:
                    System.out.println("valorA vale 3"); 
                    break;
                case 13:
                    System.out.println("valorA vale 13 en el switch");
                    break;
                default: // Opción por defecto (si el valor de valorA no coincide con ninguna opción(case))
                    System.out.println("Error, opción no disponible");
                    break;
            }

        // ESTRUCTURAS DE REPETICIÓN
            // Bucle while
            while (valorA <= 13){ // ojo los bucles infinitos
                System.out.println("valorA no vale 13 y lo voy a repetir hasta que lo sea");
                valorA ++;
            }
            // Bucle do-while
            do {
                System.out.println("Le sumo 1 a valorA si es menor que 25");
                valorA ++;
                System.out.println(valorA);
            }while (valorA < 25);
            // Bucle For
            for (int i = 0; i <= valorA; i++){
                System.out.println("i vale " + i + " y se incrementa en 1 hasta igualar a valorA que vale " + valorA);
            }
            // Bucle Foreach
            String [] semana = {"lunes","martes","miercoles","jueves","viernes","sabado","domingo"};
            for (String dia : semana){
                System.out.println(dia);
            }

            //EXTRA

            for (int i = 10; i<55; i++){
                if ((i%2 == 0)&&(i==16)&&(i%3!=0)){
                }
                System.out.println(i);
            }
    }
}