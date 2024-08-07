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
 * 
 */

namespace estuardodev
{
    internal class estuardodev
    {
        public static void Main(string[] args)
        {
            Personaje personaje = new Personaje("Ninja", "10", 100);
            personaje.Imprimir();
        }
    }

    // Reto
    internal class Personaje
    {
        private string nombre;
        private string fuerza;
        private int vida;

        public Personaje(string nombre, string fuerza, int vida)
        {
            this.nombre = nombre;
            this.fuerza = fuerza;
            this.vida = vida;
        }

        public void Imprimir()
        {
            Console.WriteLine("Nombre: " + nombre);
            Console.WriteLine("Fuerza: " + fuerza);
            Console.WriteLine("Vida: " + vida);

            Pila pila = new Pila();
            pila.add("Pila 1");
            pila.add("Pila 2");
            pila.add("Pila 3");

            Console.WriteLine("Pila: "+ pila.see());
            pila.remove();
            pila.forEach();

            Cola cola = new Cola();
            cola.add("Cola 1");
            cola.add("Cola 2");
            cola.add("Cola 3");

            Console.WriteLine("Cola: " + cola.see());
            cola.remove();
            cola.forEach();
        }
    }

    // Dificultad extra
    internal class Pila
    {
        private Stack<object> stack = new Stack<object>();

        public void add(object args)
        {
            stack.Push(args);
        }

        public void remove()
        {
            stack.Pop();
        }

        public object see()
        {
            return stack.Peek();
        }

        public void forEach()
        {
            foreach (var item in stack)
            {
                Console.WriteLine(item);
            }
        }

    }

    internal class Cola
    {
        private Queue<object> queue = new Queue<object>();

        public void add(object args)
        {
            queue.Enqueue(args);
        }

        public void remove()
        {
            queue.Dequeue();
        }

        public object see()
        {
            return queue.Peek();
        }

        public void forEach()
        {
            foreach (var item in queue)
            {
                Console.WriteLine(item);
            }
        }
    }
}
