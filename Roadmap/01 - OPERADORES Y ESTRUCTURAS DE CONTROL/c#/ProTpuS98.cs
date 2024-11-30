using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.WebSockets;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;

namespace _01_OPERADORES_Y_ESTRUCTURAS_DE_CONTROL
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //EJERCICIO:
            //1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
            //   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
            //   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

            //2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos
            //   que representen todos los tipos de estructuras de control que existan
            //   en tu lenguaje:
            //   Condicionales, iterativas, excepciones... 

            //3. Debes hacer print por consola del resultado de todos los ejemplos.

            //4. DIFICULTAD EXTRA(opcional):
            //   Crea un programa que imprima por consola todos los números comprendidos
            //   entre 10 y 55(incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

            //   Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

            TiposOperadores operadores = new TiposOperadores();
            Console.WriteLine(operadores.getResultsArimeticos());
            Console.WriteLine(operadores.getResultsAsignacion());

            operadores.OperadoresDeComparacion();
            operadores.game();
            operadores.OperadoresLogicos();

        }

        public class TiposOperadores
        {
            private int num1;
            private int num2;

            private int userNum1;
            private int userNum2;
            private int userNum3;
            private int userNum4;
            private int userNum5;
            private int userNum6;

            private int addtraction;
            private int subtraction;
            private int multiply;
            private int divide;
            private int module;

            private int x;
            private int num3;
            private int num4;
            private int num5;
            private int num6;

            private int numA;
            private int numB;

            private string name;
            private string input;
            private int age;

            private int numRandom;
            private int myNum;
            private int attemps;

            private bool a;
            private bool b;
            private bool c1;
            private bool c2;
            private bool c3;
            private bool c4;

            private bool IsRaining;
            private bool ResultadoIsRaining;

            private int aBit;
            private int bBit;
            private int AND;
            private int OR;
            private int XOR;
            private int NOT;
            private int desplazamientoIzquierda;
            private int desplazamientoDerecha;

            private int aTernario;
            private int bTernario;
            private int resultadoTernario;
            private object obj;
            private string word;

            public TiposOperadores()
            {
                //EJERCICIO 1

                //1. ARIMETICOS
                num1 = 10;
                num2 = 50;

                addtraction = num1 + num2;
                subtraction = num1 - num2;
                multiply = num1 * num2;
                divide = num1 / num2;
                module = num1 % num2;

                //2. ASIGNACION
                x = 10;
                num3 = x += 5;
                num4 = x -= 5;
                num5 = x *= 5;
                num6 = x /= 4;

                //3. COMPARACION
                name = "";
                input = "";
                age = 0;

                //4. EJEMPLO COMPARACION CON JUEGO
                Random random = new Random();
                numRandom = random.Next(0, 100);
                myNum = 0;
                attemps = 0;

                //5. OPERADORES LOGICOS
                a = true;
                b = false;
                c1 = a && b;
                c2 = a || b;
                IsRaining = true;
                ResultadoIsRaining = !IsRaining;

                userNum1 = 0;
                userNum2 = 0;

                //6. OPERADORES bit a bit
                aBit = 6;
                bBit = 3;
                AND = aBit & bBit;
                OR = aBit | bBit;
                XOR = aBit ^ bBit;
                NOT = ~aBit;
                desplazamientoDerecha = aBit >> 1;
                desplazamientoIzquierda = bBit << 1;

                //7. OPERADORES MISCELANEOS
                aTernario = 50;
                bTernario = 100;
                obj = "hello";
                word = obj as string;
            }
            public string getResultsArimeticos()
            {
                return $"OPERADORES ARIMETICOS EN C#: Adición (+), Sustracción (-), Multiplicación (*), División (/), Módulo (%). Valor Num1 = ({num1}), Valor Num2 = ({num2})." + "\n" + "Addtraction: " + addtraction + "\n" + "Subtraction: " + subtraction + "\n" + "Multiply: " + multiply + "\n" + "Divide: " + divide + "\n" + "Module: " + module + "\n";
            }
            public string getResultsAsignacion()
            {
                return "OPERADORES DE ASIGNACION EN C#: valor de X = 10: " + "\n" + "(x += 5): " + num3 + "\n" + "(x -= 5): " + num4 + "\n" + "(x *= 5): " + num5 + "\n" + "(x /= 5): " + num6 + "\n";
            }

            public void OperadoresDeComparacion()
            {
                //OPERADORES DE COMPARACION
                Console.WriteLine("OPERADORES DE COMPARACION:" + "\n");

                Console.WriteLine("Escriba si para saber si puedes conducir");
                input = Console.ReadLine();

                if (input == "si")
                {
                    Console.WriteLine("Como te llamas?");
                    name = Console.ReadLine();
                    Console.WriteLine("Cuantos años tienes ?");
                    age = int.Parse(Console.ReadLine());

                    if (age <= 16)
                    {
                        Console.WriteLine("Debes tener 18 para poder tener el carnet de conducir");
                    }
                    else if (age >= 18)
                    {
                        Console.WriteLine("Tienes carnet?");
                        input = Console.ReadLine();

                        if (input == "si")
                        {
                            Console.WriteLine("Puedes conducir");
                        }
                        else
                        {
                            Console.WriteLine("no puedes conducir");
                        }
                    }
                }
 
            }
            //EJEMPLO COMPARACION CON JUEGO
            public void game()
            {
                Console.WriteLine("Le gustaria jugar a Adivina el numero oculto? 'si' o 'no'");
                input = Console.ReadLine();

                if (input == "si")
                {
                    Console.WriteLine("introduzca un numero del 1 a 100");

                    //OPERADOR UNARIO Y NEGACION LOGICO
                    while (myNum != numRandom)
                    {
                        myNum = int.Parse(Console.ReadLine());
                        if (myNum < numRandom)
                        {
                            Console.WriteLine("El numero oculto es mayor");
                        }
                        else if (myNum > numRandom)
                        {
                            Console.WriteLine("El numero oculto es menor");
                        }
                        //OPERADOR UNARIO
                        attemps++;
                    }
                    Console.WriteLine($"¡Felicidades! Total intentos utilizados: {attemps}");
                    Console.WriteLine();
                }
            }
            //OPERADORES LOGICOS
            public void OperadoresLogicos()
            {
                Console.WriteLine("OPERADORES LOGICOS: bool a = 'true', bool b = 'false'. c1 = a && b., c2 = a||b, c3 = !a");
                Console.WriteLine($"valor de c1: {c1}. El resultado es falso porque b es false");
                Console.WriteLine($"valor de c2: {c2}. el resultado es verdadero porque a es verdadero");
                Console.WriteLine($"valor de c3: {c3}. el resultado es falso porque a es verdadero");
                Console.WriteLine();

                Console.WriteLine("Le gustaria ver un ejemplo practico? 'si', 'no'");
                input = Console.ReadLine();

                //EJEMPLO CON OPERADOR LOGICO &&
                if (input == "si")
                {
                    Console.WriteLine("OPERADOR LOGICO '&&' DARA RESULTADO TRUE SOLO SI AMBAS CONDICIONES SON VERDADERAS");
                    Console.WriteLine("Introduzca un numero");
                    userNum1 = int.Parse(Console.ReadLine());

                    Console.WriteLine("Introduzca otro numero");
                    userNum2 = int.Parse(Console.ReadLine());

                    if (userNum1 > 0 && userNum2 > 0)
                    {
                        Console.WriteLine($"el numero {userNum1} y {userNum2} son positivos");
                    }
                    else
                    {
                        Console.WriteLine("Es falso porque uno de tus numeros es negativo");
                    }

                }
                Console.WriteLine("Le gustaria ver un EJEMPLO PRACTICO OPERADOR LOGICO (||)? escriba 'si' o 'no'");
                input = Console.ReadLine();
                if (input == "si")
                {
                    //EJEMPLO OPERADORES LOGICO (||)
                    Console.WriteLine("EJEMPLO PRACTICO OPERADOR LOGICO (||). solo sera 'true' si al menos uno de los dos numeros es positivo");
                    Console.WriteLine("Introduzca un numero");
                    userNum3 = int.Parse(Console.ReadLine());
                    Console.WriteLine("Introduzca otro numero");
                    userNum4 = int.Parse(Console.ReadLine());

                    if (userNum3 > 0 || userNum4 > 0)
                    {
                        Console.WriteLine("es 'True' porque al menos un numero es positivo");
                    }
                    else
                    {
                        Console.WriteLine("Es 'False' porque ambos numeros son negativos");
                    }
                    Console.WriteLine("\n");
                    //EJEMPLO OPERADOR LOGICO (!)
                    Console.WriteLine("EJEMPLO OPERADOR LOGICO (!) Invierte el valor");
                    Console.WriteLine($"Valor de IsRaining = {IsRaining}");
                    Console.WriteLine($"Valor de ResultadoIsraining = {ResultadoIsRaining}");
                }

                //OPERADORES BIT A BIT
                Console.WriteLine("OPERADORES bit a bit");
                Console.WriteLine("Escriba si para ver ejemplos");
                input = Console.ReadLine();
                Console.WriteLine("\n");
                if (input == "si")
                {
                    Console.WriteLine("int a = 5; int b = 3.");
                    Console.WriteLine("\n");
                    Console.WriteLine($"AND bit a bit (&). Compara cada bit de los dos números y devuelve 1 solo si ambos bits son 1. RESULTADO: {AND}");
                    Console.WriteLine($"OR bit a bit (|). devuelve 1 si al menos uno de los bits es 1. RESULTADO: {OR}");
                    Console.WriteLine($"XOR bit a bit (^). Este operador devuelve 1 cuando los bits son diferentes entre sí. RESULTADO: {XOR}");
                    Console.WriteLine($"NOT bit a bit (~). Este operador invierte los bits, cambiando los 1 por 0 y viceversa. RESULTADO: {NOT}");
                    Console.WriteLine($"Desplazamiento a la izquierda (<<). Este operador desplaza los bits hacia la izquierda y rellena con ceros. Equivale a multiplicar por 2 por cada desplazamiento. RESULTADO: {desplazamientoIzquierda}");
                    Console.WriteLine($"Desplazamiento a la derecha (>>). Este operador desplaza los bits hacia la derecha. Si el número es positivo, rellena con ceros; si es negativo, rellena con unos. RESULTADO: {desplazamientoDerecha}");
                }
                Console.WriteLine("\n");
                //OPERADORES UNARIOS
                Console.WriteLine("OPERADORES UNARIOS: (+) y (-): Indican el signo del número. (++) y (--): Incremento y decremento, tanto en forma pre como post. (!): Negación lógica. (~): Complemento a bit.");
                Console.WriteLine("Le gustaria ver un ejemplo de incremento y decremento?. 'si' o 'no'");
                input = Console.ReadLine();
                if(input == "si")
                {
                    Console.WriteLine("EJEMPLO INCREMENTO POR CADA VUELTA");
                    for (int i = 0; i <= 10; i++)
                    {
                        Console.WriteLine(i);
                    }

                    Console.WriteLine("EJEMPLO DECREMENTO POR CADA VUELTA");
                    for (int i = 10; i >= 0; i--)
                    {
                        Console.WriteLine(i);
                    }

                }
                //Operadores misceláneos
                Console.WriteLine("Operadores misceláneos: Incluyen operadores como el operador ternario y el operador de tipo. Ejemplos: ?: (operador ternario), is (verifica el tipo), as (convierte tipos).");
                Console.WriteLine("Escriba 'si' para ver ejemplo de cada uno");
                input= Console.ReadLine();

                if (input == "si")
                {
                    Console.WriteLine("1. Operador ternario (?:) es una forma compacta de una declaracion (if-else)");
                    Console.WriteLine($"valor de ternario aTernario = {aTernario}. valor de ternario bTernario = {bTernario}");
                    Console.WriteLine("\n");
                    resultadoTernario = aTernario > bTernario ? aTernario : bTernario;
                    Console.WriteLine("el numero mas mayor es: " + resultadoTernario);

                    Console.WriteLine("\n");

                    Console.WriteLine("2. Operador (is). este operador sirve para verificar de que tipo es un objecto");
                    Console.WriteLine("Escriba 'si' para mostrar un ejemplo");
                    input = Console.ReadLine();

                    if (input == "si")
                    {
                        Console.WriteLine("private object obj = 'hello'");
                        if (obj is string)
                        {
                            Console.WriteLine("obj es un tipo string");
                        }
                        else
                        {
                            Console.WriteLine("obj no es de tipo string");
                        }
                    }

                    Console.WriteLine("3. Operador (as). Este operador se utiliza para convertir un objeto a un tipo específico. Si la conversión no es posible, devuelve (Null) en vez de una exepcion");
                    Console.WriteLine("Escriba 'si' para mostrar un ejemplo");
                    input = Console.ReadLine();

                    if (input == "si")
                    {
                        if (word != null)
                        {
                            Console.WriteLine("se a realizado la convercion de manera correcta");
                        }
                    }
                    Console.WriteLine("\n");
                }
                //4. DIFICULTAD EXTRA(opcional):
                //Crea un programa que imprima por consola todos los números comprendidos
                //entre 10 y 55(incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
                Console.WriteLine("Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.");
                Console.WriteLine("escriba si para mostrar");
                input = Console.ReadLine();

                if (input == "si")
                {
                    Console.WriteLine("1. Numeros comprendidos entre 10 y 55");
                    for (int i = 10; i <= 55; i++)
                    {
                        Console.WriteLine(i);
                    }
                    Console.WriteLine("\n");
                    Console.WriteLine("pares, y que no son ni el 16 ni múltiplos de 3.");
                    for (int i = 0; i <= 20; i++)
                    {
                        if (i%2 == 0 && i != 16 && i%3 != 0)
                        {
                            Console.WriteLine(i);
                        }
                    }
                }

                
            }

        }
    }
}
