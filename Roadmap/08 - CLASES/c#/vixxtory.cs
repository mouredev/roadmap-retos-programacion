using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Net.NetworkInformation;
using System.Runtime.Intrinsics.X86;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace RetosProgramacion
{
    class Program
    {
        static void Main(string[] args)
        {
            //Implemento los objetos basados en las clases
            Almuerzo menu_1 = new Almuerzo("Fideos Con Salsa", "Salsa bolognesa con fideos de verdura");
            Console.WriteLine(menu_1.getNombre());
            Console.WriteLine(menu_1.getDescripcion());

            Cola artistas = new Cola();
            artistas.AgregarElemento("Pintor");
            artistas.AgregarElemento("Escultor");
            artistas.ImprimirContenido();
            Console.WriteLine(artistas.NumeroDeElementos());
            artistas.EliminarElemento();
            artistas.ImprimirContenido();
        }
    }

    public class Almuerzo
    {
        private string nombre;
        private string descripcion;

        //Constructor predeterminado: inicializa variables por defecto
        public Almuerzo()
        {
            nombre = "Aprendiendo Logica junto a MoureDev";
            descripcion = "Soy una clase dedicada a Almuerzos";
        }
        //Constructor parametrizado
        public Almuerzo(string nombre, string descripcion)
        {
            this.nombre = nombre;
            this.descripcion = descripcion;
        }
        public string getNombre()
        {
            return nombre;
        }
        public string getDescripcion()
        {
            return descripcion;
        }   

    }
    public class Cola
    {
        private Queue<string> queue = new Queue<string>();
        public void AgregarElemento(string elemento)
        {
            queue.Enqueue(elemento);
        }
        public void EliminarElemento()
        {
            queue.Dequeue();
        }
        public int NumeroDeElementos()
        {
            return queue.Count();
        }
        public void ImprimirContenido()
        {
            foreach(string elemento in queue)
            {
                Console.WriteLine(elemento);
            }
        }
    }
    public class Pila
    {
        private Stack<string> stack = new Stack<string>();
        public void AgregarElemento(string elemento)
        {
            stack.Push(elemento);
        }
        public void EliminarElemento()
        {
            stack.Pop();
        }
        public int NumeroDeElementos()
        {
            return stack.Count();
        }
        public void ImprimirContenido()
        {
            foreach (string elemento in stack)
            {
                Console.WriteLine(elemento);
            }
        }
    }
}


