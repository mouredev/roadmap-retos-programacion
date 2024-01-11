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

using static System.Net.Mime.MediaTypeNames;

namespace RetosProgramacion2024
{
    internal class Reto1
    {
        static void Main(string[] args)
        {
            uint a = 0b_0000_1111_0000_1111_0000_1111_0000_1100;
            int x = 1;
            int y = 2;

            // Operadores de incremento
            Console.WriteLine(x++); // output: 1
            Console.WriteLine(++x); // output: 2

            // Operadores de decremento
            Console.WriteLine(x--); // output: 2
            Console.WriteLine(--x); // output: 1

            // Operador unario
            Console.WriteLine(-x); // output: -1
            Console.WriteLine(+x); // output: 1

            // Operadores aritmeticos
            Console.WriteLine(x + y); // output: 3
            Console.WriteLine(x - y); // output: -1
            Console.WriteLine(x * y); // output: 2
            Console.WriteLine(x / y); // output: 0
            Console.WriteLine(x % y); // output: 1

            // Operadores de asignación
            x = 5;
            Console.WriteLine(x); // output: 5 
            x += 9;
            Console.WriteLine(x); // output: 14
            x -= 4;
            Console.WriteLine(x); // output: 10
            x *= 2;
            Console.WriteLine(x); // output: 20
            x /= 4;
            Console.WriteLine(x); // output: 5
            x %= 2;
            Console.WriteLine(x); // output: 1
            
            bool myBool = true;
            myBool &= false;
            Console.WriteLine(myBool);  // output: False

            myBool |= true;
            Console.WriteLine(myBool);  // output: True

            myBool ^= false;
            Console.WriteLine(myBool);  // output: True

            a <<= 4;
            Console.WriteLine(Convert.ToString(a, toBase: 2)); // output: 11110000111100001111000011000000

            a >>= 2;
            Console.WriteLine(Convert.ToString(a, toBase: 2).PadLeft(4, '0'),4); // output: 111100001111000011110000110000

            // Operadores de comparación
            Console.WriteLine(x > y); // output: False
            Console.WriteLine(x < y); // output: True
            Console.WriteLine(x >= y); // output: False
            Console.WriteLine(x <= y); // output: True

            // Operadores lógicos
            Console.WriteLine(!true); // output: true
            Console.WriteLine(true & false); // output: False
            Console.WriteLine(true | false); // output: True
            Console.WriteLine(true ^ false); // output: True
            Console.WriteLine(false && true); // output: False
            Console.WriteLine(true || false); // output: True

            // Operadores de bit
            Console.WriteLine(Convert.ToString(~a, toBase: 2)); // output: 11110000111100001111000011110011

            a = 0b_1100_1001_0000_0000_0000_0000_0001_0001;
            Console.WriteLine($"Before: {Convert.ToString(a, toBase: 2)}"); // output: 11001001000000000000000000010001
            a <<= 4;
            Console.WriteLine($"After:  {Convert.ToString(a, toBase: 2)}"); // output: 10010000000000000000000100010000

            a = 0b_1001;
            Console.WriteLine($"Before: {Convert.ToString(a, toBase: 2),4}"); // output: 1001
            a >>= 2;
            Console.WriteLine($"After:  {Convert.ToString(a, toBase: 2).PadLeft(4, '0'),4}"); // output: 0010

            x = -8;
            Console.WriteLine($"Before:    {x,11}, hex: {x,8:x}, binary: {Convert.ToString(x, toBase: 2),32}"); // output: -8, hex: fffffff8, binary: 11111111111111111111111111111000
            y = x >> 2;
            Console.WriteLine($"After  >>: {y,11}, hex: {y,8:x}, binary: {Convert.ToString(y, toBase: 2),32}"); // output: -2, hex: fffffffe, binary: 11111111111111111111111111111110
            int z = x >>> 2;
            Console.WriteLine($"After >>>: {z,11}, hex: {z,8:x}, binary: {Convert.ToString(z, toBase: 2).PadLeft(32, '0'),32}"); // output: 1073741822, hex: 3ffffffe, binary: 00111111111111111111111111111110

            // Operadores de igualdad
            Console.WriteLine(x == y); // output: False
            Console.WriteLine(x != y); // output: True

            // Estructuras de control
            x = 1;
            y = 2;

            // if
            if (x == y)
                Console.WriteLine("x es igual a y");
            else
                Console.WriteLine("x no es igual a y");

            // switch
            switch(x)
            {
                case 0: 
                    Console.WriteLine($"x = {x}");
                    break;
                case 1:
                    Console.WriteLine($"x = {x}");
                    break;
                default:
                    Console.WriteLine("x no es 0 ni 1");
                    break;
            }
            
            // for
            for (int i = 0; i < 5; i++)
                Console.WriteLine(i);

            // while
            int j = 0;
            while (j < 5)
                Console.WriteLine(j++);

            // do while
            j = 0;
            do
                Console.WriteLine(j++);
            while (j < 5);

            // foreach
            string[] nombres = {"Isaac", "Sergi", "Gerard", "Pol", "Marc"};
            foreach (string nombre in nombres)
                Console.WriteLine(nombre);

            // try - catch
            try
            {
                x = 5;
                y = 0;
                int result = x/y;
            } 
            catch(DivideByZeroException e)
            {
                Console.WriteLine(e.Message);
            }

            //try - catch - finally
            try
            {
                x = 5;
                y = 0;
                int result = x / y;
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                Console.WriteLine("Se ejecuta despues de ejecutarse el código del bloque try o del bloque catch si ha saltado una excepción.");
            }

            // Reto extra
            RetoExtra();
        }

        private static void RetoExtra()
        {
            for (int i = 10; i <= 55; i++)
            {
                if ((i % 2 == 0) & i != 16 & i % 3 != 0)
                    Console.WriteLine(i);
            }
        }
    }
}
