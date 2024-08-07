import java.util.Scanner;

public class KingSaul22 {

    public static void main(String[] args) {

        //OPERADORES de ASIGNACIÓN
        operadoresAsignacion();

        //OPERADORES de INCREMENTO y DECREMETO
        operadoresIncreDecremento();

        //OPERADORES ARITMETICOS
        operadoresAritmeticos();

        //OPERADOR TERNARIO
        operadorTernario();

        //OPERADORES de COMPARACIÓN
        operadoresComparacion();

        //OPERADORES LÓGICOS
        operadoresLogicos();

        //OPERADORES de BITs
        operadoresBits();

        //CONTROL con CONDICIONALES
        controlCondicionales();

        //CONTROL con BUCLES
        controlIterativas();

        //CONTROL con EXCEPCIONES
        controlExcepciones();

        //DIFICULTAD EXTRA
        dificultadExtra();
    }

    private static void operadoresAsignacion() {
        int numeroA;
        int numeroB = 2;

        //Asignación basica:
        numeroA = 4;
        System.out.println("\nLa variable numeroA tendrá el valor:\nnumeroA = " + numeroA);
        /*
        Operadores de asiganción compuesto, realiza una operacion
        entre el valor de la variable previa al signo
        y guarda el resultado en la misma variable.
        */
        //Suma entre si mismo y otro valor:
        numeroB += numeroA;
        System.out.printf("""

                Al valor que tenia numeroB, '2', le hemos sumado numeroA:
                2 + %d = %d
                """, numeroA, numeroB
        );
        //Resta entre si mismo y otro valor:
        numeroA -= numeroB;
        System.out.printf("""
                                
                Al valor de numeroA, '4', le restamos NumeroB:
                4 - %d = %d
                """, numeroB, numeroA
        );
        //Multiplicación entre si mismo y otro valor:
        numeroB *= numeroB;
        System.out.printf("""
                                
                Al valor de numeroB, '6', le multiplicamos NumeroB:
                4 * 4 = %d
                """, numeroB
        );
        //División entre si mismo y otro valor:
        numeroB /= numeroA;
        System.out.printf("""
                                
                Al valor de numeroB, '36', le dividimos NumeroA:
                36 / %d = %d
                """, numeroA, numeroB
        );
    }

    private static void operadoresIncreDecremento() {
        /*
        Estos operadores nos permiten aumentar o disminuir en uno
        la variable en cuestión. Usando dos signos de más o menos.
         */
        int numeroA = 2;
        int numeroB = 2;

        //Incremento:
        numeroA++;
        System.out.println("\nEl valor previo al incremento era de '2', después su valor es: " + numeroA);
        //Decremento:
        numeroB--;
        System.out.println("\nEl valor previo al decremento era de '2', después su valor es: " + numeroB);

        /*
        Un uso interesante que podemos darles consiste en usarlos en operaciones
        en las que la variable empleada vaya a cambiar en una unidad.

        Siendo posible que en la operación se utilice el valor sin variar y tras realizarse, se cambie
        o variar el valor y usarlo en la misma operación.
         */
        numeroA = 2;
        numeroB = 2;

        //Se cambia el valor antes de la operación:
        //Preincremento
        numeroA = numeroA + ++numeroB;
        System.out.println("\nSiendo que numeroA y numeroB valen '2', 2 + (2+1) = " + numeroA);
        //Predecremento
        numeroA = numeroA + --numeroB;
        System.out.println("\nnumeroA + --numeroB, 5 + (3-1) = " + numeroA);
        //Se cambia el valor después de la operación:
        //Postincremento
        numeroA = numeroA - numeroB++;
        System.out.println("\nnumeroA - numeroB++, 7 - 2 = " + numeroA);
        //Postdecremento
        numeroA = numeroA + numeroB--;
        System.out.println("\nnumeroA - numeroB--, 5 - 1 = " + numeroA);
        System.out.println("Tras la operación numeroB valdrá: " + numeroB);

    }

    private static void operadoresAritmeticos() {
        int numeroA = 5;
        int numeroB = 7;
        //Suma de dos números:
        int suma = numeroA + numeroB;
        System.out.printf("\n%d + %d = %d\n", numeroA, numeroB, suma);
        //Resta de dos numeros:
        int resta = suma - numeroA;
        System.out.printf("\n%d - %d = %d\n", suma, numeroA, resta);
        //Multiplicación de dos números:
        int producto = resta * numeroB;
        System.out.printf("\n%d * %d = %d\n", resta, numeroB, producto);
        //División de dos números:
        int division = producto / numeroA;
        System.out.printf("\n%d / %d = %d\n", producto, numeroA, division);
        //Recoger el resto de una división usando el módulo:
        int resto = producto % numeroA;
        System.out.printf("\n%d %s %d = %d\n", producto, "%", numeroA, resto);
    }

    private static void operadorTernario() {
        //Los operadores ternarios son una manera de asignar un valor u otro teniendo en cuenta una condición
        //Esto es, en caso de que la condición sea TRUE se devuelve un valor A, en caso de que sea FALSE se devuelve B
        //La estructura que usa es la siguiente: condicion ? valorA : valorB
        boolean condicion = false;
        int numero = condicion ? 2 : 4;
        System.out.println("En este caso la condición es 'False', por ello se usará el segundo valor que está ubicado a la derecha\n" + numero);
    }

    private static void operadoresComparacion() {
        /*
        Estos operadores compararán los valores indicados y
        devolverán un booleano en funición del resultado.
         */

        int numeroA = -1;
        int numeroB = 4;
        boolean cumpleCondicion;

        //Igual que:
        cumpleCondicion = numeroA == numeroB;
        System.out.println("\nnumeroA es igual a numeroB: " + cumpleCondicion);
        //Distinto que:
        cumpleCondicion = numeroA != numeroB;
        System.out.println("\nnumeroA es distinto a numeroB: " + cumpleCondicion);
        //Mayor que:
        cumpleCondicion = numeroA > numeroA;
        System.out.println("\nnumeroA es mayor a numeroA: " + cumpleCondicion);
        //Menor que:
        cumpleCondicion = numeroA < numeroB;
        System.out.println("\nnumeroA es menor a numeroB: " + cumpleCondicion);
        //Mayor o igual que:
        cumpleCondicion = numeroA >= numeroB;
        System.out.println("\nnumeroA es igual o mayor a numeroB: " + cumpleCondicion);
        //Menor o igual que:
        cumpleCondicion = numeroA <= numeroA;
        System.out.println("\nnumeroA es menor o igual a numeroA: " + cumpleCondicion);

    }

    private static void operadoresLogicos() {
        boolean cumpleCondicion;

        //Operador &
        cumpleCondicion = (2 == 2) && (3 == 1);
        System.out.println("""
                                
                Pese a que '2' es igual a '2' (true),
                '3' es distinto de '1' (false),
                por lo que globalmente se devuelve false:
                """ + cumpleCondicion
        );
        //Operador |
        cumpleCondicion = (2 == 2) || (3 == 1);
        System.out.println("""
                                
                Pese a que '3' es distinto de '1' (false),
                '2' es igual a '2' (true),
                por lo que globalmente se devuelve true:
                """ + cumpleCondicion
        );
        //Operador !
        cumpleCondicion = (2 == 2) != (3 == 1);
        System.out.println("""
                                
                '2' es igual a '2' (true),
                '3' es distinto de '1' (false),
                por lo que, al ser distintos, globalmente se devuelve true:
                """ + cumpleCondicion
        );
    }

    private static void operadoresBits() {
        int numA = 11, numB = 9;
        System.out.println(numA + " a binario: " + Integer.toBinaryString(numA));
        System.out.println(numB + " a binario: " + Integer.toBinaryString(numB));

        //Operador ~ (NOT)
        //Este operador cambiara los 1 por 0 y los 0 por 1
        System.out.println("NOT " + numA + ": " + Integer.toBinaryString(~numA));

        //Operador & (AND)
        //Este operador comparará los bits individuales de ambos numeros y devolverá 1 en la posición cuando ambos sean 1
        System.out.println(numA + " AND " + numB + ": " + Integer.toBinaryString(numA & numB));

        //Operador | (OR)
        //Este operador hace lo mismo que el anterior pero con que uno de los dos valores sea 1 colocará 1
        System.out.println(numA + " OR " + numB + ": " + Integer.toBinaryString(numA | numB));

        //Operador ^ (XOR)
        //Este operador comparará los bits de dos números y devolverá 1 en la posición donde no coincidan entre los dos números
        System.out.println(numA + " XOR " + numB + ": " + Integer.toBinaryString(numA ^ numB));

        //También podemos desplazar bitsa un lado u otro(teniendo en cuenta de que se pueden perder si los desplazamos demasiado)
        //Usamos el operador << para desplazarlos a la izquierda y >> para la derecha.
        //En este caso usaremos 2 como el número de posiciones desplazadas
        System.out.println(numA + " << 2: " + Integer.toBinaryString(numA << 2));
        System.out.println(numB + " >> 2: " + Integer.toBinaryString(numA >> 2));
    }

    private static void controlCondicionales() {
        //Se usa una condición (true o false) para determinar si se hace una cosa u otra
        int numA = 2, numB = 5;
        if (numA < numB) {
            System.out.println(numA + " es menor que " + numB);
        } else {
            System.out.println(numA + " no es menor que " + numB);
        }

        //También puedes usar 'if' anidados con distintas condiciones
        if (numA > numB) {
            System.out.println(numA + " es mayor que " + numB);
        } else if (numA == numB) {
            System.out.println(numA + " es igual que " + numB);
        } else {
            System.out.println(numA + " es menor que " + numB);
        }
    }

    private static void controlIterativas() {
        //Bucles for
        //Se repetirá un código un determinado número de veces
        //Imprimimos los números desde el 0 al 9
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }

        //Bucles while
        //Se repetirá un código hasta que la condición se cumpla
        int numA = 0, numB = 2;
        boolean condicion = true;
        while (condicion) {
            System.out.println("Condición es " + condicion + ". Se continua la ejecución del while");
            if (numA == numB){
                condicion = false;
            }else if (numA > numB) {
                numB += 2;
            } else {
                numA += 3;
            }

            if (condicion) {
                System.out.println("Condición es " + condicion + ". Se continuará la ejecución del while");
            } else {
                System.out.println("Condición es " + condicion + ". Se terminará la ejecución del while");
            }
        }
    }

    private static void controlExcepciones() {
        //Hay acciones que pueden provocar fallos en un proceso
        //para solucionar esto se usa un controlador que captura ese fallo y continua con la ejecución del programa
        Scanner sc = new Scanner(System.in);
        //Si se conoce que una parte puede dar un error, lo incluimos en un try
        try {
            int numA = sc.nextInt();
            System.out.println("No ha surgido un error");
            //En caso de que surja el error, se captura
        } catch (Exception e) {
            System.out.println("Ha surgido un error");
            //finally es algo que siempre se ejecutará
        } finally {
            System.out.println("Este código se ejecutará siempre");
            sc.close();
        }
    }

    private static void dificultadExtra() {
        //Empezando por 10 y hasta llegar a 55
        for (int i = 10; i <= 55; i += 2) {
            //Se imprimirá los números pares siempre que no sea 16 o multiplo de 3
            if (i % 2 == 0 && i != 16 && i % 3 != 0) System.out.println(i);
        }
    }
}
