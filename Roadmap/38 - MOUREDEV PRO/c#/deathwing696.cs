using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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

namespace Reto_38
{
    internal class deathwing696
    {
        internal enum Estado_t
        {
            activo,
            inactivo
        };

        public class Usuario
        {
            private int id;
            private string email;
            private Estado_t estado;

            public int Id { get { return id; } }
            public string Email { get { return email; } }
            public Estado_t Estado { get { return estado; } }

            public Usuario(int id, string email, Estado_t status) 
            {
                this.id = id;
                this.email = email;
                this.estado = status;
            }
        }

        public class MoureDevPRO
        {
            private List<Usuario> usuarios = new List<Usuario>();
            public void ImportCSV(string path)
            {
                try
                {
                    var file = File.ReadAllLines(path);

                    for (int i = 1; i < file.Length; i++)
                    {
                        var values = file[i].Split(',');

                        var id = int.Parse(values[0].Trim());
                        var email = values[1].Trim();
                        var status = values[2].Trim().ToLower().Equals("activo") ? Estado_t.activo : Estado_t.inactivo;

                        var Usuario = new Usuario(id, email, status);
                        usuarios.Add(Usuario);
                    }
                }
                catch 
                {
                    Console.WriteLine("Ha ocurrido un error al leer el csv. Asegúrese de que el fichero existe y tiene un formato correcto.");
                }
            }

            internal void SelectWinners()
            {
                if (usuarios.Count <= 0)
                {
                    Console.WriteLine("No hay usuarios importados desde el csv, por tanto, no pueden haber ganadores");
                    return;
                }

                List<Usuario> usuarios_copy = new List<Usuario>(usuarios);

                //Seleccionamos el ganador de la suscripción
                Random rnd = new Random();
                var suscriptionIndex = rnd.Next(0, usuarios_copy.Count);
                Usuario selectedUser = usuarios_copy[suscriptionIndex];
                Console.WriteLine($"El ganador de la suscripción es: \n\t{selectedUser.Id} - {selectedUser.Email}");

                if (usuarios_copy.Count < 2)
                {
                    Console.WriteLine("No hay más usuarios importados desde el csv, por tanto, no pueden haber más ganadores");
                    return;
                }

                //Seleccionamos el ganador del descuento
                usuarios_copy.RemoveAt(suscriptionIndex);
                var discountIndex = rnd.Next(0, usuarios_copy.Count);                                    
                selectedUser = usuarios_copy[discountIndex];
                Console.WriteLine($"El ganador de la suscripción es: \n\t{selectedUser.Id} - {selectedUser.Email}");

                if (usuarios.Count < 2)
                {
                    Console.WriteLine("No hay más usuarios importados desde el csv, por tanto, no pueden haber más ganadores");
                    return;
                }

                //Seleccionamos el ganador del descuento
                usuarios_copy.RemoveAt(discountIndex);
                selectedUser = null;

                while (usuarios_copy.Count > 0)
                {
                    var bookIndex = rnd.Next(0, usuarios_copy.Count);
                    selectedUser = usuarios_copy[bookIndex];

                    if (selectedUser.Estado == Estado_t.activo)
                    {
                        break;
                    }
                    else
                    {
                        usuarios_copy.RemoveAt(bookIndex);
                        selectedUser = null;
                    }
                }

                if (selectedUser != null)
                    Console.WriteLine($"El ganador de la suscripción es: \n\t{selectedUser.Id} - {selectedUser.Email}");
                else
                    Console.WriteLine("No hay más usuarios importados desde el csv que tengan el estado activo, por tanto, no hay ganador del libro");
            }
        }

        static void Main(string[] args)
        {
            var moureDevPRO = new MoureDevPRO();
            moureDevPRO.ImportCSV($"{AppDomain.CurrentDomain.BaseDirectory}mouredevPro.csv");
            moureDevPRO.SelectWinners();



            Console.ReadKey();
        }
    }
}
