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
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

namespace RetosProgramacion2024
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Queue
            Queue<int> fifo = new Queue<int>();

            // Insertar elementos en la cola
            fifo.Enqueue(1);
            fifo.Enqueue(2);
            fifo.Enqueue(3);
            fifo.Enqueue(4);

            // Mostrar elementos de la cola sin eliminar el elemento. El elemeto que se muestra se va al final de la cola
            fifo.Peek();
            fifo.Peek();
            fifo.Peek();
            fifo.Peek();

            // Mostrar elementos de la cola
            fifo.Dequeue();
            fifo.Dequeue();
            fifo.Dequeue();
            fifo.Dequeue();

            // Stack
            Stack<int> lifo = new Stack<int>();

            // Insertar elementos en la pila
            lifo.Push(1);
            lifo.Push(2);
            lifo.Push(3);
            lifo.Push(4);

            // Mostrar elementos de la pila sin eliminar el elemento. El elemeto que se muestra se va al final de la pila
            lifo.Peek();
            lifo.Peek();
            lifo.Peek();
            lifo.Peek();

            // Mostrar elementos de la pila
            lifo.Pop();
            lifo.Pop();
            lifo.Pop();
            lifo.Pop();

            // Dificultad extra
            NavegadorWeb();
            ImpressoraCompartida();
        }

        private static void NavegadorWeb()
        {
            Console.WriteLine("Escribe \"salir\" para salir de la aplicación");
            Console.WriteLine("Escribe \"adelante\" para moverte hacia adelante");
            Console.WriteLine("Escribe \"atras\" para moverte hacia atras");

            Stack<string> stackBack = new();
            Stack<string> stackForward = new();
            bool exit = false;
            string webname = "";

            while (!exit)
            {
                Console.WriteLine("Escribe el comando o nombre de la web:");
                string? temp = Console.ReadLine();
                temp ??= "";

                switch (temp.ToLower())
                {
                    case "atras":
                        if (stackBack.Count == 0)
                        {
                            Console.WriteLine("No se puede ir atras");
                            break;
                        }

                        stackForward.Push(webname);
                        webname = stackBack.Pop();
                        Console.WriteLine($"web: {webname}");
                        break;
                    case "adelante":
                        if (stackForward.Count == 0)
                        {
                            Console.WriteLine("No se puede ir adelante");
                            break;
                        }

                        stackBack.Push(webname);
                        webname = stackForward.Pop();
                        Console.WriteLine($"Web: {webname}");
                        break;
                    case "salir":
                        exit = true;
                        break;
                    default:
                        if (temp != "")
                        {
                            if (webname != "")
                                stackBack.Push(webname);
                            webname = temp;
                            Console.WriteLine($"Web: {webname}");
                        }
                        break;
                }
            }
        }

        private static void ImpressoraCompartida()
        {
            Console.WriteLine("Escribe \"salir\" para salir de la aplicación");
            Console.WriteLine("Escribe \"imprimir\" para imprimir el documente");

            Queue<string> documentos = new();
            bool exit = false;

            while (!exit)
            {
                Console.WriteLine("Escribe el comando o el nombre del documento:");
                string? temp = Console.ReadLine();
                temp ??= "";

                switch (temp.ToLower())
                {
                    case "imprimir":
                        if (documentos.Count == 0)
                        {
                            Console.WriteLine("No hay documetos en la cola");
                        }
                        else
                        {
                            Console.WriteLine($"Imprimiendo el documento {documentos.Dequeue()}");
                        }
                        break;
                    case "salir":
                        exit = true;
                        break;
                    default:
                        if (temp != "")
                            documentos.Enqueue(temp);
                        break;
                }
            }
        }
    }
}
