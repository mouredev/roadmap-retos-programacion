using System;
using System.Collections.Generic;

namespace R08___2024
{
    //Creacion de clase:
    class MiClase
    {
        //Defino los atributos, por ejemplo una persona:
        string nombre;
        int edad;

        //Aquí irían las propiedades, esto está en pocos lenguajes, de normal se usan getters y setters...
        //Las propiedades sirven para poder ver un atributo (get) o cambiar el atributo (set). Ejemplo:
        public string Nombre { get { return nombre; } set { nombre = value; } }
        //También podemos hacerla solo que retorne el valor pero que no lo cambie (set) para el data hiding:
        public int Edad { get { return edad; } }

        //Después de las propiedades van los constructores:
        public MiClase(string nombre, int edad)
        {
            this.nombre = nombre;
            this.edad = edad;
        }
        //Tambien podemos hacerlo sin parámetros para hacer readlines o asignar los valores que queramos:
        public MiClase()
        {
            this.nombre = "Ejemplo";
            this.edad = 99;
        }

        //Después de los constructores suelen ir los getter/setters podemos usar getter/setters o propiedades según queramos:
        public string getNombre()
        {
            return this.nombre;
        }
        public void setNombre(string nombre)
        {
            this.nombre = nombre;
        }

        //Después van los métodos de implementación como por ejemplo sería cumpliranyos:
        public void CumplirAnyos()
        {
            this.edad++;
        }

        //Y por último los de interfaz:
        public string VerInfo()
        {
            return $"{this.nombre},{this.edad}";
        }

        //De manera más profesional sobreescribiendo el método toString:
        public override string ToString()
        {
            return $"{this.nombre},{this.edad}";
        }

        //Dentro de la POO hay bastante más cosas pero esto es algo básico, una vez entendido sale solo ;)
    }

    //Dificultad adicional:
    //La T mayúscula es un parámetro de tipo genérico, significa que esto funciona con todos los tipos de datos.
    class Pila<T>
    {
        private Stack<T> elementos;

        public Pila()
        {
            elementos = new Stack<T>();
        }

        public void Push(T elemento)
        {
            elementos.Push(elemento);
        }

        public T Pop()
        {
            return elementos.Pop();
        }

        public int Count()
        {
            return elementos.Count;
        }

        public void Imprimir()
        {
            Console.WriteLine("Contenido de la pila:");
            foreach (var elemento in elementos)
            {
                Console.WriteLine(elemento);
            }
        }
    }

    class Cola<T>
    {
        private Queue<T> elementos;

        public Cola()
        {
            elementos = new Queue<T>();
        }

        public void Enqueue(T elemento)
        {
            elementos.Enqueue(elemento);
        }

        public T Dequeue()
        {
            return elementos.Dequeue();
        }

        public int Count()
        {
            return elementos.Count;
        }

        public void Imprimir()
        {
            Console.WriteLine("Contenido de la cola:");
            foreach (var elemento in elementos)
            {
                Console.WriteLine(elemento);
            }
        }
    }



    class Program
    {
        static void Main(string[] args)
        {
            MiClase objeto = new MiClase("Juan", 30);

            // Imprimir los atributos usando la función Imprimir
            Console.WriteLine("Valores iniciales:");
            Console.WriteLine(objeto.ToString());

            // Modificar los atributos
            objeto.Nombre = "Pedro";

            // Imprimir los atributos actualizados
            Console.WriteLine("Valores modificados:");
            Console.WriteLine(objeto.ToString());


            //Dificultad adicional:
            // Ejemplo de uso de la clase Pila
            Pila<int> pila = new Pila<int>();
            pila.Push(1);
            pila.Push(2);
            pila.Push(3);
            pila.Imprimir();
            Console.WriteLine("Número de elementos en la pila: " + pila.Count());
            pila.Pop();
            pila.Imprimir();
            Console.WriteLine("Número de elementos en la pila: " + pila.Count());

            // Ejemplo de uso de la clase Cola
            Cola<string> cola = new Cola<string>();
            cola.Enqueue("Uno");
            cola.Enqueue("Dos");
            cola.Enqueue("Tres");
            cola.Imprimir();
            Console.WriteLine("Número de elementos en la cola: " + cola.Count());
            cola.Dequeue();
            cola.Imprimir();
            Console.WriteLine("Número de elementos en la cola: " + cola.Count());

            Console.ReadKey();

        }
    }
}
