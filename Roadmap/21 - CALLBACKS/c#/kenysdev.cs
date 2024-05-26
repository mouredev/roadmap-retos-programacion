/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* CALLBACKS
------------------------------------------
https://beetechnical.com/tech-tutorial/callbacks-in-csharp/

*/

#pragma warning disable CA1050
class Program {
/*
* EJERCICIO #1:
* Explora el concepto de callback en tu lenguaje creando un ejemplo
* simple (a tu elección) que muestre su funcionamiento.
*/
    // (opcional) Forma de representar y referenciar métodos con una firma específica.
    delegate void CallbackDelegate(string summands, int result);

    static void SumNumbers(int a, int b, CallbackDelegate callback) {
        int result = a + b;
        callback($"{a} + {b}", result);
    }

    static void MyCallback(string summands, int result) {
        Console.WriteLine($"La suma de {summands} es: {result}");
    }

/*
* EJERCICIO #2:
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

    static async Task ProcessOrder(
        string name, Func<string, Task> confirm, Func<string, Task> prepare, 
        Func<string, Task> serving) {
        Console.WriteLine($"-----\n* Procesando: '{name}' \n-----\n");
        await confirm(name);
        await prepare(name);
        await serving(name);
    }

    static int TimeRandom() {
        Random random = new();
        return random.Next(1, 11);
    }

    static async Task ConfirmOrder(string name) {
        int time = TimeRandom();
        Console.WriteLine($"* Confirmando {name}, espere {time} segundos.");
        await Task.Delay(time * 1000);
        Console.WriteLine($"- '{name}', ha sido confirmado.\n");
    }

    static async Task PrepareOrder(string name) {
        int time = TimeRandom();
        Console.WriteLine($"* Preparando, espere {time} segundos.");
        await Task.Delay(time * 1000);
        Console.WriteLine($"- '{name}', esta Listo.\n");
    }

    static async Task ServingOrder(string name) {
        int time = TimeRandom();
        Console.WriteLine($"* Sirviendo, espere {time} segundos.");
        await Task.Delay(time * 1000);
        Console.WriteLine($"- '{name}', ha sido entregado.\n");
    }

    static async Task Order(string dishName) {
        await ProcessOrder(dishName, ConfirmOrder, PrepareOrder, ServingOrder);
    }

    static async Task Main() {
        Console.WriteLine("EJERCICIO #1");
        SumNumbers(6, 6, MyCallback);
        SumNumbers(5, 2, MyCallback);

        Console.WriteLine("\nEJERCICIO #2");
        await Order("Baleadas");
        await Order("Tamales");
        await Order("Enchiladas");
    }
}
