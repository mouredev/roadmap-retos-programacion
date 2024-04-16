/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */


using System;
namespace estuardodev
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Queue<string> queue = new Queue<string>();
            queue.Enqueue("Estuardo");
            queue.Enqueue("Lilian");
            queue.Enqueue("C#");
            queue.Enqueue("Python");

            Stack<string> stack = new Stack<string>();
            stack.Push("Estuardo");
            stack.Push("Lilian");
            stack.Push("C#");
            stack.Push("Python");

            Ejercicio(queue, stack);
            Web();
            Impresora();
        }
        

        static void  Ejercicio(Queue<string> values, Stack<string> valores) 
        {
            Console.WriteLine("-- Primero en entrar, Primero en salir --");
            foreach (var item in values)
            {
                Console.WriteLine(item.ToString());
            }


            Console.WriteLine("\n-- Último en entrar, Primero en salir --");
            foreach (var item in valores)
            {
                Console.WriteLine(item.ToString());
            }
        }

        static void Web()
        {
            Console.WriteLine("\n¿Qué desea hacer?");
            Stack<string> historial = new Stack<string>();
            string paginaActual = "Google";
            int contador = 0;

            while (contador < 5)
            {
                Console.WriteLine("Estas en : " + paginaActual);
                if (paginaActual.Equals("Google"))
                {
                    Console.Write("Ingrese un comando (adelante 'Nombre de la web'): ");
                }
                else
                {
                    Console.Write("Ingrese un comando (adelante 'Nombre de la web', 'atras'): ");
                }
                
                string comando = Console.ReadLine().ToLower();
                if (comando.Contains("adelante"))
                {
                    string[] palabrras = comando.Split(' ');
                    Console.WriteLine($"Entrando a {palabrras[1]}");
                    historial.Push(paginaActual);
                    paginaActual = palabrras[1];
                }
                else
                {
                    Console.WriteLine($"Regresando a {historial.Peek()}");
                    paginaActual = historial.Peek();
                    historial.Push(paginaActual);
                    
                }
                contador++;
            }
            if (contador == 5)
            {
                Console.WriteLine("\n Gracias por usar nuestro navegador :)");
            }
        }

        static void Impresora()
        {
            Queue<string> documentos = new Queue<string>();
            int contador = 0;

            while (contador < 5)
            {
                Console.WriteLine("\nPara imprimir escriba 'imprimir' o agregue documentos con 'agregar -Nombre-' y si desea imprimir un solo documento escriba 'imprimir -Nombre-'");
                string entrada = Console.ReadLine();
                if (entrada.Equals("imprimir"))
                {
                    foreach(string s in documentos)
                    {
                        Console.WriteLine($"Imprimiendo: {s}");
                    }
                    Console.WriteLine("\nDocumentos totalmente impresos.");
                    documentos.Clear();
                } else if (entrada.Contains("imprimir") && entrada.Length > 8)
                {
                    string[] valores = entrada.Split(" ");
                    Console.WriteLine($"Imprimiendo: {valores[1]}");
                    Console.WriteLine("\nDocumento totalmente impreso.");

                } else if (entrada.Contains("agregar"))
                {
                    string[] valores = entrada.Split(" ");
                    documentos.Enqueue(valores[1]);
                }
                contador ++;
            }
            if (contador == 5)
            {
                Console.WriteLine("\n Gracias por usar nuestra impresora :)");
            }
        }

    }
}
