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
namespace CeroUno
{
    class CeroUno
    {
        static void Main(string[] args)
        {
            int a = 2; int b = 3; int c = 4;

            //Aritméticos
            int suma = a + b;
            int resta = b - a;
            int multi = a * a;
            int divi = a / 2;
            int modulo = c % a;
            //Asignación
            int variable = 10;
            a += 5; //a es igual a 7
            c -= 1; //c es igual a 3
            b *= 2; //b es igual a 6
            c /= a; //b es igual a 2
            //Comparación
            bool igual = a == b;
            bool noIgual = a != b;
            bool mayorQue = a > b;
            bool menorQue = b > a;
            bool mayorIgualQue = a >= b;
            bool menorIgualQue = a <= b;
            //Lógicos
            bool x = true;
            bool y = false;
            bool z = true;

            bool yy = (x && x);
            bool o = (y || x);
            bool dif = !z;

            if (x == y)
            {
                z = true;
            } else if (y == z)
            {
                x = true;
            } else
            {
                x = false;
            }

            while(variable > c)
            {
                variable++;
            }

            try
            {
                if (!igual)
                {
                    Console.WriteLine("a y b NO SON IGUALES");
                }
            } catch
            {
                throw new Exception("Son iguales, cuidado!");
            }

            //Opcional
            for (int i = 10; i <= 55; i++)
            {
                if (i % 2 == 0 && i != 16 && i % 3 != 0)
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}