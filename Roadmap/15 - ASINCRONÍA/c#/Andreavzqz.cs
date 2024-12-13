using System; 
using System.Threading.Tasks;

namespace ProgramaAsincrono
{
    class Program
    {
        static async task Main(string[] args)
        {

            //Dificultad extra
            Task taskC = EjecutarFuncionAsync("Funcion C", 3);
            Task taskB = EjecutarFuncionAsync("Funcion B", 2);
            Task taskA = EjecutarFuncionAsync("Funcion A", 1);

            //Esperar a que las funciones C, B Y A finalicen
            await task.WhenAll(taskC, taskB, taskA);

            //Ejecutar funcion D despues de las anteriores hayan terminado
            await EjecutarFuncionAsync("Funcion D", 1);
        }

        static async Task EjecutarFuncionAsync(string nombre, int segundos)
        {
            Console.WriteLine($"{nombre} empieza. Duracion: {segundos} segundos.");
            Console.WriteLine($"{nombre} empieza a las {DateTime.Now:T}.");

            await Task.Delay(segundos * 1000);

            Console.WriteLine($"{nombre} finaliza a las {DateTime.T}.");
        }
    }
/*

- Explicación

Método Main:
Este método es el punto de entrada del programa y se declara como async para permitir el uso de await.
Se crean tareas (Task) para las funciones C, B y A que se ejecutan en paralelo. Se utiliza Task.WhenAll para esperar que todas estas tareas finalicen antes de continuar con la ejecución.
Después de que las funciones C, B y A finalicen, se ejecuta la función D.

Método EjecutarFuncionAsync:
Este método representa una función que se ejecutará de manera asíncrona. Toma un nombre y una duración en segundos como parámetros.
Imprime el nombre de la función, la hora de inicio y la duración.
Utiliza Task.Delay para simular una tarea que toma tiempo en completarse. Task.Delay es una manera de esperar de forma asíncrona sin bloquear el hilo.
Una vez completado el tiempo de espera, se imprime la hora de finalización de la función.

*/

}
