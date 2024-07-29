using System;
using System.Collection.Generic;
using EjemploClaseYestructuras;

namespace EjemploClaseYestructuras
{
    // Clase Persona
    class Persona
    {
        
        // Atributos
        public string Nombre { get; set; }
        public int Edad { get; set; }

        / Consultor (inicializador)
        public Persona(string nombre, int edad)
            {
                Nombre = nombre;
                Edad = edad;
            }
    

       // Funcion para imprimir los atributos
       public void Imprimir()
          {
              Console.WriteLine($"Nombre: {Nombre}, Edad: {Edad}");
          }
    }
   // Clase Pila
    class Pila<T>
    {
        private List<T> elementos = new List<T>

        // Añadir un elemento a la pila
        public void Push(T elemento)
        {
            elementos.Add(elementos);
        }

        // Eliminar y retornar el elemento en la cima de la pila
        public T Pop()
        {
            if (elementos.Count == 0)
                throw new InvalidOperationExveption("La pila está vacía");
            T elemento = elementos[elementos.Count - 1];
            elementos.RemoveAt(elementos.Count - 1);
            return elemento;
        }

        // Retornar el número de elemento en la pila
        public int Count ()
        {
            return elementos.Count;
        }

        // Imprimir todos los elementos de la pila
        public void Imprimir()
        {
            foreach (var elemento in elementos)
            {
                Console.WriteLine(elemento);
            }
        }
    }

    // Clase cola
    class Cola<T>
    {
        private Queue<T> elementos = new Queue<T>();

        // Añadir un elemento a la cola
        public void Enqueue (T elemento);
        {
            elementos.Enqueue(elemento);
        }

        // Eliminar y retornar el primer elemento de la cola
        public T Dequeue()
        {
            if (elemntos.Count == 0)
                throw new InvalidOperationException("La cola está vacía.");
            return elementos.Dequeue();
        }

        // Retornar el número de elementos en la cola
        public int Count()
        {
            return elementos.Count;
        }

        // Imprimir todos los elemnentos de la cola
        public void Imprimir()
        {
            foreach (var elemto in elementos)
            {
                Console.WriteLine(elemento);
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
        
        // Parte 1: Clase persona
        Persona persona = new Persona("Juan", 25);

        // Imprimir los atributos iniciales
        persona.Imprimir();

        // Modificar los atributos
        persona.Nombre = "Pedro";
        persona.Edad = 30;

        // Imprimir los atributos modificados
        persona.Imprimir();


        // Parte 2: Uso de la pila
        Pila<int> pila = new Pila<int>();
        Pila.Push(1);
        Pila.Push(2);
        Pila.Push(3);
        Console.WriteLine("Elemento de la pila:");
        pila.Imprimir();
        Console.WriteLine($"Elemento eliminado de la pila: {pila.Pop()}");
        Console.WriteLine($"Número de ekemento en la pila: {pila.Count()}");


        // Parte 3: Uso de la cola
        Cola<int> cola = new Cola<int>();
        cola.Enqueue(1);
        cola.Enqueue(2);
        cola.Enqueue(3);
        Console.WriteLine("Elementos de la cola:");
        cola.Imprimir();
        Console.WriteLine($"Elemento eliminado de la cola: {cola.Dequeue()}");
        Console.WriteLine($"Nuúmero de elementos en la cola: {cola.Count()}");

        }
    }
/*

Explicación

Clase Persona:
Define los atributos Nombre y Edad.
Tiene un constructor para inicializar estos atributos.
La función Imprimir muestra los valores de los atributos.

Clase Pila<T>:
Implementa una pila genérica usando una lista interna.
Métodos Push, Pop, Count e Imprimir para añadir, eliminar, contar e imprimir elementos, respectivamente.

Clase Cola<T>:
Implementa una cola genérica usando una cola interna (Queue).
Métodos Enqueue, Dequeue, Count e Imprimir para añadir, eliminar, contar e imprimir elementos, respectivamente.

Programa Principal:
Demuestra cómo crear y utilizar instancias de Persona, Pila y Cola, realizando varias operaciones y mostrando los resultados.
*/
}
