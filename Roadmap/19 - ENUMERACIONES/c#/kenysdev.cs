/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* ENUMERACIONES
------------------------------------------
https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum
https://learn.microsoft.com/es-es/dotnet/api/system.enum?view=net-8.0
*/

#pragma warning disable CA1050
class Program {
/*
* EJERCICIO 1:
* Empleando tu lenguaje, explora la definición del tipo de dato
* que sirva para definir enumeraciones (Enum).
* Crea un Enum que represente los días de la semana del lunes
* al domingo, en ese orden. Con ese enumerado, crea una operación
* que muestre el nombre del día de la semana dependiendo del número entero
* utilizado (del 1 al 7).
*/
    enum Weekday {
        MONDAY = 1,
        TUESDAY = 2,
        WEDNESDAY = 3,
        THURSDAY = 4,
        FRIDAY = 5,
        SATURDAY = 6,
        SUNDAY = 7
    }

    static string GetDay(int num) {
        return Enum.GetName(typeof(Weekday), num) ?? "'o'";
    }

    static int GetNumDay(string day) {
        return Enum.TryParse(day, out Weekday weekday) ? (int)weekday : 0;
    }

/*
* EJERCICIO 2:
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
    enum Status {
        PENDING,
        SHIPPED,
        DELIVERED,
        CANCELED
    }

    class Order(string identifier) {
        Status _status = Status.PENDING;

        public void Send() {
            Console.WriteLine("\nEnviar:");
            if (_status == Status.PENDING) {
                _status = Status.SHIPPED;
                Console.WriteLine(Info());
            } else {
                Console.WriteLine($"invalid operation, {Info()}");
            }
        }

        public void Cancelled() {
            Console.WriteLine("\nCancelar:");
            if (_status == Status.PENDING) {
                _status = Status.CANCELED;
                Console.WriteLine(Info());
            } else {
                Console.WriteLine($"invalid operation, {Info()}");
            }
        }

        public void Delivered() {
            Console.WriteLine("\nEntregar:");
            if (_status == Status.SHIPPED) {
                _status = Status.DELIVERED;
                Console.WriteLine(Info());
            } else {
                Console.WriteLine($"invalid operation, {Info()}");
            }
        }

        public string Info() {
            return $"{identifier} is {_status}";
        }
    }


    static void Main() {
        // _____________________________________
        Console.WriteLine(GetDay(7));
        Console.WriteLine(GetDay(3));
        Console.WriteLine(GetDay(8));

        Console.WriteLine(GetNumDay("TUESDAY"));
        Console.WriteLine(GetNumDay("FRIDAY"));
        Console.WriteLine(GetNumDay("abc"));

        // _____________________________________
        // Creación de pedidos
        Order libro1 = new("libro1");
        Order libro2 = new("libro2");
        Order libro3 = new("libro3");

        // Positivas
        Console.WriteLine("\n-----\nOperaciones exitosas:\n-----");
        libro1.Send();
        libro1.Delivered();
        libro2.Cancelled();

        // Negativas
        Console.WriteLine("\n-----\nOperaciones inválidas:\n-----");
        libro3.Delivered();
        libro2.Cancelled();
        libro1.Send();

        // Info
        Console.WriteLine("\n-----\nEstado de órdenes\n-----");
        Console.WriteLine(libro1.Info());
        Console.WriteLine(libro2.Info());
        Console.WriteLine(libro3.Info());
    }
}
