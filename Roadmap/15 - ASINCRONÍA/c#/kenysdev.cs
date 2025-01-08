/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  C#                            ║
╚═══════════════════════════════════════╝
-----------------------------------------------
* ASINCRONÍA
-----------------------------------------------
*/

#pragma warning disable CA1050
class Program {
    /*
    * EJERCICIO #1:
    * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
    * asíncrona una función que tardará en finalizar un número concreto de
    * segundos parametrizables. También debes poder asignarle un nombre.
    * La función imprime su nombre, cuándo empieza, el tiempo que durará
    * su ejecución y cuando finaliza.
    */
    static async Task Process(string name, int time)
    {
        Console.WriteLine($"- Iniciar función: {name} -> Duración: {time}");
        await Task.Delay(time * 1000);
        Console.WriteLine($"* Función {name} ha terminado.");
    }

    static async Task Test()
    {
        await Task.WhenAll(
            Process("Test 2", 4),
            Process("Test 1", 2)
        );
    }

    /*
    * EJERCICIO #2:
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

    static async Task InParallel()
    {
        await Task.WhenAll(
            Process("C", 3),
            Process("B", 2),
            Process("A", 1)
        );
    }

    static async Task Main()
    {
        await Test();
        await InParallel();
        await Process("D", 1);
    }
}
