internal class Program
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
    private static void Main(string[] args)
    {
        int a = 10;
        int b = 5;
        int suma = a + b; // adición
        int diferencia = a - b; // substracción
        int producto = a * b; // multiplicación
        int cociente = a / b; // división
        int remanente = a % b; // modulo

        bool esMayor = a > b; // mayor que
        bool esMenor = a < b; // menor que
        bool esIgual = a == b; // igual a
        bool noEsIgual = a != b; // no es igual a
        bool esMayorOIgual = a >= b; // mayor o igual a
        bool esMenorOIgual = a <= b; // menor o igual a
        bool yLogico = esMayor && esMenor; // y logico
        bool oLogico = esMayor || esMenor; // o logico
        bool noLogico = !esMayor; // no logico

        int x = 10;
        int y = 10;

     
        bool mismoValorOperador = x == y; // revisa si x e y tienen el mismo valor usando el operador de igualdad
        bool diferenteValorOperador = x != y; // revisa so x e y tienen diferente valor usando el operador de desigualdad

        // condicional
        if (a > b)
        {
            Console.WriteLine("a es mayor que b");
        }
        else if (a < b)
        {
            Console.WriteLine("a es menor que b");
        }
        else
        {
            Console.WriteLine("a es igual que b");
        }

        // iterativo
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"iteracion {i}");
        }

        // exepcion
        try
        {
            int result = a / 0;
            Console.WriteLine($"resultado: {result}");
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine("no se permite la division por cero");
        }

        for (int i = 10; i <= 55; i++)
        {
            if (i % 2 == 0 && i != 16 && i % 3 != 0)
            {
                Console.WriteLine(i);
            }
        }
    }
}