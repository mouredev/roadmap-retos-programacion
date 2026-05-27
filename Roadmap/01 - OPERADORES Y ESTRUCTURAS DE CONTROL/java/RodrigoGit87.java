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

public class RodrigoGit87 {
    public static void main(String[] args){
    //operadores aritmeticos
    int num1 = 2;
    int num2 = 5;

    int suma = num1 + num2;
    int resta = num2 - num1;
    int multiplicacion = num1 * num2;
    double division = num1 / num2;
    double restoDivision = num1 % num2;
    double potencia = Math.pow(num1, num2);

    IO.println (" suma: " + suma + "\n resta:" + resta+ " \n multiplicacion: "+multiplicacion+ "\n division: "
            + division + "\n resto: "+ restoDivision+ "\npotencia: " + potencia);

    //ASignacion
    num1 = num2;
        IO.println( num1); //ahora num1 vale num2 (5)

    num1 = num2 * 2; //num1 sigue valiendo 5
        IO.println( num1 ); //  ahora vale 10 por que num2 + 2 =  '5 x 2' = 10

    //se puede asignar el valor resultante a la variable declarada, simplemente añadiendo el operador aritmetico al signo igual
    num1 += 69;
    num1 -= 69;
    num1 *= num2; // num1= 10 * num2= 5
         IO.println(num1); //ahora num1=50
    num1 /= 2;
         IO.println(num1);//ahjora num1 = 25
    num2 %= 5;
         System.out.println(num2); //num2 ahora valdra el resultado del resto de la division. (num2 = 0)


    //Comparacion
    int a, b;
    a= 33;
    b= 3;

        IO.println("a == b: " + (a == b)); // Es falso por que el  valor que se asigno a 'a' fue 33 y 'b' vale 3
    // lo comprobamos->
        IO.println("a == 33: " + (a == 33));// imprime un true por que comparar 33 con 33, efectivamente es 33

        IO.println(" a != b:" + (a != b)); // a es distinto de b? true

        IO.println("\notros comparadores(faciles de entender a simple vista)");
        IO.println(" a > b:" + (a > b)); // 33 mayor q 3? true
        IO.println(" a >= b:" + (a >= b)); // 33 mayor o igual q 3? true
        IO.println(" a < b:" + (a < b)); //....
        IO.println(" a <= b:" + (a <= b));


    // Lógicos
        IO.println("\nLógicos");
    // Y (AND)
        IO.println("\nTabla de verdad con el operador Y &&");
    // Solo es verdad cuando los dos valores son verdad
        IO.println("true && true: " + (true && true));
        IO.println("true && false: " + (true && false));
        IO.println("false && true: " + (false && true));
        IO.println("false && false: " + (false && false));

        IO.println("Ejemplo, 2 > 0 && 2 == 2: " + (2 > 0 && 2 == 2)); // ambas son ciertas, true

    // O (OR)
        IO.println("\nTabla de verdad con el operador O ||");
    // Solo es falso cuando los dos valores son falsos
        IO.println("true || true: " + (true || true));
        IO.println("true || false: " + (true || false));
        IO.println("false || true: " + (false || true));
        IO.println("false || false: " + (false || false));
        IO.println("Ejemplo, 3 > 1 || 5 == 8: " + (3 > 1 || 5 == 8)); // 3>1? si(true) O 5 es lo mismo que 8? no (false). REsultado final true
    //por que una condicion si es verdadera.

    // NO (NOT)
    // Se usa el signo de admiracion
        IO.println("\nEl operador NOT ! Niega algo q es verdad, por tanto será falso y viceversa");
        IO.println("Ejemplo, (!(3 > 1) || 5 == 8): " + (!(3 > 1) || 5 == 8));

    // Unarios
        IO.println("\nUnarios, valor de b=3");

        IO.println("+b: " + (+b));// lo hace positivo
        IO.println("-b: " + (-b));// lo hace negativo
        IO.println("++b: " + (++b));// PreIncremento; si esta delante va a incrementar el valor antes de imprimirlo
        IO.println("b++: " + (b++));/*
     * Si el incremento va detrás, se imprime el valor actual y el valor final queda
     * guardado hasta la proxima iteracion.
     */
        IO.println("Valor de b despues de la iteracion b++: " + (b));
        IO.println("--b: " + (--b));// Decremento, igual q con el incremento

        //ESTRUCTURAS DE CONTROL
        //condicionales
        int x= 10;
        int y = 13;
        int numMayor, numMenor; //declarar variables fuera del bucle si queremos usarlas fuera de él.
           // IF, ELSE IF
            if ( x > y){ //lo q va dentro de las llaves se conoce como scope o ámbito. variables declaradas aqui dejan de existir fuera de él.
                        //por eso se declaran las variables fuera del scope, para q sigan existiendo uan vez asignados los valores.
                 numMayor = x;
                 IO.println("numero mayor: " + numMayor);
            } else if ( x < y){
                numMayor = y;
                IO.println("numero mayor: " + numMayor);
            } else IO.println(" Son iguales ");

            //BUCLES
            //for
            System.out.println(" -ciclo for-");
            for (int i=0; i <= 10; i+=2){
            IO.println("\n numeros pares: " + i);
            }
            //while
            System.out.println(" -ciclo while-");
               int i = 0;
                while(i <= 10){
                    IO.println("\n numeros pares: " + i);
                    i+=2;
                }
            //do while
            i = 0; // reset de i al valor 0
            System.out.println("\n -ciclo  Do while-");
                do{
                    i += 2;
                    IO.println("numeros pares: " + i);
                }while(i <= 10);

            // EXCEPCIONES - try-catch-finally
        try {
            var resultado = 10 / 0;
        } catch (ArithmeticException e) {
            System.err.println("\nNo se puede dividir por 0 :P");
        } finally {
            System.out.println(" el codigo continua...");
        }
        System.out.println(" ");
            //throw (Crear una clase y su metodo throw fuera del main)
            /*EJemplo:
            *public class ClaseThrow (){
            * public void verificarEdad (int edad) throws IllegalArgumentException {
                if (edad < 18)System.out.println(" Tienes q ser mayor de edad");
                else if (edad >= 65 ) System.out.println(" Demasiado mayor " );
                else System.out.println(" En el prime ");
        *       }
        *     }*/

        //EJERCICIO EXTRA
        System.out.println("\nNumeros pares del 10 al 55");
        for ( i = 10; i <= 55; i+=2){
            if (i % 3 == 0 || i ==16) continue;
            System.out.println(" numero par: " + i);
        }
    }
}

