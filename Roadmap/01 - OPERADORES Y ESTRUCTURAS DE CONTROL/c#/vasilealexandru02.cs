public class vasilealexandru02
{
    public vasilealexandru02()
    {

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

        /*
            Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
             Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
            (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
         */

        // Operadores aritmeticos
        int suma = 1 + 2;
        int resta = 1 - 2;
        int multiplicacion = 1 * 2;
        double division = 1 / 2;
        double modulo = 10 % 2;

        int operadorIncremento = 0;
        int operadorDecremento = 1;

        ++operadorIncremento;
        operadorIncremento++;
        --operadorDecremento;
        operadorDecremento--;

        // Operadores lógicos booleanos
        bool operadorAnd = true && false;

        bool operadorOr = true || false;

        bool operadorNegacion = !true;

        bool operadorIR = false ^ true;

        bool operadorComparacion = true == true;
        bool operadorComparacionDistinto = true != false;

        bool test = true;

        test &= true; // Output: True

        test |= false; // Output: True

        test ^= true; // Output: False


        // Operadores de desplazamiento y bit a bit

        uint valor = 0b_1100_1001_0000_0000_0000_0000_0001_0001;
        uint desplazamientoIzquierda = valor << 4;
        uint desplazamientoDerecha = valor >> 4;


        /*
         *  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
            que representen todos los tipos de estructuras de control que existan
            en tu lenguaje:
            Condicionales, iterativas, excepciones...
         */

        // Condicionales
        if (true)
        {
            Console.WriteLine("Verdadero!");

        }
        else if (false && false)
        {
            Console.WriteLine("Verdadero también!");
        }
        else
        {
            Console.WriteLine("No me queda más que entrar aquí...");
        }

        string diaSemana = "Lunes";
        switch (diaSemana)
        {

            case "Lunes":
                Console.WriteLine("Primer dia de la semana!");
                break;
            case "Martes":
                Console.WriteLine("Seguimos fuertes con este martes lluvioso!");
                break;
            case "Miércoles":
                Console.WriteLine("Miércoles de ser productivo!");
                break;
            case "Jueves":
                Console.WriteLine("Ya casi estamos... último empujón!");
                break;
            case "Viernes":
                Console.WriteLine("Día de positividad y comienzo del weekend");
                break;
            case "Sabado":
            case "Domingo":
                Console.WriteLine("No me molestes estoy de weekend total!");
                break;

            default:
                Console.WriteLine("No sé que dia es este :/");
                break;

        }


        List<int> numeros = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        // Iterativas
        int numeroTotal = 0;
        for (int i = 0; i < 10; i++)
        {
            numeroTotal += i;
        }

        foreach (int numero in numeros)
        {
            Console.WriteLine("Numero: " + numero);
        }

        int numeroDoWhile = 10;
        do
        {
            Console.WriteLine("Dentro del bucle do while!", numeroDoWhile);
            numeroDoWhile--;

        } while (numeroDoWhile > 0);


        int numeroWhile = 0;
        while (numeroWhile < 10)
        {
            Console.WriteLine("Esto es un bucle while normal");
            numeroWhile++;
        }

        // Try catch finally 
        try
        {
            Console.WriteLine("Este es el codigo que se va a intentar ejecutar");

        }
        catch (Exception e)
        {
            Console.WriteLine("Esta es la excepcion a controlar", e);

        }

        finally
        {
            Console.WriteLine("Código que se ejecuta al final de nuestro bloque try catch");
        }

        /* DIFICULTAD EXTRA (opcional):
        * Crea un programa que imprima por consola todos los números comprendidos
        * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/
        int numeroEjercicio = 10;

        while (numeroEjercicio <= 55)
        {
            if (numeroEjercicio % 2 == 0 && !(numeroEjercicio == 16 || numeroEjercicio % 3 == 0))
            {
                Console.WriteLine(numeroEjercicio);
            }

            numeroEjercicio++;
        }

    }
}
