using System;

namespace LionnyRdguez
{
    class Program
    {
        static void Main(string[] args)
        {
            
        }
    }

    class Ejercicio_01
    {
        /*Operadores de C#
        Operadores Aritméticos:
        +, -, *, /, %

        Operadores de Asignación:
        =, +=, -=, *=, /=, %=

        Operadores de Comparación:
        ==, !=, >, <, >=, <=

        Operadores Lógicos:
        &&, ||, !

        Operadores de Incremento y Decremento:
        ++, --
        */

        /*Estructuras de Control de C#
        Estructuras de Selección:
        if, else if, else, switch

        Estructuras de Repetición:
        for, while, do while, foreach

        Estructuras de Salto:
        break, continue, return

        Estructuras de manejo de excepciones:
        try, catch, finally, throw
        */

        //Ejemplos de operadores
        public void OperadoresAritmeticos()
        {
            int a = 10;
            int b = 5;

            Console.WriteLine("Suma: " + (a + b));
            Console.WriteLine("Resta: " + (a - b));
            Console.WriteLine("Multiplicación: " + (a * b));
            Console.WriteLine("División: " + (a / b));
            Console.WriteLine("Módulo: " + (a % b));
        }
        public void OperadoresAsignacion()
        {
            int a = 10;
            a += 5;
            Console.WriteLine("Asignación: " + a);
        }
        public void OperadoresComparacion()
        {
            int a = 10;
            int b = 5;

            Console.WriteLine("Igualdad: " + (a == b));
            Console.WriteLine("Desigualdad: " + (a != b));
            Console.WriteLine("Mayor que: " + (a > b));
            Console.WriteLine("Menor que: " + (a < b));
            Console.WriteLine("Mayor o igual que: " + (a >= b));
            Console.WriteLine("Menor o igual que: " + (a <= b));
        }
        public void OperadoresLogicos()
        {
            bool a = true;
            bool b = false;

            Console.WriteLine("AND: " + (a && b));
            Console.WriteLine("OR: " + (a || b));
            Console.WriteLine("NOT: " + (!a));
        }
        public void OperadoresIncrementoDecremento()
        {
            int a = 10;

            Console.WriteLine("Incremento: " + (++a));
            Console.WriteLine("Decremento: " + (--a));
        }
        
        //Ejemplos de estructuras de control

        public void EstructurasSeleccion()
        {
            int a = 10;

            if (a > 5)
            {
                Console.WriteLine("a es mayor que 5");
            }
            else if (a == 5)
            {
                Console.WriteLine("a es igual a 5");
            }
            else
            {
                Console.WriteLine("a es menor que 5");
            }

            switch (a)
            {
                case 1:
                    Console.WriteLine("a es igual a 1");
                    break;
                case 2:
                    Console.WriteLine("a es igual a 2");
                    break;
                default:
                    Console.WriteLine("a es mayor que 2 o menor que 1");
                    break;
            }
        }
        public void EstructurasRepeticion()
        {
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("For: " + i);
            }

            int j = 0;
            while (j < 5)
            {
                Console.WriteLine("While: " + j);
                j++;
            }

            int k = 0;
            do
            {
                Console.WriteLine("Do While: " + k);
                k++;
            } while (k < 5);

            int[] array = { 1, 2, 3, 4, 5 };
            foreach (int item in array)
            {
                Console.WriteLine("Foreach: " + item);
            }
        }
        public void EstructurasSalto()
        {
            for (int i = 0; i < 5; i++)
            {
                if (i == 3)
                {
                    break;
                }
                Console.WriteLine("Break: " + i);
            }

            for (int j = 0; j < 5; j++)
            {
                if (j == 3)
                {
                    continue;
                }
                Console.WriteLine("Continue: " + j);
            }

            for (int k = 0; k < 5; k++)
            {
                if (k == 3)
                {
                    return;
                }
                Console.WriteLine("Return: " + k);
            }
        }
        public void EstructurasManejoExcepciones()
        {
            try
            {
                int a = 10;
                int b = 0;
                int c = Division(a, b);

            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
            finally
            {
                Console.WriteLine("Bloque finally ejecutado");
            }
        }
        public int Division(int a, int b)
        {
            if (b == 0)
            {
                throw new Exception("No se puede dividir entre cero");
            }
            return a / b;
        }

        public static void DificultadExtra()
        {
            for (int i = 10; i <= 55; i++)
            {
                if(i % 2 == 0 && i != 16 && i % 3 != 0)
                Console.WriteLine(i);
            }
        } 
    }
}
