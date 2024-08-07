/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */

namespace Roadmap
{
    internal class Reto19
    {
        enum Semana
        {
            Lunes = 1,
            Martes = 2,
            Miercoles = 3,
            Jueves = 4,
            Viernes = 5,
            Sabado = 6,
            Domingo = 7
        }

        static void Main(string[] args)
        {
            Console.WriteLine(ObtenerDia(5));

            // Reto extra
            Paquete paquete1 = new(1);
            Paquete paquete2 = new(2);
            
            Console.WriteLine(paquete1.ToString());
            paquete1.CanviarEstado(Estado.Enviado);
            Console.WriteLine(paquete1.ToString());
            paquete1.CanviarEstado(Estado.Entregado);
            Console.WriteLine(paquete1.ToString());

            Console.WriteLine(paquete2.ToString());
            paquete2.CanviarEstado(Estado.Entregado);
            Console.WriteLine(paquete2.ToString());
            paquete2.CanviarEstado (Estado.Cancelado);
            Console.WriteLine(paquete2.ToString());
            paquete2.CanviarEstado(Estado.Enviado);
            Console.WriteLine(paquete2.ToString()); 



        }

        static string ObtenerDia(int numDia)
        {
            return ((Semana)numDia).ToString();
        }
    }

    public enum Estado
    {
        Pendiente,
        Enviado,
        Entregado,
        Cancelado
    }

    public class Paquete
    {
        private int Id;
        private Estado Estado;

        public Paquete(int id, Estado estado = Estado.Pendiente)
        {
            Id = id;
            Estado = estado;
        }

        public void CanviarEstado(Estado estado)
        {
            if ((Estado == Estado.Pendiente & estado == Estado.Enviado) | (Estado == Estado.Enviado & estado == Estado.Entregado) | (Estado == Estado.Pendiente & estado == Estado.Cancelado))
                Estado = estado;
            else
                Console.WriteLine($"No se puede canviar el estado de {Estado} a {estado} del paquete {Id}");

        }

        public override string ToString()
        {
            return $"El paquete {Id} tiene el estado {Estado}";
        }
    }
}
