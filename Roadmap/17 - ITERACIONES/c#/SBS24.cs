// Author: Sandra Baigorri
using System;
using System.Linq;


namespace Iteracciones
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * EJERCICIO:
             * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
             * números del 1 al 10 mediante iteración.
             *
             * DIFICULTAD EXTRA (opcional):
             * Escribe el mayor número de mecanismos que posea tu lenguaje
             * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
             */
            int num = 1;
            Imprimir1();
            Imprimir2();
            Imprimir3();
            Imprimir4();
            Console.WriteLine("----------- IMPRIMIR5 -----------");
            Imprimir5(num);
        }
        //FOR
        private static void Imprimir1()
        {
            Console.WriteLine("----------- IMPRIMIR1 -----------");
            for (int i = 1; i <= 10; i++) 
            {
                Console.WriteLine("Número: " + i);
            }
        }
        //WHILE
        private static void Imprimir2()
        {
            Console.WriteLine("----------- IMPRIMIR2 -----------");
            int i = 1;
            while (i <= 10)
            {
                Console.WriteLine("Número: " + i);
                i++;
            }
        }
        //DO WHILE
        private static void Imprimir3()
        {
            Console.WriteLine("----------- IMPRIMIR3 -----------");
            int i = 1;
            do
            {
                Console.WriteLine("Número: " + i);
                i++;
            } 
            while (i <= 10);
        }
        //FOREACH
        private static void Imprimir4()
        {
            Console.WriteLine("----------- IMPRIMIR4 -----------");            
            foreach (int i in Enumerable.Range(1, 10))
            {
                Console.WriteLine("Número: " + i);      
            }
        }
        //RECURSIVIDAD
        private static void Imprimir5(int num)
        {                        
            if(num <= 10)
            {
                Console.WriteLine("Número: " + num);
                Imprimir5(num + 1); 
            }
        }
    }
}
