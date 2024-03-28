using System;
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

namespace elliotwith1T
{
    class Program
    {
        static void Main(string[] args)
        {
            #region Ejercicio 1

            //Aritmeticos:

            //Addition
            int add = 5 + 5;

            //Subtraction
            int sub = 10 - 7;

            //Multiplication 

            int mult = 5 * 5;

            //Division
            int div = 100 / 10;

            //Modulus
            int remainder = 10 % 3;

            //Increment
            int x = ++mult;
            mult--;//reset

            //Decrement
            int y = sub;
            y--;



            Console.WriteLine("Suna:" + add);
            Console.WriteLine("Subtraccion:" + sub);
            Console.WriteLine("Multiplicacion:" + mult);
            Console.WriteLine("Division:" + div);
            Console.WriteLine("Sobra:" + remainder);
            Console.WriteLine("Incremento:" + x);
            Console.WriteLine("Decremento:" + y);

            #endregion

            #region Ejercicio 2

            int num1 = 5;
            int num2 = 10;

            //Operadores Condicionales
            bool igualQue = (num1 == num2);
            bool diferenteQue = (num1 != num2);
            bool mayorQue = (num1 > num2);
            bool menorQue =  (num1 < num2);
            bool mayorOIgualQue =  (num1 >= num2);
            bool Que = (num1 <= num2);

            bool[] condicionales = new bool[igual, diferente, mayorQue, menorQue, mayorOIgualQue, Que];

            for(int i = 0; i<condicionales.Length; i++)
            {
                Console.WriteLine("num1 esta " + condicionales[i].Name + " num2 = " + condicionales[i]);
            }


            //Operadores Logicos
            bool and = (num1 > 0) && (num2 < 0);
            bool or = (num1 > 0) || (num2 < 0);
            bool not = !(num1 > 0);

            //Iterativas
            while(num1 < 10)
            {

                Console.WriteLine("num1 = " num1);
                int++;
            }

            do
            {
                Console.WriteLine("num1 is < 10")
            } while (num1 < 10);



            //for, foreach, do, while



            //Excepciones
            //try, catch, and finally


            #endregion

            #region Ejercicio 3

            for(int i =10; i<56; i++)
            {
               if(i % 2 == 0 && i !=16 && i%3 !=0)
                {
                    Conole.WriteLine(i);
                }
               
            }

            #endregion

        }

    }

}

