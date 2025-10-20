using System;
using System.Collections.Generic;
using System.Linq;

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

namespace FuncionesYAlcance
{
    class Program
    {
        // --- Variable "Global" (campo estático en la clase) ---
        private static string globalVar = "Soy una variable global";

        static void Main(string[] args)
        {
            Console.WriteLine("===> Funciones básicas <===");

            // Sin parámetros ni retorno
            Greet();

            // Con un parámetro
            GreetPerson("Wilmer");

            // Con varios parámetros
            Add(5, 3);

            // Con retorno
            int result = Multiply(5, 3);
            Console.WriteLine($"El resultado de la multiplicación es {result}");

            // Con parámetros por defecto
            GreetDefault("MoureDev");
            GreetDefault("Wilmer", "Hello");

            // Con parámetros de longitud variable (params)
            PrintArgs(1, "texto", true, 12.34);


            Console.WriteLine("\n===> Funciones dentro de funciones (Local Functions) <===");
            void OuterFunction()
            {
                Console.WriteLine("Esta es la función externa.");
                void InnerFunction()
                {
                    Console.WriteLine("Esta es la función interna.");
                }
                InnerFunction();
            }
            OuterFunction();


            Console.WriteLine("\n===> Funciones del Framework .NET <===");
            var myList = new List<int> { 1, 2, 3, 4, 5 };
            Console.WriteLine($"Usando la propiedad 'Count' de una Lista: La lista tiene {myList.Count} elementos.");
            
            // Se necesita using System.Linq
            Console.WriteLine($"Usando el método de extensión Max() de LINQ: El valor máximo es {myList.Max()}");


            Console.WriteLine("\n===> Variable LOCAL y GLOBAL <===");
            MyFunctionScope();

            // Modificar una variable global (campo estático)
            Console.WriteLine($"Antes de modificar: {globalVar}");
            ModifyGlobal();
            Console.WriteLine($"Después de modificar: {globalVar}");


            /*
             * DIFICULTAD EXTRA (opcional):
             */
            Console.WriteLine("\n====> DIFICULTAD EXTRA <====");
            int timesPrintedNumber = FizzBuzzExtra("Fizz", "Buzz");
            Console.WriteLine($"\nEl número se imprimió un total de {timesPrintedNumber} veces.");
        }

        // --- Definiciones de las funciones (métodos estáticos) ---

        static void Greet()
        {
            Console.WriteLine("Hola, C#! ");
        }

        static void GreetPerson(string name)
        {
            Console.WriteLine($"Hola, {name}!");
        }

        static void Add(int a, int b)
        {
            Console.WriteLine($"La suma de {a} y {b} es {a + b}");
        }

        static int Multiply(int a, int b)
        {
            return a * b;
        }

        static void GreetDefault(string name, string greeting = "Hola")
        {
            Console.WriteLine($"{greeting}, {name}!");
        }

        static void PrintArgs(params object[] args)
        {
            Console.WriteLine("Argumentos variables (params):");
            foreach (var arg in args)
            {
                Console.WriteLine($"- {arg}");
            }
        }

        static void MyFunctionScope()
        {
            string localVar = "Soy una variable local";
            Console.WriteLine(globalVar); // Acceso a la variable "global" (campo estático)
            Console.WriteLine(localVar);
        }

        static void ModifyGlobal()
        {
            globalVar = "He modificado la variable global";
        }

        static int FizzBuzzExtra(string text1, string text2)
        {
            int count = 0;
            for (int i = 1; i <= 100; i++)
            {
                bool isMultipleOf3 = (i % 3 == 0);
                bool isMultipleOf5 = (i % 5 == 0);

                if (isMultipleOf3 && isMultipleOf5)
                {
                    Console.WriteLine($"{text1}{text2}");
                } else if (isMultipleOf3)
                {
                    Console.WriteLine(text1);
                } else if (isMultipleOf5)
                {
                    Console.WriteLine(text2);
                } else
                {
                    Console.WriteLine(i);
                    count++;
                }
            }
            return count;
        }
    }
}
