using System;
using System.Collections;
using System.Collections.Generic;
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

namespace R07___2024
{
    class NavegadorWeb
    {
        private Stack<string> historial = new Stack<string>();
        private Stack<string> historialAtras = new Stack<string>();

        public void Navegar(string pagina)
        {
            Console.WriteLine($"Navegando a: {pagina}");
            historial.Push(pagina);
            historialAtras.Clear(); // Limpiar el historial hacia atrás cuando se navega a una nueva página
        }

        public void Atras()
        {
            if (historial.Count > 1)
            {
                string paginaActual = historial.Pop();
                historialAtras.Push(paginaActual);

                string paginaAnterior = historial.Peek();
                Console.WriteLine($"Volviendo atrás a: {paginaAnterior}");
            }
            else
            {
                Console.WriteLine("No hay páginas anteriores para retroceder.");
            }
        }

        public void Adelante()
        {
            if (historialAtras.Count > 0)
            {
                string paginaSiguiente = historialAtras.Pop();
                historial.Push(paginaSiguiente);

                Console.WriteLine($"Avanzando adelante a: {paginaSiguiente}");
            }
            else
            {
                Console.WriteLine("No hay páginas siguientes para avanzar.");
            }
        }
    }

    class ImpresoraCompartida
    {
        private Queue<string> documentos = new Queue<string>();

        public void AgregarDocumento(string documento)
        {
            documentos.Enqueue(documento);
            Console.WriteLine($"Documento '{documento}' agregado a la cola de impresión.");
        }

        public void Imprimir()
        {
            if (documentos.Count > 0)
            {
                string documento = documentos.Dequeue();
                Console.WriteLine($"Imprimiendo documento: {documento}");
            }
            else
            {
                Console.WriteLine("No hay documentos en la cola de impresión.");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //Pila: 
            //Pila con diferentes objetos:
            Stack stackList = new Stack();
            //añado elementos varios:
            stackList.Push(1);
            stackList.Push(2);
            stackList.Push("a");
            stackList.Push("b");

            //Elimino elementos:
            //Con pop solo elimino el primer elemento del principio:
            stackList.Pop();
            stackList.Pop();
            //Con clear elimino todos los elementos
            stackList.Clear();

            //Pila tipo array, sólo con elementos de un mismo tipo
            Stack<int> stackInt = new Stack<int>();
            //añado elementos varios:
            stackInt.Push(1);
            stackInt.Push(2);
            stackInt.Push(3);
            stackInt.Push(4);

            //Elimino elementos:
            //Con pop solo elimino el primer elemento del principio:
            stackInt.Pop();
            stackInt.Pop();
            //Con clear elimino todos los elementos
            stackInt.Clear();

            //Colas:
            //Con diferentes tipos: 
            Queue queueList = new Queue();
            //Encolo / añado elementos a la lista: 
            queueList.Enqueue(1);
            queueList.Enqueue("Hola");
            //Quito el objeto al principio de la cola:
            queueList.Dequeue();
            //Elimino todos los elementos de la cola:
            queueList.Clear();

            //Colas:
            //Con un mismo tipo: 
            Queue<int> queueInt = new Queue<int>();
            //Encolo / añado elementos a la lista: 
            queueInt.Enqueue(1);
            queueInt.Enqueue(2);
            //Quito el objeto al principio de la cola:
            queueInt.Dequeue();
            //Elimino todos los elementos de la cola:
            queueInt.Clear();

            //Dificultad adicional adaptado a consola:
            NavegadorWeb navegador = new NavegadorWeb();

            while (true)
            {
                Console.WriteLine("Ingrese una URL para navegar, 'adelante' para avanzar, 'atrás' para retroceder, o 'salir' para terminar:");
                string input = Console.ReadLine();

                if (input.ToLower() == "salir")
                {
                    break;
                }
                else if (input.ToLower() == "adelante")
                {
                    navegador.Adelante();
                }
                else if (input.ToLower() == "atrás")
                {
                    navegador.Atras();
                }
                else
                {
                    navegador.Navegar(input);
                }
            }

            //Dificultad adicional impresora:
            ImpresoraCompartida impresora = new ImpresoraCompartida();

            while (true)
            {
                Console.WriteLine("Ingrese 'imprimir' para imprimir un documento o el nombre de un documento para agregarlo a la cola:");
                string input = Console.ReadLine();

                if (input.ToLower() == "imprimir")
                {
                    impresora.Imprimir();
                }
                else
                {
                    impresora.AgregarDocumento(input);
                }
            }



        }
    }
}
