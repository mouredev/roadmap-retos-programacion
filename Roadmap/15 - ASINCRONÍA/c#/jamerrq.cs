/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */

using System;
using System.Threading;

namespace Roadmap15
{
    class Async
    {
        static void Main(string[] args)
        {
            Thread c = new(() => Function("C", 3));
            Thread b = new(() => Function("B", 2));
            Thread a = new(() => Function("A", 1));
            Thread d = new(() => Function("D", 1));

            c.Start();
            b.Start();
            a.Start();

            c.Join();
            b.Join();
            a.Join();

            d.Start();
            d.Join();
        }

        static void Function(string name, int seconds)
        {
            Console.WriteLine($"{name} starts at {DateTime.Now}");
            Thread.Sleep(seconds * 1000);
            Console.WriteLine($"{name} ends at {DateTime.Now}");
        }
    }
}
