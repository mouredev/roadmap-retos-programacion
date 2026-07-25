using System;

namespace Xperiargluna
{
    class Program
    {
        static void Main(string[] args)
        {
            //OPERADORES ARITMÉTICOS
            Console.WriteLine($"Suma: 10 + 2 = {10 + 2}");
            Console.WriteLine($"Resta: 10 - 2 = {10 - 2}");
            Console.WriteLine($"Multiplicación: 10 * 2 = {10 * 2}");
            Console.WriteLine($"División: 10/ 2 = {10 / 2}");
            Console.WriteLine($"Módulo: 10 % 2 = {10 % 2}");

            //OPERADORES DE COMPARACIÓN
            Console.WriteLine($"Igualdad: 10 == 2 es {10 == 3}");
            Console.WriteLine($"Desigualdad: 10 != 2 es {10 != 3}");
            Console.WriteLine($"Mayor que: 10 > 2 es {10 > 3}");
            Console.WriteLine($"Menor que: 10 < 2 es {10 < 3}");
            Console.WriteLine($"Mayor o igual que: 10 >= 2 es {10 >= 3}");
            Console.WriteLine($"Menor o igual que: 10 <= 2 es {10 <= 3}");

            //OPERADORES LÓGICOS
            Console.WriteLine($"AND &&: 10 + 2 == 12 and 5 -1 == 4 es {10 + 2 == 12 && 5 - 1 == 4}");
            Console.WriteLine($"OR ||: 10 + 2 == 12 or 5 -1 == 2 es {10 + 2 == 12 || 5 - 1 == 2}");
            Console.WriteLine($"NOT !:  10 + 2 != 10 es {10 + 2 != 10}");

            //OPERADORES DE ASIGNACIÓN
            int my_number = 3;      //asignación
            Console.WriteLine(my_number);
            my_number += 1;       //suma y asignación
            Console.WriteLine(my_number);
            my_number -= 1;      //resta y asignación
            Console.WriteLine(my_number);
            my_number *= 2;      //multiplicación y asignación
            Console.WriteLine(my_number);
            my_number /= 2;      //división y asignación
            Console.WriteLine(my_number);
            my_number %= 2;       //módulo y asignación
            Console.WriteLine(my_number);

            //OPERADORES DE PERTENENCIA
            //contains - contiene
            string texto = "Hola, c#";
            bool contiene = texto.Contains("c#");
            Console.WriteLine(contiene);

            //OPERADORES DE IDENTIDAD 
            //ReferenceEquals en objetos
            object obj1 = new object();
            object obj2 = obj1;
            object obj3 = new object();

            Console.WriteLine(object.ReferenceEquals(obj1, obj2));
            Console.WriteLine(object.ReferenceEquals(obj1, obj3));


            //OPERADORES DE BIT
            // 7 = 0111
            // 4 = 0100
            Console.WriteLine($"AND: 7 & 4 = {7 & 4}"); // 0100
            Console.WriteLine($"OR: 7 | 4 = {7 | 4}"); // 0111
            Console.WriteLine($"XOR: 7 ^ 4 = {7 ^ 4}"); // 0011
            Console.WriteLine($"NOT: ~7 = {~7}"); // invierte los bits de 0111 a 1000 
            Console.WriteLine($"Desplazamiento a la derecha: 7 >> 2 = {7 >> 2}"); // 0001
            Console.WriteLine($"Desplazamiento a la izquierda: 7 << 2 = {7 << 2}"); // 011100


            //ESTRUCTURAS DE CONTROL

            //condicionales
            string my_name = "Jesús";

            if (my_name == "Pepe")
            {
                Console.WriteLine("Mi nombre es Pepe");
            }
            else if (my_name == "Jesús")
            {
               Console.WriteLine("Mi nombre es Jesús");   
            }
            else
            { 
                  Console.WriteLine("Mi nombre no es Pepe");         
            }

            //iterativas bucle for

            for (int i = 0; i < 6; i++)
            {
                Console.WriteLine(i);
            }

            //bucle while
            int contador = 1;
            while (contador <= 5) 
            {
                Console.WriteLine($"Número: {contador}");
                contador++; //incrementa el contador
            }

            //bucle do while 
            int contador2 = 2;
            do
            {
                Console.WriteLine($"Número: {contador2}");
                contador2++;
            }
            while (contador2 <= 5);

            //excepciones
            try
            {
                int divisor = 0;
                int resultado = 10 / divisor;
            }
            catch (DivideByZeroException error)
            {
                Console.WriteLine("Se ha producido un error " + error.Message);
            }
            finally 
            {
                Console.WriteLine("Operación finalizada ");           
            }

            //Ejercicio extra 
            for (int i = 10; i <= 56; i++)
            {
                if (i % 2 == 0 && i != 16 && i % 3 != 0 )
                {
                    Console.WriteLine(i);
                }
            }
            
        }
    }
}
