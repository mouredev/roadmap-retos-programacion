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
 
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

class Program
{
    public static void Main(string[] args)
    {
        //Operadores aritmeticos
        int a = 10;
        int b = 20;
        Console.WriteLine("Suma: " + (a + b));
        Console.WriteLine("Resta: " + (a - b));
        Console.WriteLine("Multiplicacion: " + (a * b));
        Console.WriteLine("Division: " + (a / b));
        Console.WriteLine("Modulo: " + (a % b));
        Console.WriteLine("Incremento: " + (++a));
        Console.WriteLine("Decremento: " + (--a));

        //Operadores logicos

        bool c = true;
        bool d = false;
        Console.WriteLine("\nOperadores logicos");
        Console.WriteLine("NOT: " + (!c));
        Console.WriteLine("AND: " + (c && d));
        Console.WriteLine("OR: " + (c || d));

        //Operadores de comparacion
        Console.WriteLine("\nOperadores de comparacion");
        Console.WriteLine("Igual: " + (a == b));
        Console.WriteLine("Distinto: " + (a != b));
        Console.WriteLine("Mayor que: " + (a > b));
        Console.WriteLine("Menor que: " + (a < b));
        Console.WriteLine("Mayor o igual que: " + (a >= b));
        Console.WriteLine("Menor o igual que: " + (a <= b));

        //Operadores de asignacion
        Console.WriteLine("\nOperadores de asignacion");
        Console.WriteLine("Asignacion: " + (a = b));
        Console.WriteLine("Suma y asignacion: " + (a += b));
        Console.WriteLine("Resta y asignacion: " + (a -= b));
        Console.WriteLine("Multiplicacion y asignacion: " + (a *= b));
        Console.WriteLine("Division y asignacion: " + (a /= b));
        Console.WriteLine("Modulo y asignacion: " + (a %= b));

        //Operadores de identidad
        Console.WriteLine("\nOperadores de identidad");
        Console.WriteLine("Igualdad: " + "a es un numero entero? " + (a is int));
        Console.WriteLine("Desigualdad: " + "a no es un numero entero? " + (a is not int));

        object obj1 = new object();
        object obj2 = new object();
        Console.WriteLine(obj1 == obj2); // False, diferentes referencias

        object obj1 = new object();
        object obj2 = obj1;
        Console.WriteLine(Object.ReferenceEquals(obj1, obj2)); // True, misma referencias

        //Opertadores de pertenencia
        Console.WriteLine("\nOperadores de pertenencia no existen de tal manera en C#, hay algunas maneras de lograrlo.");
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
        bool exists = numbers.Contains(3); // true

        string texto = "Hola mundo";
        bool contiene = texto.Contains("Hola"); // True

        //Operadores de bits
        Console.WriteLine("\nOperadores de bits.");
        Console.WriteLine("AND: " + (a & b));
        Console.WriteLine("OR: " + (a | b));
        Console.WriteLine("XOR: " + (a ^ b));
        Console.WriteLine("Desplazamiento a la izquierda: " + (a << 1));
        Console.WriteLine("Desplazamiento a la derecha: " + (a >> 1));

        //Estructuras de control
        Console.WriteLine("\nEstructuras de control");
        // Condicional 
        if(a == b)
        {
            Console.WriteLine("A es igual que B");
        }
        else if(a > b)
        {
            Console.WriteLine("A es mayor que B");
        }
        else
        {
            Console.WriteLine("A es menor que B");
        }

        // Iterativa
        for(int i = 0; i < 8; i++)
        {
            Console.WriteLine("Iteracion: " + i);
        }

        // Excepcion
        try
        {
            int zero = 0;
            int division = 5 / zero;
        }
        catch(DivideByZeroException ex)
        {
            Console.WriteLine("Ocurrio una excepcion: " + ex.Message);
        }

        // Dificultad extra
        Console.WriteLine("\nDificultad extra");
        for(int i = 10; i <= 55; i++)
        {
            if(i % 2 == 0 && i != 16 && i % 3 != 0)
            {
                Console.WriteLine(i);
            }
        }

    }
}