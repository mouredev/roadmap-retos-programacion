/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */
using System;

namespace Roadmap21
{
    class Callbacks
    {
        public delegate void Callback();

        public void ProcessOrder(string dish, Callback confirm, Callback ready, Callback delivered)
        {
            Console.WriteLine($"🥫 Processing order for {dish}...");
            confirm();
            Random random = new Random();
            int seconds = random.Next(1, 11);
            System.Threading.Thread.Sleep(seconds * 1000);
            ready();
            System.Threading.Thread.Sleep(seconds * 1000);
            delivered();
        }

        public void Confirm()
        {
            Console.WriteLine("Order confirmed 📝");
        }

        public void Ready()
        {
            Console.WriteLine("Order ready 🍽");
        }

        public void Delivered()
        {
            Console.WriteLine("Order delivered 📥");
        }

        public void Run()
        {
            ProcessOrder("Pizza 🍕", Confirm, Ready, Delivered);
        }

        static void Main(string[] args)
        {
            Callbacks callbacks = new Callbacks();
            callbacks.Run();
        }
    }
}
