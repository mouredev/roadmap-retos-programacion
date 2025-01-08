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

using System;

namespace Roadmap19
{
    class Enumerations
    {
        public enum DaysOfWeek
        {
            Monday = 1,
            Tuesday,
            Wednesday,
            Thursday,
            Friday,
            Saturday,
            Sunday
        }

        public static void ShowDay(int day)
        {
            if (day < 1 || day > 7)
            {
                Console.WriteLine("Invalid day");
                return;
            }

            DaysOfWeek dayOfWeek = (DaysOfWeek)day;
            Console.WriteLine(dayOfWeek);
        }

        public enum OrderStatus
        {
            PENDING,
            SENT,
            DELIVERED,
            CANCELED
        }

        public class Order
        {
            public int Id { get; set; }
            public OrderStatus Status { get; set; }

            public Order(int id)
            {
                Id = id;
                Status = OrderStatus.PENDING;
            }

            public void Send()
            {
                if (Status == OrderStatus.PENDING)
                {
                    Status = OrderStatus.SENT;
                }
                else
                {
                    Console.WriteLine("Order already sent");
                }
            }

            public void Deliver()
            {
                if (Status == OrderStatus.SENT)
                {
                    Status = OrderStatus.DELIVERED;
                }
                else
                {
                    Console.WriteLine("Order must be sent first");
                }
            }

            public void Cancel()
            {
                if (Status == OrderStatus.PENDING)
                {
                    Status = OrderStatus.CANCELED;
                }
                else
                {
                    Console.WriteLine("Order cannot be canceled");
                }
            }

            public void ShowStatus()
            {
                Console.WriteLine($"Order {Id} is {Status}");
            }
        }

        public static void Main(string[] args)
        {
            ShowDay(1);
            ShowDay(7);
            ShowDay(8);

            Order order1 = new Order(1);
            order1.ShowStatus();
            order1.Send();
            order1.ShowStatus();
            order1.Send();
            order1.Deliver();
            order1.ShowStatus();

            Order order2 = new Order(2);
            order2.ShowStatus();
            order2.Send();
            order2.Deliver();
            order2.ShowStatus();
            order2.Cancel();
            order2.ShowStatus();
        }
    }
}
