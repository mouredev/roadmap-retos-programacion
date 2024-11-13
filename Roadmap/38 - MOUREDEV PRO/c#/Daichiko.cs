/*
 * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */

namespace retos_programacion._2024.Reto_38
{
    public class reto_38
    {
        //Enumerado de tipos de estatus
        internal enum Status {activo, inactivo};

        //clase base para manejos de usuarios
        internal class user
        {
            private int id;
            private string email;
            private Status status;

            public user(int id, string email, Status status)
            {
                this.id = id;
                this.email = email;
                this.status = status;
            }

            public int Id { get => id;}
            public string Email { get => email;}
            public Status Status { get => status;}
        }

        //logica principal del programa
        public class mainLogic
        {
            //lista de usuarios necesaria
            private List<user> users = new List<user>();

            //Obtener datos de usuarios de .CSV
            public bool ImportCSV(string path)
            {
                try
                {
                    var file = File.ReadAllLines(path);

                    for (int i = 1; i < file.Length; i++)
                    {
                        var values = file[i].Split(',');

                        var id = int.Parse(values[0].Trim());
                        var email = values[1].Trim();
                        var status = values[2].Trim().ToLower().Equals("activo") ? Status.activo : Status.inactivo;

                        var Usuario = new user(id, email, status);
                        users.Add(Usuario);
                    }
                    return true;
                }
                catch
                {
                    Console.WriteLine("Ha ocurrido un error al leer el csv. Asegúrese de que el fichero existe y tiene un formato correcto.");
                    return false;
                }
            }

            //Seleccion de ganadores
            public void SelectWinners ()
            {
                if (users.Count <= 0) 
                {
                    Console.WriteLine("No se han cargado usuarios al sistema");
                    return;
                };

                List<user> usersCopyActivos = (new List<user>(users)).Where(u => u.Status == Status.activo).ToList();

                if (usersCopyActivos.Count <= 0)
                {
                    Console.WriteLine("No hay mas usuarios en el sistema activos para seleccionar un ganador de suscripcion");
                    return;
                };

                // Crear selectores para cada tipo de premio
                IWinnerSelector subscriptionSelector = new SubscriptionWinnerSelector();
                IWinnerSelector discountSelector = new DiscountWinnerSelector();
                IWinnerSelector bookSelector = new BookWinnerSelector();

                // Seleccionar ganadores para cada tipo de premio
                SelectWinnerMessage(subscriptionSelector, usersCopyActivos, "No hay más usuarios activos para seleccionar un ganador de suscripción");
                SelectWinnerMessage(discountSelector, usersCopyActivos, "No hay más usuarios activos para seleccionar un ganador de descuento");
                SelectWinnerMessage(bookSelector, usersCopyActivos, "No hay más usuarios activos para seleccionar un ganador de libro");


            }

            //Se crea una funcion para mostrar los diferentes resultados del ganador
            private void SelectWinnerMessage(IWinnerSelector selector, List<user> users, string message)
            {
                if (users.Count <= 0)
                {
                    Console.WriteLine(message);
                    return;
                }

                selector.SelectWinner(users);
            }

            //Se crea una interfaz para la seleccion del ganador
            private interface IWinnerSelector
            {
                void SelectWinner(List<user> users);
            }

            //Se crea la clase para la seleccion del ganador de suscripcion
            private class SubscriptionWinnerSelector : IWinnerSelector
            {
                public void SelectWinner(List<user> users)
                {
                    // Selección del ganador de la suscripción
                    Random rnd = new Random();
                    int winnerIndex = rnd.Next(users.Count);
                    user winner = users[winnerIndex];
                    Console.WriteLine($"El ganador de la suscripción es: \n\t{winner.Id} - {winner.Email}");
                    users.RemoveAt(winnerIndex);
                }
            }

            //Se crea la clase para la seleccion del ganador de descuento
            private class DiscountWinnerSelector : IWinnerSelector
            {
                public void SelectWinner(List<user> users)
                {
                    // Selección del ganador del descuento
                    Random rnd = new Random();
                    int winnerIndex = rnd.Next(users.Count);
                    user winner = users[winnerIndex];
                    Console.WriteLine($"El ganador del descuento es: \n\t{winner.Id} - {winner.Email}");
                    users.RemoveAt(winnerIndex);
                }
            }

            //Se crea la clase para la seleccion del ganador del libro
            private class BookWinnerSelector : IWinnerSelector
            {
                public void SelectWinner(List<user> users)
                {
                    // Selección del ganador del libro
                    Random rnd = new Random();
                    int winnerIndex = rnd.Next(users.Count);
                    user winner = users[winnerIndex];
                    Console.WriteLine($"El ganador del libro es: \n\t{winner.Id} - {winner.Email}");
                    users.RemoveAt(winnerIndex);
                }
            }
        }
    }
}
