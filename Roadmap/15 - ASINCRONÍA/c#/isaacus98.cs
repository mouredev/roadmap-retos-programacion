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
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */

namespace Roadmap
{
    public class Reto15
    {
        static async Task Main(string[] args)
        {
            await Funcion("Isaac", 5000);

            // Reto extra
            await Task.WhenAll(Funcion("A", 3000), Funcion("B", 2000), Funcion("A", 1000));
            await Funcion("D", 1000);
        }

        static async Task Funcion(string nombre, int segundos)
        {
            Console.WriteLine($"nombre: {nombre}, tiempo de duración: {segundos}");
            await Task.Delay(segundos);
            Console.WriteLine("Finalización de la funcion");
        }
    }
}
