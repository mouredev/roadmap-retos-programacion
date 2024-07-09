namespace _01_operadores
{
    internal class Program
    {
        static void Main(string[] args)
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


            // Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
            // Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

            // 1. Operadores Aritmeticos
            //  1.1a - Incremento 
            Console.WriteLine("------- Incremento A ---------------");
            int example = 0;

            Console.WriteLine($"example = {example}");
            Console.WriteLine($"example++ = {example++}");
            Console.WriteLine($"example = {example}");

            // 1.1b - Incremento
            Console.WriteLine("------- Incremento B ---------------");
            example = 0;
            Console.WriteLine($"example = {example}");
            Console.WriteLine($"++example = {++example}");
            Console.WriteLine($"example = {example}");

            // 1.2a - Decremento
            Console.WriteLine("------- Decremento A ---------------");
            example = 0;
            Console.WriteLine($"example = {example}");
            Console.WriteLine($"example-- = {example--}");
            Console.WriteLine($"example = {example}");

            // 1.2b - Decremento
            Console.WriteLine("------- Decremento B ---------------");
            example = 0;
            Console.WriteLine($"example = {example}");
            Console.WriteLine($"--example = {--example}");
            Console.WriteLine($"example = {example}");

            // 1.3 - Unarios
            Console.WriteLine("------- Unario ---------------");
            example = 1;
            Console.WriteLine($"example = {example}");
            Console.WriteLine($"+example = {+example}");
            Console.WriteLine($"-example = {-example}");
            Console.WriteLine($"-(-example) = {-(-example)}");

            // 1.4 - Multiplicación
            Console.WriteLine("------- Multiplicación ---------------");
            int exampleA = 3;
            int exampleB = 4;
            Console.WriteLine($"{exampleA} * {exampleB} = {exampleA * exampleB}");

            // 1.5 - División
            Console.WriteLine("------- División ---------------");
            exampleA = 3;
            exampleB = 4;
            Console.WriteLine($"{exampleA} / {exampleB} = {(double)exampleA / exampleB}");

            // 1.6 - Resto
            Console.WriteLine("------- Resto ---------------");
            exampleA = 3;
            exampleB = 4;
            Console.WriteLine($"{exampleA} % {exampleB} = {exampleA % exampleB}");

            // 1.7 - Suma
            Console.WriteLine("------- Suma ---------------");
            exampleA = 3;
            exampleB = 4;
            Console.WriteLine($"{exampleA} + {exampleB} = {exampleA + exampleB}");

            // 1.8 - Resta
            Console.WriteLine("------- Resta ---------------");
            exampleA = 3;
            exampleB = 4;
            Console.WriteLine($"{exampleA} - {exampleB} = {exampleA - exampleB}");

            // 1.9 - Asignación compuesta
            Console.WriteLine("------- Asignación compuesta ---------------");
            example = 5;
            Console.WriteLine($"example = {example}");

            example += 9;
            Console.WriteLine($" += 9 = {example}");

            example -= 4;
            Console.WriteLine($" -= 4 = {example}");

            example *= 2;
            Console.WriteLine($"*= 2 = {example}");

            example /= 4;
            Console.WriteLine($" /= 4 = {example}");

            example %= 3;
            Console.WriteLine($" %= 3 = {example}");


            Console.WriteLine("----------------------------------------------");
            Console.WriteLine("----------------------------------------------");


            // 2. Operadores de Comparación
            //  2.1 - Menor que (<)
            Console.WriteLine("------- Menor que (<) ---------------");
            Console.WriteLine($"{7.0} < {5.1} = {7.0 < 5.1}");
            Console.WriteLine($"{5.0} < {5.1} = {5.0 < 5.1}");

            //  2.2 - Mayor que (>)
            Console.WriteLine("------- Mayor que (>) ---------------");
            Console.WriteLine($"{7.0} > {5.1} = {7.0 > 5.1}");
            Console.WriteLine($"{5.0} > {5.1} = {5.0 > 5.1}");

            //  2.3 - Menor o igual que (<=)
            Console.WriteLine("------- Menor o igual que (<=) ---------------");
            Console.WriteLine($"{7.0} <= {5.1} = {7 <= 5.1}");
            Console.WriteLine($"{5.0} <= {5.0} = {5 <= 5}");

            //  2.4 - Mayor o igual que (>=)
            Console.WriteLine("------- Mayor o igual que (>=) ---------------");
            Console.WriteLine($"{7.0} >= {5.1} = {7 >= 5.1}");
            Console.WriteLine($"{5.0} >= {5.0} = {5 >= 5}");


            Console.WriteLine("----------------------------------------------");
            Console.WriteLine("----------------------------------------------");


            // 3. Operadores de Comparación
            //  3.1 - Operador de negación lógico !
            Console.WriteLine("------- Operador de negación lógico ! ---------------");
            bool passed = false;
            Console.WriteLine($"!passed = {!passed}");
            Console.WriteLine($"!true = {!true}");

            //  3.2 - Operador lógico AND &
            Console.WriteLine("------- Operador de negación lógico & ---------------");
            bool a = false & true;
            Console.WriteLine($"false & true = {a}");

            bool b = true & true;
            Console.WriteLine($"true & true = {b}");

            //  3.3 - Operador IR exclusivo lógico ^
            Console.WriteLine("------- Operador IR exclusivo lógico ^ ---------------");
            Console.WriteLine($"true ^ true = {true ^ true}");
            Console.WriteLine($"true ^ false = {true ^ false}");
            Console.WriteLine($"false ^ true = {false ^ true}");
            Console.WriteLine($"false ^ false = {false ^ false}");

            //  3.4 - Operador lógico OR |
            Console.WriteLine("------- Operador lógico OR | ---------------");
            a = false | true;
            Console.WriteLine($"false | true = {a}");

            b = true | true;
            Console.WriteLine($"true | true = {b}");

            //  3.5 - Operador lógico condicional AND &&
            Console.WriteLine("------- Operador lógico condicional AND && ---------------");
            a = false && true;
            Console.WriteLine($"false && true = {a}");

            b = true && true;
            Console.WriteLine($"true && true = {b}");

            //  3.6 - Operador OR lógico condicional ||
            Console.WriteLine("------- Operador OR lógico condicional || ---------------");
            a = false || true;
            Console.WriteLine($"false || true = {a}");

            b = true || true;
            Console.WriteLine($"true || true = {b}");


            Console.WriteLine("----------------------------------------------");
            Console.WriteLine("----------------------------------------------");


            // 4. Operadores de desplazamiento y bit a bit
            //  4.1 - Operador de complemento bit a bit ~
            Console.WriteLine("------- Operador de complemento bit a bit ~ ---------------");
            uint ae = 0b_0000_1111_0000_1111_0000_1111_0000_1100;
            uint be = ~ae;
            Console.WriteLine($"{~ae} = {Convert.ToString(be, toBase: 2)}");

            //  4.2 - Operador de desplazamiento izquierdo <<
            Console.WriteLine("------- Operador de desplazamiento izquierdo << ---------------");
            uint x = 0b_1100_1001_0000_0000_0000_0000_0001_0001;
            Console.WriteLine($"Before: {Convert.ToString(x, toBase: 2)}");

            uint y = x << 4;
            Console.WriteLine($"After:  {Convert.ToString(y, toBase: 2)}");

            //  4.3 - Operador de desplazamiento a la derecha >>
            Console.WriteLine("------- Operador de desplazamiento a la derecha >> ---------------");
            x = 0b_1001;
            Console.WriteLine($"Before: {Convert.ToString(x, toBase: 2),4}");

            y = x >> 2;
            Console.WriteLine($"After:  {Convert.ToString(y, toBase: 2).PadLeft(4, '0'),4}");

            //  4.4 - Operador de desplazamiento a la derecha sin signo >>>
            Console.WriteLine("------- Operador de desplazamiento a la derecha sin signo >>> ---------------");
            int xa = -8;
            Console.WriteLine($"Before:    {xa,11}, hex: {xa,8:x}, binary: {Convert.ToString(xa, toBase: 2),32}");

            int ya = xa >> 2;
            Console.WriteLine($"After  >>: {ya,11}, hex: {ya,8:x}, binary: {Convert.ToString(ya, toBase: 2),32}");

            int za = xa >>> 2;
            Console.WriteLine($"After >>>: {za,11}, hex: {za,8:x}, binary: {Convert.ToString(za, toBase: 2).PadLeft(32, '0'),32}");


            Console.WriteLine("----------------------------------------------");
            Console.WriteLine("----------------------------------------------");


            // 5. Operadores de igualdad
            //  5.1 - Operador de igualdad ==
            Console.WriteLine("------- Operador de igualdad == ---------------");
            int au = 1 + 2 + 3;
            int bu = 6;
            Console.WriteLine($"{au} == {bu} = {au == bu}");  // output: True

            char c1 = 'a';
            char c2 = 'A';
            Console.WriteLine($"{c1} == {c2} = {c1 == c2}");  // output: False
            Console.WriteLine($"{c1} == {char.ToLower(c2)} = {c1 == char.ToLower(c2)}");  // output: True

            //  5.2 - Operador de desigualdad !=
            Console.WriteLine("------- Operador de desigualdad != ---------------");
            int a2 = 1 + 1 + 2 + 3;
            int b2 = 6;
            Console.WriteLine($"{a2} != {b2} = {a2 != b2}");  // output: True

            string s1 = "Hello";
            string s2 = "Hello";
            Console.WriteLine($"{s1} != {s2} = {s1 != s2}");  // output: False

            object o1 = 1;
            object o2 = 1;
            Console.WriteLine($"{o1} != {o2} = {o1 != o2}");  // output: True


            Console.WriteLine("----------------------------------------------");
            Console.WriteLine("----------------------------------------------");


            // 1. Estructuras de Control
            //  1.1 - if
            int a5 = 5;
            int a6 = 6;
            if (a5 == 5)
            {
                Console.WriteLine("Son iguales");
            } else
            {
                Console.WriteLine("No son iguales");
            }

            if (a5 != a6)
            {
                Console.WriteLine("Son iguales");
            }
            else
            {
                Console.WriteLine("No son iguales");
            }

            //  1.2 - switch
            switch(a5)
            {
                case 1: 
                    Console.WriteLine("1");
                    break;

                case 2: 
                    Console.WriteLine("2");
                    break;

                case 3: 
                    Console.WriteLine("3");
                    break;

                 case 4:
                    Console.WriteLine("4");
                    break;

                 case 5: 
                    Console.WriteLine("5");
                    break;

                default:
                    Console.WriteLine("Es otro valor");
                    break;
            }

            //  1.3 - while
            int aWhile = 0;
            while (aWhile != 10)
            {
                aWhile++;
                Console.WriteLine($"aWhile: {aWhile}");
            }

            //  1.4 - for
            for(int j = 0; j < 10; j++)
            {
                Console.WriteLine($"j: {j}");
            }

            //  1.5 - foreach
            string[] matriz = { "rojo", "verde", "azul", "blanco" };
            foreach(string elemento in matriz)
            {
                Console.WriteLine($"elemento: {elemento}");
            }

            //  1.6 - do while
            aWhile = 0;
            do {
                aWhile++;
                Console.WriteLine($"aWhile: {aWhile}");

            } while (aWhile != 10);




            Console.WriteLine("----------------------------------------------");
            Console.WriteLine("----------------------------------------------");
            Console.WriteLine("------ Ejercicio ---------------");

            // Crea un programa que imprima por consola todos los números:
            //  - comprendidos entre 10 y 55(incluidos)
            //  - pares
            //  - no son ni el 16
            //  - ni múltiplos de 3
            for (int i = 10; i < 56; i++)
            {
                if (i % 2 == 0 && i != 16 && i % 3 == 0) 
                { 
                    Console.WriteLine(i);
                }
            }
        }
    }
}
