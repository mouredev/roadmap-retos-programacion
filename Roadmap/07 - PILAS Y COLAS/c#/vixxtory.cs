using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Net.NetworkInformation;
using System.Runtime.Intrinsics.X86;
using System.Security.Cryptography.X509Certificates;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace RetosProgramacion
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Las colecciones en C Sharp son grupos de objetos relacionados.
              Se diferencian de las matrices en que permiten aumentar o disminuir su capacidad de manera dinámica.       
              Las colecciones genéricas que se encuentran en el espacio de nombres System.Collections.Generic son:
              List<T>, Queue<T>, Stack<T> y Dictionary<TKey, TValue>.*/

            //La clase Queue<T> (cola) es una colección de elementos organizados “FIFO”; los primeros elementos en entrar son los primeros en salir.
            Queue<string> kings = new Queue<string>();
            kings.Enqueue("Arturo");
            kings.Enqueue("Alejandro");
            kings.Enqueue("Melchor");
            kings.Enqueue("Gaspar");
            kings.Enqueue("Baltasar");
            foreach(var king in kings)
            {
                Console.WriteLine($"{king}");
            }
            Console.WriteLine("\n");
            Console.WriteLine(kings.Dequeue()); //Elimina y devuelve el elemento en el principio de la cola.
            Console.WriteLine(kings.Peek()); //Devuelve el elemento en el principio de la cola sin eliminarlo.
            Console.WriteLine("\n");
            foreach (var king in kings)
            {
                Console.WriteLine($"{king}");
            }

            //La clase Stack<T> (pila) es una colección de objetos organizados “LIFO”; los últimos en entrar son los primeros en salir.
            Stack<string> pizzas= new Stack<string>();
            pizzas.Push("Cuatro estaciones"); //Añade elementos al principio de la pila
            pizzas.Push("Romana");
            pizzas.Push("Barbacoa");
            foreach (var pizza in pizzas)
            {
                Console.WriteLine(pizza);
            }
            Console.WriteLine("\n");
            Console.WriteLine(pizzas.Pop()); //Elimina y devuelve el elemento en el principio de la pila.
            Console.WriteLine(pizzas.Peek()); //Devuelve el elemento al principio de la pila sin eliminarlo
            Console.WriteLine("\n");
            foreach (var pizza in pizzas)
            {
                Console.WriteLine(pizza);
            }

            //Introduccion y recuperacion de elementos con List
            List<int> list = new List<int>();
            list.Add(1); // Añade elementos al final de la lista como en el caso de las colas (Queue)
            list.Add(2);
            list.Add(3);
            list.Add(4);
            list.Add(5);
            foreach (int item in list)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("\n");
            list.Insert(0, 0); //Añade el elemento al comienzo de la lista como en el caso de las pilas (Stack)
            list.Insert(0, -1);
            foreach (int item in list)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("\n");
            Console.WriteLine(list[0]); //Devuelve el primer elemento de la lista como Peek() en las colas
            Console.WriteLine(list[list.Count - 1]); //Devuelve el ultimo elemento de la lista como Peek() en las pilas
            
            //DIFICULTAD EXTRA
            
            //NAVEGACION WEB
            //Agrego dos pilas, una para las paginas de la izquierda y otras para las de la derecha
            Stack<string> websIzq = new Stack<string>();
            //A la pila de la izquierda le agrego todos los valores iniciales
            Stack<string> websDer = new Stack<string>();
            websIzq.Push("web A");
            websIzq.Push("web B");
            websIzq.Push("web C");
            websIzq.Push("web D");
            //Pagino hacia atras
            navegarAtras(websIzq, websDer);
            navegarAtras(websIzq, websDer);
            navegarAtras(websIzq, websDer);
            //Pagino hacia adelante
            navegarAdelante(websIzq, websDer);
            navegarAdelante(websIzq, websDer);

            //IMPRESORA
            Queue<string> impresora = new Queue<string>();
            //Se agregan documentos a la cola
            impresora.Enqueue("DOC 1");
            impresora.Enqueue("DOC 2");
            impresora.Enqueue("DOC 3");
            impresora.Enqueue("DOC 4");
            impresora.Enqueue("DOC 5");
            //Se imprimen los documentos por orden de llegada
            imprimir(impresora);
            imprimir(impresora);
            imprimir(impresora);
            imprimir(impresora);
            imprimir(impresora);
            imprimir(impresora);
        }

        static void navegarAtras(Stack<string> pilaIzquierda, Stack<string> pilaDerecha)
        {
            if (pilaIzquierda.Count() != 0)
            {
                pilaDerecha.Push(pilaIzquierda.Pop());
                Console.WriteLine(pilaIzquierda.Peek());
                Console.WriteLine("\n");
            }
            else
                Console.WriteLine("No es posible realizar la accción");
        }
        static void navegarAdelante(Stack<string> pilaIzquierda, Stack<string> pilaDerecha)
        {
            if (pilaDerecha.Count() != 0)
            {
                pilaIzquierda.Push(pilaDerecha.Pop());
                Console.WriteLine(pilaIzquierda.Peek());
                Console.WriteLine("\n");
            }
            else
                Console.WriteLine("No es posible realizar la acción");
        }
        static void imprimir(Queue<string> impresora)
        {
            if (impresora.Count() > 0)
                Console.WriteLine(impresora.Dequeue());
            else
                Console.WriteLine("No se encuentran documentos disponibles para imprimir");
        }
    }
}


