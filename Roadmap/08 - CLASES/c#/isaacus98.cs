/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */

namespace RetosProgramacion2024
{
    internal class Reto8
    {    
        static void Main(string[] args)
        {
            // Crear objeto persona y establecer valor a sus atributos
            Persona persona = new();
            persona.Nombre = "Isaac";
            persona.Edad = 26;

            // Imprimir atributos
            persona.ImprimirAtributos();

            // Canviar valor de los atributos
            persona.Nombre = "Sergi";
            persona.Edad = 25;

            // Imprimir atributos
            persona.ImprimirAtributos();

            // Reto extra
            Console.WriteLine("\nPila\n");
            Pila<int> pila = new();
            pila.Push(1);
            pila.Push(2);
            pila.Push(3);

            Console.WriteLine(pila.Size());
            pila.Print();
            Console.WriteLine("\n" + pila.Pop());


            Console.WriteLine("\nCola\n");
            Cola<int> cola = new();
            cola.Enqueue(1);
            cola.Enqueue(2);
            cola.Enqueue(3);

            Console.WriteLine(cola.Size());
            cola.Print();
            Console.WriteLine("\n" + cola.Dequeue());
        }
    }

    public class Persona
    {
        public string Nombre;
        public int Edad;

        public Persona()
        {

        }

        public void ImprimirAtributos()
        {
            Console.WriteLine($"Nombre: {Nombre}, Edad: {Edad}");
        }
    }


    // Reto extra
    public class Cola<T1>
    {
        private Queue<T1> queue;

        public Cola()
        {
            queue = new Queue<T1> ();
        }

        public void Enqueue(T1 item)
        {
            queue.Enqueue (item);
        }

        public T1 Dequeue()
        {
           return queue.Dequeue ();
        }

        public int Size()
        {
            return queue.Count ();
        }

        public void Print()
        {
            foreach (T1 item in queue)
            {
                Console.Write (item + " ");
            }
        }
    }

    public class Pila<T1>
    {
        private Stack<T1> stack;

        public Pila()
        {
            stack = new Stack<T1>();
        }

        public void Push(T1 item)
        {
            stack.Push(item);
        }

        public T1 Pop()
        {
            return stack.Pop();
        }

        public int Size()
        {
            return stack.Count();
        }

        public void Print()
        {
            foreach (T1 item in stack)
            {
                Console.Write(item + " ");
            }
        }
    }
}
